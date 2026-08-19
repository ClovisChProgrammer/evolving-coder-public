# URL Access Fallbacks — Receita de Acesso Web

> Lido sob demanda quando uma integração web falha (redirect, bloqueio, HTML ilegível).
> Núcleo da lição: [LRN-20260805-001] + [LRN-20260805-002] (Pattern-Keys: `url-access-fallback`, `html-extraction-anchor-regex`).

## 1. Fallback de documento canônico

Quando a URL "de diretório" falha ou devolve **308/3xx** (típico de Docusaurus, VitePress, SPAs estáticas):

1. Sem barra final? Experimente **com** a barra.
2. Com barra e ainda 308/layout? Anexe o documento canônico:

```
https://site/dir/            → https://site/dir/index.html   (ou index.htm)
```

O servidor estático serve o documento na rota `/dir/` como `/dir/index.html`. Antes de desistir, teste o fallback (limite global: máx. 2 tentativas; reportar ao usuário após 2 falhas).

## 2. Fetch de HTML cru (onde o webfetch falha)

PowerShell:

```powershell
(New-Object System.Net.WebClient).DownloadString($url)
```

Python (httpx, segue redirects + User-Agent de navegador):

```python
import httpx
r = httpx.Client(follow_redirects=True, timeout=30,
                 headers={"User-Agent": "Mozilla/5.0"}).get(url)
html = r.text
```

## 3. Extração de valores de HTML minificado

Páginas de build (minify) vêm em **1 linha**. Passos:

1. Remover tags: `re.sub(r"<[^>]+>", "", html)`
2. Regex **com âncora de terminação** no fim do padrão — sem ela o `+`/`.*` casa guloso e captura texto além do valor:

```python
# Base64 com padding "=" delimitando o fim do token:
re.findall(r"Authorization:\s*APIKey\s+([A-Za-z0-9+/]+={1,2})", texto, re.IGNORECASE)
```

3. Placeholders (`[Chave Pública]`, etc.) não casam (sem padding base64) — pegue a **última** ocorrência via `findall` para ignorá-los.

## 4. Regras

- Máx. 2 tentativas consecutivas em endpoint externo; após 2 falhas, reportar erro completo e aguardar instrução (global-rules #1).
- Nunca logar/expor valores extraídos de chaves reais (global-rules #2).
- Testar extração com **fixture local** do HTML real (sem rede), cobrindo positivo + negativo.
