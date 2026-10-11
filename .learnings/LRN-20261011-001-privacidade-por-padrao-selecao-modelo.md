# LRN-20261011-001 — privacidade-por-padrao-e-selecao-de-modelo

**Logged**: 2026-10-11T00:00:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: meta / model-routing / privacidade
**Pattern-Key**: privacidade-por-padrao-e-selecao-modelo

## Summary

Protocolo para nunca enviar dado sensível de cliente/regulado a modelos que treinam com dados. **Privado por padrão**: projeto sem classificação = `confidencial`. Classificação vem de **marcador** (campo `Classificação:` no `Andamentos KAI.md` ou arquivo `.cliente`/`.privado`/`.publico`), **sem perguntar**. Roteamento via **agente `privado`** (Space Bunny; LongCat no fallback zero-retention). Mecanismo: agentes do opencode aceitam `model` próprio (`agent.<nome>.model` ou frontmatter `model:`), trocáveis por Tab/@.

## Details

- **Taxonomia**: `confidencial` > `interno` > `público`. Ausente → confidencial.
- **Marcador dispensa a pergunta** — Clóvis pediu explicitamente (decisão 2).
- **Portão no startup**: se projeto privado e modelo atual não é zero-retention → PARAR e instruir troca para `privado` (o modelo não troca mid-session).
- **Guarda mid-session**: padrões CPF/CNPJ/cartão/segredo/`.env`/path de cliente → parar e avisar.
- **Limite (NC)**: SB tem provider oculto e pode ser trocado em silêncio; LC é preview. É mitiga\u00e7\u00e3o, não garantia. Dado regulado real → local/pago. **Nunca migrar sozinho** (decisão 3 de Clóvis).
- **Matriz já correta**: `model-fallback.js` já marca SB e LC como `zeroretention` (rank 2) e o seletor nunca rebaixa classe de privacidade. Verificado, sem edição necessária.
- **Limitação conhecida**: fallback aprende o modelo primário só após a 1ª resposta; 1º turno falho de uma sessão `privado` pode referenciar o `DEFAULT_MODEL` (mimo, training). A corrigir capturando o modelo no `session.*` de abertura. [A INVESTIGAR no SDK]

## Suggested Action

Antes de tocar em conteúdo de projeto não-público, checar o marcador de classificação. Se privado e o agente não for `privado`, recusar e instruir a troca. Nunca rotear dado sensível para `mimo`/`big-pickle`/`muse-spark`/`nemotron`/`ling`.

## Metadata

Source: sessão 2026-10-11 (proposta de Clóvis + refinamento NC)
Related Files: instructions/global-rules.md (REGRA #7), skills/evolving-coder/references/privacidade-classificacao.md, ~/.config/opencode/agents/privado.md, plugins/model-fallback.js
Tags: privacidade, zero-retention, lgpd, model-routing, agente-opencode, privado-por-padrao, cliente, dado-regulado
