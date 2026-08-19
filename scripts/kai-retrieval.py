#!/usr/bin/env python3
"""
KAI Retrieval v2 — memory search with semantic + keyword support
Uso:
    python scripts/kai-retrieval.py --build          # (re)build index + embeddings
    python scripts/kai-retrieval.py --query "termos"  # semantic search (default)
    python scripts/kai-retrieval.py --query-literal "termos"  # keyword search (legacy)
    python scripts/kai-retrieval.py --tags "tag1,tag2" # busca por tags
    python scripts/kai-retrieval.py --list            # lista entradas
    python scripts/kai-retrieval.py --project "name"  # filtra por projeto
"""
import json
import re
import sys
import os
import struct
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = SKILL_DIR / "scripts" / "knowledge-index.json"
EMBEDDINGS_PATH = SKILL_DIR / "scripts" / "knowledge-embeddings.npz"
DIARY_PATH = SKILL_DIR / "DIARY.md"
LEARNINGS_PATH = SKILL_DIR / ".learnings" / "LEARNINGS.md"
ERRORS_PATH = SKILL_DIR / ".learnings" / "ERRORS.md"

# Try to import fastembed (optional dependency for semantic search)
_FASTEMBED_AVAILABLE = False
_embedding_model = None

def _get_embedding_model():
    global _embedding_model, _FASTEMBED_AVAILABLE
    if _embedding_model is not None:
        return _embedding_model
    try:
        from fastembed import TextEmbedding
        _embedding_model = TextEmbedding()
        _FASTEMBED_AVAILABLE = True
        return _embedding_model
    except ImportError:
        _FASTEMBED_AVAILABLE = False
        return None
    except Exception:
        _FASTEMBED_AVAILABLE = False
        return None


def parse_diary(text):
    """Parse DIARY.md entries by ## headers"""
    entries = []
    current = None
    for line in text.split("\n"):
        if line.startswith("## ") and "\u00cdndice" not in line:
            if current:
                entries.append(current)
            title = line.replace("## ", "").strip()
            current = {"source": "diary", "title": title, "text": "", "tags": []}
        elif current:
            current["text"] += line + "\n"
    if current:
        entries.append(current)
    return entries


def parse_learnings(text):
    """Parse .learnings/ entries by [LRN-XXXXX] pattern"""
    entries = []
    current = None
    for line in text.split("\n"):
        m = re.match(r"^## \[(LRN-[\d-]+)\] (\S+)", line)
        if m:
            if current:
                entries.append(current)
            current = {"source": "learning", "id": m.group(1), "area": m.group(2),
                       "title": "", "text": "", "tags": [], "status": "unknown"}
        elif current:
            current["text"] += line + "\n"
            tm = re.match(r"^(\w[\w-]*):\s+(.+)", line)
            if tm:
                key, val = tm.group(1).lower(), tm.group(2).strip()
                if key == "status":
                    current["status"] = val
                elif key == "tags":
                    current["tags"] = [t.strip() for t in val.split(",")]
                elif key in ("summary", "title"):
                    current["title"] = val
    if current:
        entries.append(current)
    return entries


def tokenize(text):
    return re.findall(r"[a-zA-Z]\w+", text.lower())


def _entry_text_for_embedding(e):
    """Build a text string suitable for embedding from an entry."""
    parts = []
    title = e.get("title") or e.get("id", "")
    if title:
        parts.append(title)
    tags = e.get("tags", [])
    if tags:
        parts.append(" ".join(tags))
    text = e.get("text", "").strip()[:500]  # limit to 500 chars for embedding
    if text:
        parts.append(text)
    return " | ".join(parts) if parts else ""


def build_index():
    entries = []
    for path in [DIARY_PATH, LEARNINGS_PATH, ERRORS_PATH]:
        if path and path.exists():
            text = path.read_text(encoding="utf-8")
            if path == DIARY_PATH:
                entries.extend(parse_diary(text))
            else:
                entries.extend(parse_learnings(text))
    # Build token index for each entry
    for e in entries:
        tokens = tokenize(e["text"] + " " + e.get("title", ""))
        e["_tokens"] = Counter(tokens)
        e["_token_set"] = set(tokens)
    # Save keyword index
    serializable = []
    for e in entries:
        entry = {k: v for k, v in e.items() if not k.startswith("_")}
        entry["_token_count"] = len(e.get("_tokens", {}))
        serializable.append(entry)
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(serializable, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[KAI] Keyword index rebuilt: {len(entries)} entries -> {INDEX_PATH}")

    # Build embeddings if fastembed available
    model = _get_embedding_model()
    if model and entries:
        texts = [_entry_text_for_embedding(e) for e in entries]
        valid_indices = [i for i, t in enumerate(texts) if t.strip()]
        if valid_indices:
            valid_texts = [texts[i] for i in valid_indices]
            embeddings = list(model.embed(valid_texts))
            import numpy as np
            emb_array = np.array(embeddings, dtype=np.float32)
            # Save as .npz with metadata
            np.savez(
                str(EMBEDDINGS_PATH),
                embeddings=emb_array,
                indices=np.array(valid_indices, dtype=np.int32),
                version=np.array([2], dtype=np.int32),
            )
            print(f"[KAI] Embeddings built: {len(valid_indices)} entries -> {EMBEDDINGS_PATH}")
        else:
            print("[KAI] No embeddable entries found.")
    elif not model:
        print("[KAI] fastembed not available. Semantic search disabled. Install: pip install fastembed")

    return entries


def load_index():
    if INDEX_PATH.exists():
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return build_index()


def load_embeddings():
    """Load embeddings and metadata. Returns (embeddings_array, valid_indices) or None."""
    if not EMBEDDINGS_PATH.exists():
        return None
    try:
        import numpy as np
        data = np.load(str(EMBEDDINGS_PATH))
        return data["embeddings"], data["indices"]
    except Exception:
        return None


def query_semantic(terms, top_k=5):
    """Semantic search using cosine similarity."""
    model = _get_embedding_model()
    emb_data = load_embeddings()
    if not model or emb_data is None:
        # Fallback to keyword
        return query(terms, top_k)

    import numpy as np
    embeddings, valid_indices = emb_data
    entries = load_index()

    q_emb = list(model.embed([terms]))[0]
    # Cosine similarity (embeddings are normalized, so dot product works)
    sims = np.dot(embeddings, q_emb)
    # Get top-k
    top_indices = np.argsort(sims)[::-1][:top_k]

    results = []
    for idx in top_indices:
        entry_idx = int(valid_indices[idx])
        if entry_idx < len(entries):
            e = entries[entry_idx]
            score = float(sims[idx])
            title = e.get("title") or e.get("id", "sem titulo")
            source = e["source"]
            results.append((score, title, source, e.get("text", "")[:200]))
    return results


def query(terms, top_k=3, entries=None):
    """Keyword search (legacy)."""
    if entries is None:
        entries = load_index()
    query_tokens = set(tokenize(terms))
    if not query_tokens:
        return []
    scored = []
    for e in entries:
        tokens = set(tokenize(e.get("title", "") + " " + e["text"]))
        score = len(query_tokens & tokens)
        if score > 0:
            title = e.get("title") or e.get("id", "sem titulo")
            source = e["source"]
            scored.append((score, title, source, e["text"][:200]))
    scored.sort(key=lambda x: -x[0])
    return scored[:top_k]


def by_tags(tag_list, entries=None):
    if entries is None:
        entries = load_index()
    tags = [t.strip().lower() for t in tag_list.split(",")]
    results = []
    for e in entries:
        etags = [t.strip().lower() for t in e.get("tags", [])]
        if any(t in etags for t in tags):
            title = e.get("title") or e.get("id", "sem titulo")
            results.append((e["source"], title, etags, e["text"][:200]))
    return results


def list_entries(entries=None):
    if entries is None:
        entries = load_index()
    print(f"\n{'TIPO':<10} {'TITULO':<50} {'TAGS'}")
    print("-" * 90)
    for e in entries:
        title = e.get("title") or e.get("id", "?")
        tags = ", ".join(e.get("tags", []))[:30]
        print(f"{e['source']:<10} {title:<50} {tags}")
    print(f"\nTotal: {len(entries)} entries")


def by_project(project_name, entries=None):
    """Filter entries by project name (case-insensitive substring match)."""
    if entries is None:
        entries = load_index()
    project_lower = project_name.lower()
    results = []
    for e in entries:
        text = e.get("text", "")
        project_match = re.search(r"\*\*Project\*\*:\s*(.+)", text)
        if project_match and project_lower in project_match.group(1).lower():
            title = e.get("title") or e.get("id", "sem titulo")
            results.append((e["source"], title, e.get("tags", []), e["text"][:300]))
            continue
        title = e.get("title", "")
        if project_lower in title.lower():
            results.append((e["source"], title, e.get("tags", []), e["text"][:300]))
    return results


def format_result(r, detail=False):
    score, title, source, preview = r
    s = f"[{source}] {title} (score: {score:.3f})" if isinstance(score, float) else f"[{source}] {title} (score: {score})"
    if detail:
        s += f"\n  {preview.strip()}"
    return s


if __name__ == "__main__":
    if "--build" in sys.argv:
        build_index()
    elif "--query" in sys.argv:
        idx = sys.argv.index("--query")
        terms = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        if not terms:
            print("[KAI] Uso: --query \"texto\"")
            sys.exit(1)
        results = query_semantic(terms)
        if results:
            print(f"\n[KAI] Top {len(results)} resultados (semântico): '{terms}'\n")
            for r in results:
                print(format_result(r, detail=True))
                print()
        else:
            print(f"[KAI] Nenhum resultado para: '{terms}'")
    elif "--query-literal" in sys.argv:
        idx = sys.argv.index("--query-literal")
        terms = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        if not terms:
            print("[KAI] Uso: --query-literal \"texto\"")
            sys.exit(1)
        results = query(terms)
        if results:
            print(f"\n[KAI] Top {len(results)} resultados (keyword): '{terms}'\n")
            for r in results:
                print(format_result(r, detail=True))
                print()
        else:
            print(f"[KAI] Nenhum resultado para: '{terms}'")
    elif "--tags" in sys.argv:
        idx = sys.argv.index("--tags")
        t = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        results = by_tags(t)
        if results:
            print(f"\n[KAI] Entradas com tags: '{t}'\n")
            for src, title, tags, preview in results:
                print(f"[{src}] {title}")
                print(f"  tags: {tags}")
                print()
        else:
            print(f"[KAI] Nenhuma entrada com tags: '{t}'")
    elif "--list" in sys.argv:
        list_entries()
    elif "--project" in sys.argv:
        idx = sys.argv.index("--project")
        project = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        if not project:
            print("[KAI] Uso: --project <nome-do-projeto>")
        else:
            results = by_project(project)
            if results:
                print(f"\n[KAI] Entradas do projeto '{project}':\n")
                for src, title, tags, preview in results:
                    print(f"[{src}] {title}")
                    if tags:
                        print(f"  tags: {', '.join(tags)}")
                    print(f"  {preview.strip()[:200]}...")
                    print()
                print(f"Total: {len(results)} entradas")
            else:
                print(f"[KAI] Nenhuma entrada encontrada para o projeto: {project}")
    else:
        entries = build_index()
        print(f"[KAI] Pronto. Use --query, --query-literal, --tags, --list, ou --project")
