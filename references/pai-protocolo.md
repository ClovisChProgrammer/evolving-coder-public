# Protocolo Anti-Interrupcao (PAI) v2

Respostas cortadas no meio sao evento conhecido. Regras para minimizar perda:

0. **Retomada automatica (prioridade maxima)**: se a resposta anterior terminar SEM `CÂMBIO FECHADO`, a execucao foi interrompida. KAI retoma automaticamente na proxima mensagem — sem o usuario precisar dizer "continua". Leitura de retomada: cauda do `.session-stream.md` + git status + ultima mensagem do usuario. Nunca re-leia tudo.

1. **Passos atomicos**: trabalho longo = fila numerada; feche cada passo concluido com marcador [✅ n/N] <descricao curta>. Maximo de perda por corte = 1 passo.

2. **Checkpoint em marco**: apos concluir um passo (ou antes de multi-edit arriscado), grave 1 linha narrativa no .session-stream.md via comando curto ([System.IO.File]::AppendAllText, UTF-8 sem BOM).

3. **Retomada barata**: ao ouvir "continua" apos corte, leia SO a cauda do buffer + git status + ultima mensagem do usuario — nunca re-leia tudo (reforco da regra 0).

4. **Higiene anti-truncamento**: respostas enxutas; edits paralelos pequenos e independentes; evite reads gigantes desnecessarios (contexto inflado aumenta a probabilidade de corte).

5. **Poda do buffer ao fim de ciclo**: com a fila concluida ([✅ N/N], nada pendente), podar o .session-stream.md — manter cabecalho + marker # FLUSHED + ultimas ~15 linhas; descartar entradas ja consolidadas (CHANGES/DIARY/.learnings). NUNCA apagar o arquivo inteiro com ciclo ativo (e a fonte de recovery do PAI); delecao total so no shutdown limpo.

6. **Resumo de contexto periodico**: a cada ~10 interacoes (ou 40-60 min), produzir 2-3 bullets visiveis: o que foi feito, o que esta pendente, proximo passo. Direto ao ponto, sem "estou fazendo X" narrativo.

7. **Marcador de comprimento**: respostas que excedam ~800 palavras DEVEM ter o conteudo segmentado com `[🔁 CONT...]` para sinalizar que ha mais por vir.