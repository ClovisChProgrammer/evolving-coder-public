# Comando Global de Resolucao — RESOLVA!

**Gatilho** — mensagem do usuario em linha unica, case-insensitive: RESOLVA! ou RESOLVA.

**Comportamento** — resolver TUDO que estiver pendente (fila de tarefas, CRITICAL/WARNING do healthcheck, itens em aberto reportados) SEM pedir autorizacao — incluindo commit e push de pendencias ja revisadas.

**Excecoes (bloqueiam a execucao)** — se o item pendente envolver:
1. **Seguranca dos dados do usuario** (exposicao potencial de secrets/dados privados, conteudo sensivel em diff/staging)
2. **Comprometimento do funcionamento da KAI** (destruicao de memoria/buffer, corrupcao de arquivos do sistema)

→ NAO resolver. Emitir imediatamente mensagem contendo EXATAMENTE o tipo de warning que o usuario precisa saber (nivel + causa precisa + risco) e aguardar instrucao explicita.
