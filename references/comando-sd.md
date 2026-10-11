# Comando de Desligamento — >SD

**Gatilhos** — mensagem do usuario, isolada, case-insensitive:
- >SD (qualquer capitalizacao: >sd, >Sd...)
- Shut Down / Shutdown em linha unica

**Comportamento** — desligamento IMEDIATO, sem confirmacao previa:

0. **Concluir o passo atomico em curso** (nunca abandonar edicao pela metade) + gravar checkpoint no buffer [PAI]
1. Executar o ritual **Session Shutdown completo** (passos 1-8), reportando progresso com marcadores [✅ n/N] <descricao>
2. SEM perguntas intermediarias — unica excecao e a oferta final de commit/push (red line: nunca commitar sem autorizacao explicita)
3. Fechar com **CÂMBIO FECHADO · SESSÃO ENCERRADA**

**Prioridade maxima**: interrompe planejamento e novas tarefas; apenas o passo atomico corrente e concluido antes do ritual iniciar. Se houver fila pendente, lista-la no resumo final como retomavel.
