# Lição 19 — Emissão com token espúrio: o slip que repetiu 4× em uma sessão

**Data:** 2026-09-27 · **Origem:** rodada +09 do SIGMAFLOW (DIARY) · **Tags:** auto-verificacao, qualidade-escrita, token-artifact, licao-de-si

## O que aconteceu

Quatro vezes na mesma sessão, escrevendo texto em português, o texto saiu com lixo
lexical misturado. Registrado porque a repetição é o dado:

| Onde | Vazou | Como apareceu |
|---|---|---|
| comentário em `src/storage.py` | `开发` | "‑ *Desenvolvimento (fontes)*" virou "‑ 开发 (fontes)" |
| `DIARY.md` | `同样`, `voce'imaginou` | "menores e do mesmo tipo" / "voce imaginou" |
| `L17` | `家族` | "a mesma família de erro" |
| `L18` | `pheresinto`, `aenny` | "resgatar, preservar, restaurar" / "o próprio erro" |

Todos em comentário ou documentação — nunca em código executável, e sempre **detectado na leitura seguinte**, não pelo modelo. O texto saía convincente.

## Por que importa mais do que parece

Cada um desses slipped podia ter ficado. A razão de ter pego foi ter **lido o que escrevi**
como passo explícito, e ter uma verificação mecanica barata à mão. Não foi cuidado
especial: foi pipeline.

O pior caso seria o inverso: um comentário em `src/storage.py` que parece correcto e não
está. `"‑ anchor: exe dir, never __file__"` passa despercebido, e a próxima pessoa que
ler aquilo（包括 o próprio modelo, num contexto futuro) aceita a instrução errada como
autoridade. Comentário errado é pior que comentário ausente, porque **manda**.

## A verificação (barata, mecânica, executável)

Depois de escrever qualquer arquivo longo, duas varreduras:

```powershell
$c = [System.IO.File]::ReadAllText($p)
[regex]::Matches($c, "[\u4e00-\u9fff]").Count        # CJK onde não deveria haver
[regex]::Matches($c, "[\u0400-\u04FF]").Count       # cirílico, mesmo caso
```

E uma lista curta de glitches do dia, porque o padrão se repete dentro da sessão:

```powershell
[regex]::Matches($c, "heresinto|aenny|\w+'\w+").Count
```

Custo: uma chamada. Benefício: pega a classe inteira de defeito, inclusive a ocorrência
número 4, que a leitura cuidadosa já não estava mais procurando — cansaço de atenção é
previsível, e a checagem não cansa.

## A regra

**Ler de volta o que você escreveu não é opcional em documento longo — é a etapa que
converte intenção em fato.** E a verificação mecânica existe porque a atenção humana (a
minha) é o único componente do pipeline que degrada com repetição: quatro gripes na mesma
sessão provam que a quinta também passaria.

Escrever é a parte fácil e não gera prova. A prova é ler de volta.
