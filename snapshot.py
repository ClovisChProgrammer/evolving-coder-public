import shutil, json, os, sys, subprocess, datetime, argparse

SNAPSHOT_DIR = "snapshots"
INDEX_FILE = os.path.join(SNAPSHOT_DIR, "snapshot_index.json")
MAX_SNAPSHOTS = 5


def run_git(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)))
    if result.returncode != 0:
        print(f"Erro git: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def load_index():
    if not os.path.exists(INDEX_FILE):
        return []
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index(index):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def cmd_take(message):
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    index = load_index()

    commit = run_git(["git", "rev-parse", "HEAD"])
    snapshot_id = f"snap-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    snap_path = os.path.join(SNAPSHOT_DIR, snapshot_id)
    os.makedirs(snap_path, exist_ok=True)

    files = run_git(["git", "ls-files"]).split("\n")
    files = [f for f in files if f]

    for f in files:
        src = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)
        dst = os.path.join(snap_path, f)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(src):
            shutil.copy2(src, dst)

    entry = {
        "id": snapshot_id,
        "timestamp": datetime.datetime.now().isoformat(),
        "message": message,
        "commit": commit,
        "files": files,
    }

    index.append(entry)
    while len(index) > MAX_SNAPSHOTS:
        old = index.pop(0)
        old_path = os.path.join(SNAPSHOT_DIR, old["id"])
        if os.path.exists(old_path):
            shutil.rmtree(old_path)

    save_index(index)
    print(f"Snapshot '{snapshot_id}' salvo: {message}")
    print(f"  Commit: {commit[:12]}")
    print(f"  Arquivos: {len(files)}")


def cmd_list():
    index = load_index()
    if not index:
        print("Nenhum snapshot encontrado.")
        return
    print(f"{'ID':<28} {'Data':<22} {'Commit':<12} {'Mensagem'}")
    print("-" * 80)
    for s in index:
        ts = s["timestamp"][:19]
        print(f"{s['id']:<28} {ts:<22} {s['commit'][:12]:<12} {s['message']}")


def cmd_rollback(steps):
    index = load_index()
    if not index:
        print("Nenhum snapshot para restaurar.")
        return

    if steps > len(index):
        print(f"Só existem {len(index)} snapshots. Usando o mais antigo.")
        steps = len(index)

    target = index[-steps]
    snap_path = os.path.join(SNAPSHOT_DIR, target["id"])
    if not os.path.exists(snap_path):
        print(f"Snapshot '{target['id']}' não encontrado em disco.")
        return

    root = os.path.dirname(os.path.abspath(__file__))
    for f in target["files"]:
        src = os.path.join(snap_path, f)
        dst = os.path.join(root, f)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)

    print(f"Rollback de {steps} snapshots concluído.")
    print(f"  Snapshot: {target['id']}")
    print(f"  Mensagem: {target['message']}")
    print(f"  Arquivos restaurados: {len(target['files'])}")
    print("  Commit original:", target["commit"][:12])
    print("  ⚠️  Alterações estão no working tree. Revise com 'git diff' antes de commitar.")


def main():
    parser = argparse.ArgumentParser(description="Snapshot tool — rollback rápido")
    sub = parser.add_subparsers(dest="command")

    p_take = sub.add_parser("take", help="Tirar snapshot")
    p_take.add_argument("-m", "--message", required=True, help="Descrição do que vai fazer")

    p_roll = sub.add_parser("rollback", help="Restaurar snapshot")
    p_roll.add_argument("steps", type=int, nargs="?", default=1, help="Quantos snapshots voltar (1-5)")

    sub.add_parser("list", help="Listar snapshots")

    args = parser.parse_args()
    if args.command == "take":
        cmd_take(args.message)
    elif args.command == "list":
        cmd_list()
    elif args.command == "rollback":
        cmd_rollback(args.steps)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
