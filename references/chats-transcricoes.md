# Arquivo de Transcricoes — CHATS (v2)

## Politica Geral

Toda sessao gera transcricao arquivada:

1. **Pasta de trabalho**: <skill-dir>\CHATS\ (= ~/.config/opencode/skills/evolving-coder/CHATS/, versionada no repo PRIVADO)
2. **Export nativo**: opencode export <sessionID> executado VIA PYTHON subprocess (capture_output=True, decode utf-8) — NUNCA via redirect > do PowerShell 5.1 (corrompe UTF-8). Gravar DIRETO no <skill-dir>\CHATS\
3. **Conversor reutilizavel**: <skill-dir>\CHATS\convert_session.py
4. **Nome de arquivo**: YYYY-MM-DD_<slug-da-sessao>_<descritor-do-projeto>.md
5. **Cabecalho obrigatorio**: participantes, sistema/modelo, contexto, inicio/fim em BRT, duracao da janela
6. **Corpo**: dialogos verbatim (👤 Clovis SPA / 🔧 Kai SPD), tool calls como resumo 1-linha, ruido interno filtrado
7. **Commit/push OBRIGATORIO**: incluir o .md no commit/push do repo PRIVADO sempre. Repo PUBLICO recebe apenas o MODULO — transcricoes NUNCA vao ao publico

## Auto-Salvamento (sessoes pessoais)

### Marcadores de sessao pessoal (salva SEM perguntar)

A transcricao e gerada automaticamente no shutdown quando a sessao tem QUALQUER um destes:

- **Tema de identidade**: nome de KAI, relacao SPD/SPA, "nossa relacao", reflexoes existenciais sobre o sistema
- **Mudancas de sistema**: novos skills, protocolos, mudancas em SOUL.md, USER.md, IDENTITY.md, PROTOCOL.md
- **Tom emocional/conversacional**: conversa nao-tecnica sobre projetos pessoais, arte, filosofia, "nostalgia"
- **Decisoes que moldam o sistema**: aprovacao de novos protocolos, mudancas estruturais de comportamento
- **Conversa >50% nao-tecnica** (medida por proporcao de mensagens)

### Sessoes hibridas

Se parte da sessao e tecnica e parte pessoal → tratar como pessoal (o que importa deve ser preservado).

## Regra de Pergunta (CAMBIO FECHADO / >SD)

### Quando PERGUNTAR

- Sessao SIGNIFICATIVA: decisoes importantes, trabalho em projetos, mudancas de sistema, >10 interacoes
- Frase exata: `Quer que eu salve a transcricao desta sessao? [s/n]`
- Se sim → gerar transcricao + commit (sem perguntar de novo)
- Se nao → descartar (com confirmacao explicita)

### Quando NAO perguntar

- Sessao trivial: <5 interacoes, pergunta unica, resposta curta
- Sessao puramente tecnica sem decisoes (ex: "rode esse comando", "qual a sintaxe de X")
- Sessao pessoal detectada (auto-salvamento ja cobre)

## Fallback de Crash

Se `.session-stream.md` existir sem `# FLUSHED` no startup (crash detectado):
- A transcricao pode ser gerada do conteudo residual do buffer
- Na recuperacao, perguntar se deseja salvar a transcricao parcial da sessao anterior

## Fonte de Dados

A transcricao e consolidada a partir do `.session-stream.md` (preservado pelo FLUSH, PROTOCOL.md §3.7) + tool calls capturados + dialogo verbatim. Nao re-varrer tudo — derivar do que ja foi capturado.