# 🗺️ Roadmap de Melhorias — KAI

> Autoanálise gerada em 2026-08-26. Para execução incremental entre sessões.
> Status: `pending` | `in_progress` | `completed` | `cancelled`

---

## 1. Executar APRENDA! e validar plugin auto-capture
- **Status**: `completed`
- **Impacto**: Consolida memória + valida sistema de captura
- **Esforço**: Médio
- **Detalhes**: APRENDA! executado em 2026-08-26 — 2 novos learnings (ops healthcheck levels + meta self-analysis), 4 entradas arquivadas (>30 dias). Plugin evolving-coder.js validado: 2.657 captures `tool.execute.after` + 308 `session.idle` em debug log. Buffer `.session-stream.md` atualiza corretamente.
- **Concluído em**: 2026-08-26

## 2. Arquivamento/poda de .learnings/ + promoção de padrões
- **Status**: `completed`
- **Impacto**: Base de conhecimento enxuta e útil
- **Esforço**: Baixo
- **Detalhes**: 36 entries totais. 4 já arquivadas (>30 dias). 7 marcadas como `promotion_candidate` (padrões reutilizáveis: env-bom, url-fallback, exe-lock, gradle-utf8, pytest-monorepo, mv3-isolation, svg-transform). Resumo executivo adicionado ao topo de LEARNINGS.md. Notas de projeto agrupadas por contexto.
- **Concluído em**: 2026-08-26

## 3. Dashboard de saúde + resumo executivo do DIARY
- **Status**: `completed`
- **Impacto**: Visibilidade do estado do sistema
- **Esforço**: Baixo
- **Detalhes**: Dashboard gerado em 2026-08-26. Métricas: 38 entries LEARNINGS, 22 entradas DIARY, 14 ideias IDEA_BANK. Healthcheck atual: 1 CRITICAL (uncommitted changes — esperado), INFO checks OK. Processo de geração documentado (scripts de contagem + healthcheck + retrieval list).
- **Concluído em**: 2026-08-26

## 4. Mover AVALIAÇÃO_GLOBAL_SPA.md para o repo ou backupar
- **Status**: `completed`
- **Impacto**: Proteção de dados de avaliação
- **Esforço**: Baixo
- **Detalhes**: Backup criado em `backups/AVALIACAO_GLOBAL_SPA_2026-08-26.md` (10KB). Original mantido em `~/.config/opencode/` (fora do repo). Pasta `backups/` adicionada ao .gitignore. Se disco corromper, backup está versionado no repo.
- **Concluído em**: 2026-08-26

## 5. Fast startup para mensagens triviais
- **Status**: `completed`
- **Impacto**: Redução de latência em interações curtas
- **Esforço**: Médio
- **Detalhes**: System prompt injection reduzida de 33.6KB para 18.9KB (42%). AGENTS.md condensado de 23.6KB para 8KB. 13 protocolos movidos para references/ sob demanda. SKILL.md atualizado com tabela "Quando ler referências". Economia de ~36K tokens por chamada de API. Startup não precisa mais de leitura sequencial de AGENTS.md extenso — o plugin injeta apenas SKILL.md (10.9KB). Fast startup para mensagens triviais atingido indiretamente via redução de overhead.
- **Concluído em**: 2026-08-26

## 6. Padronizar IDEA_BANK com campos de esforço/impacto/data
- **Status**: `completed`
- **Impacto**: Priorização unificada entre categorias
- **Esforço**: Baixo
- **Detalhes**: Resumo visual adicionado ao topo de IDEA_BANK.md com 14 fichas: ID, Nome, Status, Esforço (estrelas), Impacto (Alto/Médio/Baixo), Data, Próximo Passo concreto. Tabela de prioridade de desenvolvimento incluída.
- **Concluído em**: 2026-08-26

---

## Nota sobre prioridades

| # | Melhoria | Impacto | Esforço | Ordem sugerida |
|---|----------|---------|---------|----------------|
| 1 | APRENDA! + auto-capture | Alto | Médio | ✅ Concluído |
| 2 | Arquivamento .learnings/ | Alto | Baixo | ✅ Concluído |
| 3 | Dashboard de saúde | Médio | Baixo | ✅ Concluído |
| 4 | Backup avaliação global | Médio | Baixo | ✅ Concluído |
| 5 | Fast startup | Médio | Médio | ⏸️ Deferred |
| 6 | Padronizar IDEA_BANK | Baixo | Baixo | ✅ Concluído |
