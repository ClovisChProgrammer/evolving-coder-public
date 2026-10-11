---
name: bom-blind-ast-guards
description: "Guarda que parseia codigo-fonte por AST fica CEGA a arquivos com BOM: o U+FEFF inicial vira SyntaxError e um `except (SyntaxError, UnicodeDecodeError): continue` pula o arquivo em silencio - o guard passa e o defeito sobrevive exatamente no arquivo que ele nunca leu. Use ao escrever/revisar lint por AST, invariante de import, deteccao de chamada ou qualquer guarda sobre um repo Windows que pode conter arquivos com BOM. Triggers: 'guard AST', 'invariante de import', 'ast.parse', 'read_text read_bytes', 'arquivo com BOM', 'guard cego', 'falso-negativo de lint', 'SyntaxError U+FEFF', 'guard passou mas o defeito ficou'."
---

# Bom Blind Ast Guards

Guarda que faz `ast.parse(read_text(...))` nunca ve o arquivo que deveria proteger quando esse arquivo tem BOM. O BOM vira `SyntaxError`, o `except ...: continue` "defensivo" engole a excecao, e o guard fecha verde sobre um ponto cego. Regra: **parseie bytes, nunca texto decodificado**, e trate BOM explicitamente.

## Quick Reference

| Situation | Action |
|-----------|--------|
| Guard usa `ast.parse(read_text(...))` | Trocar por `ast.parse(caminho.read_bytes(), filename=str(caminho))` |
| `except (SyntaxError, UnicodeDecodeError): continue` | Proibido como "arquivo ilegivel" — esse except E' o falso-negativo |
| Repo Windows com arquivos escritos por `Set-Content -Encoding UTF8` (PS 5.1) | Assumir BOM possivel (ver `powershell-windows`); nunca depender de `read_text` |
| Necessidade de provar que o guard protege de verdade | Incluir um arquivo **COM BOM** entre os mutantes — se o guard o pular, o mutante nao morre |
| Guarda que pode `continue` sobre erro de parsing | Contar quantos arquivos leu e **falhar se a contagem cair** |
| Detectar BOM em diagnostico | Ler 3 bytes: `open(p, 'rb').read(3) == b'\xef\xbb\xbf'` |

## Usage

### O defeito

`read_text(encoding="utf-8")` **mantem** o BOM como U+FEFF no inicio da string. `ast.parse("\ufeffimport x")` levanta `SyntaxError: invalid non-printable character U+FEFF`. Um `except SyntaxError: continue` escrito para "ignorar arquivos de dados" passa a ser o mecanismo que **oculta justamente o arquivo protegido**.

### A correcao

Ler bytes (o parser ignora BOM sozinho) e nomear o arquivo para melhorar a mensagem de erro:

```python
# ERRADO — cego a BOM
tree = ast.parse(read_text(caminho, encoding="utf-8"))

# CERTO — le bytes; filename melhora o erro; BOM deixa de ser ponto cego
tree = ast.parse(caminho.read_bytes(), filename=str(caminho))
```

Se por algum motivo precisar decodificar antes, use `utf-8-sig` (remove o BOM):

```python
texto = caminho.read_bytes().decode("utf-8-sig")  # aceita COM e SEM BOM
```

### Nunca mascarar erro de parsing

Se a guarda varre varios arquivos, nao faca `continue` cego. Ou trate BOM explicitamente, ou **conte a cobertura**:

```python
lidos = 0
for caminho in repo.rglob("*.py"):
    try:
        tree = ast.parse(caminho.read_bytes(), filename=str(caminho))
    except SyntaxError:
        continue  # arquivo genuinamente invalido? entao torne isso visivel
    lidos += 1
    # ... checagens da guarda ...
assert lidos >= N_ESPERADO, f"guarda leu {lidos}/{N_ESPERADO} - ponto cego provavel (BOM?)"
```

## Examples

No SIGMAFLOW, `test_guard_escrita_atomica` vigiava escritas nao-atomicas em `data/`. O arquivo `src/storage.py` tinha BOM (emitido por uma ferramenta UTF-8-com-BOM). Logo a funcao `_escrever_espelho` — que reimplementava `temp + replace` **sem fsync** — nunca foi analisada. A fase P-1 foi declarada pronta com o defeito intacto no ponto cego.

Fix aplicado: `ast.parse(caminho.read_bytes(), filename=str(caminho))` em **todos** os guards, e o mutante **M7** exige que um arquivo com BOM seja **lido**, nao pulado. Quando M7 nao mata o mutante, o guard ainda esta cego.

## Source Learning

- Learning ID: LRN-20261002-001
- Pattern-Key: bom-invisible-em-guards-ast
- Original File: .learnings/LEARNINGS.md
- Relacionados: LRN-20260819-001 (BOM por `Set-Content -Encoding UTF8` no PS 5.1), `powershell-windows`
