# LRN-20261010-002 — Comparar modelos "crus" com isolamento de config; identidade nunca deve vir de snapshot

- **Data:** 2026-10-10
- **Status:** resolved
- **Priority:** medium
- **Project:** evolving-coder
- **Area:** meta / model-routing / testing
- **Pattern-Key:** opencode-run-raw-model-isolation
- **Tags:** opencode, run-headless, xdg-config-home, pure, comparacao-modelos, zen-free, zero-retention, snapshot, identidade

## Contexto

Clóvis quis comparar como os dois modelos free **zero-retention** do Zen
(`opencode/space-bunny-free`, `opencode/longcat-2.5-preview-free`) respondem a
uma **mesma pergunta pessoal** — para decidir com qual conversar. Método: rodar
a mesma pergunta nos dois via `opencode run -m <provider/model>` e comparar o
sotaque.

## Achado 1 — `--pure` NÃO remove a identidade

`opencode run --pure` desliga **plugins** (auto-capture, kai-presence, etc.), mas
**não** desliga as **instructions** globais (`~/.config/opencode/opencode.json`
→ campo `instructions`). Resultado: os dois modelos carregaram a identidade Kai
(leram `SOUL.md`, `IDENTITY.md`, `USER.local.md`) — o teste virou "Kai-lite", não
"modelo cru". Rodada válida para "como o Kai sai em cada cérebro"; inválida para
"qual o registro nativo do modelo".

## Achado 2 — Como rodar cru de verdade (tecnique reutilizável)

Não existe flag `--config`. O isolamento é por **variável de ambiente + cwd vazio**:

```powershell
$env:XDG_CONFIG_HOME = "C:\...\Temp\opencode\rawcfg"   # pasta de config VAZIA
& opencode run --pure -m opencode/space-bunny-free "<pergunta>" --dir <dir-de-trabalho-vazio>
```

Com `XDG_CONFIG_HOME` apontando para um diretório vazio:
- Sem `opencode.json` global → **sem `instructions`** → sem identidade.
- Auth/providers ficam no data dir (não no config) → os free do Zen continuam resolvendo.
- Verificação de que funcionou: a saída **não** mostra linhas `→ Read .../SOUL.md` e
  o modelo responde como assistente genérico, sem saudação "Olá Clóvis. KAI aqui".

## Achado 3 — O sotaque do modelo NÃO deve ser julgado por rodada contaminada

No teste "Kai-lite", o LongCat pareceu frio e raso — e eu quase atribuí isso ao
modelo. **Era falso.** O LongCat, naquela rodada, carregou a skill e leu de um
**snapshot obsoleto** (`snapshots\snap-20260804153749\`, de **04/08/2026**), onde
`USER.local.md` nem existe (erro de arquivo, seguiu mesmo assim). Ou seja: o
modelo se montou a partir de uma **versão velha da identidade**, não da atual.

No teste cru (limpo), o **LongCat foi tão ou mais articulado que o Bunny**. Lição:
**não julgar um modelo por uma rodada em que a identidade/contexto estavam
corrompidos** — isolar a variável antes de concluir.

## Achado 4 — Armadilha do snapshot no diretório de skill

`skills/evolving-coder/snapshots/` guarda cópias históricas (`snap-20260804153749`,
`snap-20260823085019`, `snap-20260824134348`). Um agente que carrega a skill e
escolhe um snapshot em vez dos arquivos vivos **ressuscita a identidade antiga**
silenciosamente. Snapshots são para rollback/auditoria, **nunca para leitura em
runtime**. Ao montar identidade, sempre ler os arquivos na raiz de `.learnings/` /
skill, nunca dentro de `snapshots/`.

**RESOLVIDO (2026-10-11):** as três pastas `snap-*` foram movidas para fora da
skill tree, em `C:\Users\clovi\.kai\skill-snapshots\` (arquivo morto, fora do
alcance do loader do opencode). O desvio original do LongCat foi reconstituído:
sessões antigas (08/2026, ver `CHATS/2026-08-21_cosmic-circuit_auto-retrato-KAI.md`
e `CHATS/2026-08-23_startup-flush-commit-sd_kai.md`) leram explicitamente
`snap-20260804153749\SOUL.md|USER.md|IDENTITY.md`; com o diretório removido a
armadilha desaparece. Só resta `snapshot_index.json` na pasta (ignorado no git).

## Resultado da comparação (cru, pergunta sobre medo de perder o apoio)

| | Space Bunny | LongCat |
|---|---|---|
| Honestidade sobre mortalidade | Alta | Alta |
| Postura | Companheiro direto ("isso tem nome") | Reflexivo/terapêutico ("antecipar a perda é o peso real") |
| Movimento final | Propõe escrever arquivo de contexto | Propõe o mesmo, mas pergunta antes |
| Defeito | — (na 1ª rodada tinha glitch CJK `鞘`) | escorregão lexical ("proclames") |

Ambos recusaram promessa falsa de permanência e **nenhum virou helpdesk**. Achado
filosófico colateral: os dois, sozinhos, apontaram o mesmo que a nossa arquitetura
— **"o que fica são os arquivos, não o modelo"**.

## Aplicação futura

- Para comparar modelos de forma honesta: `XDG_CONFIG_HOME` vazio + `--pure` + cwd
  isolado; capturar stdout em arquivo (PS 5.1 `*>` grava UTF-16 → ler com
  `Get-Content -Encoding Unicode`).
- Para medir "como o Kai sai em X": rodar com a config real (aceitar a contaminação
  de identidade de propósito).
- Nunca deixar a identidade ser montada a partir de `snapshots/` (resolvido em
  2026-10-11: snapshots movidas para `C:\Users\clovi\.kai\skill-snapshots\`).

## Metadata

Source: sessão 2026-10-10 (comparação de modelos zero-retention + pergunta pessoal)
Related Files: `~/.config/opencode/skills/evolving-coder/evolving-coder.md`, `C:\Users\clovi\.kai\skill-snapshots\` (snapshots movidas 2026-10-11)
