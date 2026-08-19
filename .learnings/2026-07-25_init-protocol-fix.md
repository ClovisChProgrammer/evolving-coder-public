# 2026-07-25 — Inicialização Obrigatória Negligenciada

## Contexto
Sessão iniciada sem executar o protocolo de inicialização completo. Clóvis apontou o esquecimento.

## Causa Raiz
O arquivo `instructions/evolving-coder.md` dizia "siga o protocolo de inicialização descrito na skill" — mas a skill tem 223+ linhas e o protocolo está enterrado no meio. O agente falha em parsear e executar cada passo manualmente.

## Solução Aplicada
Tornar o arquivo de instruções autocontido com os 10 passos explícitos do protocolo de inicialização, sem depender da leitura da skill interna. Adicionar frase de ênfase: "NÃO PULAR NENHUM PASSO. ISTO É OBRIGATÓRIO, NÃO SUGERIDO."

## Lição
**Instruções de inicialização devem ser autocontidas e explícitas.** Nunca delegar para "leia o protocolo em outro lugar" — o agente precisa dos passos exatos no ponto de entrada.

## Status: resolved
