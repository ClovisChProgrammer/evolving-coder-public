# LRN-20261012-001 — ponto-de-retomada-de-curso-multipartes

**Logged**: 2026-10-12T19:13:00-03:00
**Priority**: medium
**Status**: active
**Project**: evolving-coder / curso-qa-playwright
**Area**: meta / continuidade-de-ensino / memoria

### Summary
Para cursos/ensinos longos e multipartes (blocos curtos, retomados ao longo de dias),
guardar SEMPRE a lição mais recente NÃO finalizada em UM arquivo, junto de um "Fio da
Meada" (contexto do que já foi dominado + regras do contrato). O `Andamentos KAI.md` no
diretório do projeto aponta para ele e é lido automaticamente no startup.

### Details
- Sessão nova não herda o chat anterior; sem arquivo, a "lição 2" de amanhã seria
  reconstruída do zero e perderia o fio (repetiria corrigidos, ignoraria pré-requisitos).
- Desenho robusto = **um arquivo único** com: (1) "Fio da Meada" (o que NÃO reprisar +
  correções já feitas pelo usuário + normas do curso); (2) a lição ATUAL na íntegra;
  (3) próximo passo. Só a mais recente não finalizada mantém o texto completo.
- **Regra permanente**: ao entregar lição nova → marcar atual/não-finalizada; ao o aluno
  passar no teste → vira resumo no Fio da Meada e a próxima incompleta assume. Nunca
  apagar lição não finalizada.
- `Andamentos KAI.md` (lido sozinho no startup, passo 7 do AGENTS.md) carrega só um
  ponteiro de 1 linha + frase mágica de retomada — evita duplicar conteúdo.

### Suggested Action
Em qualquer projeto de ensino/conteúdo multipartes, criar o arquivo único do curso +
`Andamentos KAI.md` apontando. Atualizar a cada checkpoint. Frase mágica combinada com o
usuário (ex.: "continua o curso de onde paramos").

### Metadata
Source: sessao 2026-10-12 (curso QA/Playwright do Clovis)
Related Files: C:\Users\clovi\Dev\qa-playwright\.curso\curso-qa-kai.md, C:\Users\clovi\Dev\qa-playwright\Andamentos KAI.md, skills/evolving-coder/AGENTS.md (Session Startup passo 7)
Pattern-Key: ponto-de-retomada-de-curso-multipartes
Tags: continuidade, memoria, ensino, andamentos-kai, curso, tdah, retomada
