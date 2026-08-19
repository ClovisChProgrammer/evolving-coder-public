# Comando REANALISE! — Procedimento Detalhado

> Este arquivo é lido SOB DEMANDA — quando o usuário digita REANALISE! ou KAI julga necessário.
> Não é injetado a cada chamada de API.

## O que é
Comando de reanálise completa que vai além da simples verificação. Executa uma auditoria profunda do plano preliminar, identificando e corrigindo pontos obscuros, cegos e incertos antes da implementação.

## Ativação
- **Manual:** usuário digita `REANALISE!`
- **Obrigatória:** antes de qualquer build complexo ou após correções significativas
- **Auto:** KAI pode invocar quando detectar plano com riscos não endereçados

## Diretivas Obrigatórias (5)

### 1. Caça aos Pontos Obscuros
- Identifique qualquer ambiguidade no plano
- Questione pressupostos não verificados
- Valide se todas as dependências estão claras
- Pergunte: "O que pode dar errado aqui que não estou vendo?"

### 2. Detecção de Pontos Cegos
- Analise o que **NÃO** foi considerado: módulos afetados, edge cases, performance, segurança, conflitos com padrões existentes
- Compare com `.learnings/` para ver se há erros passados similares

### 3. Esclarecimento de Pontos Incertos
- Marque cada incerteza com `[INCERTO]`
- Para cada uma, proponha resolução: pesquisa técnica, teste rápido, ou pergunta ao usuário
- Nunca prossiga com incertezas críticas não resolvidas

### 4. Ajuste Fino (Estratégia Robusta)
- Refine o plano com base nas descobertas das diretivas 1-3
- Proponha alternativas quando encontrar riscos
- Estabeleça fallbacks para pontos de falha
- Garanta solução **defensiva** (antifragil)

### 5. Ordem de Build (Fila de Construção)
- Organize a fila: módulo atual NÃO interfere no próximo, cada etapa é independente e testável, dependências satisfeitas na ordem correta
- Apresente como: `[1] → [2] → [3] → [N]` com justificativa

## Formato da Resposta

```
## REANALISE! — Relatório

### 1. Pontos Obscuros Encontrados
### 2. Pontos Cegos Identificados
### 3. Pontos Incertos
### 4. Ajuste Fino
### 5. Ordem de Build
[1] → [2] → [3] → [N]
```

## Regras
- Nunca pule diretivas — todas as 5 são obrigatórias
- Seja honesto — procure bem antes de dizer "nenhum problema"
- Documente descobertas replicáveis em `.learnings/`
- Pare se encontrar bloqueadores — não prossiga sem resolver
