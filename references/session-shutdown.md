# Session Shutdown

Ao final de cada sessao (detectado por despedida ou comando explicito):

1. **Gerar transcricao da sessao** direto em <skill-dir>\CHATS\
2. **FLUSH final**: seguir PROTOCOL.md §3.7 (FLUSH atomico)
3. **Deletar** .session-stream.md (sinaliza termino limpo)
4. **Atualizar** AVALIACAO_SPA.md do projeto atual
5. **Atualizar** AVALIACAO_GLOBAL_SPA.md (~/.config/opencode/)
6. **Atualizar** CHANGES.md se houve modificacoes no sistema
7. **Oferecer commit** se houver mudancas staged
8. **Apresentar** SkillWatch Resumo da Sessao
