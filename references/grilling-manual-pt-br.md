# MANUAL DO GRILLING (grill-me / grilling) — PT-BR

> Autor: Matt Pocock (mattpocock/skills) · Licença: MIT · Adaptado para opencode/KAI
> Última atualização: 2026-10-13

## 1. Objetivo

As skills `grill-me` e `grilling` servem para **apertar/afinar um plano, ideia ou decisão** antes de codificar. Ao invés de pular direto para implementação, o agente faz perguntas em rodadas até eliminar ambiguidades e chegar a um entendimento compartilhado.

- `grill-me`: wrapper de invocação (recomendado dizer "grill essa ideia").
- `grilling`: primitiva (árvore de decisão, *rounds*, *frontier*).

## 2. Quando usar

Use quando:
- Existe uma ideia vaga ("quero criar X", "vou refatorar Y") sem detalhes.
- Há decisão importante com trade-offs.
- Você quer validar escopo antes de gastar tokens/tempo.
- Há ambiguidade entre alternativas.
- Precisa alinhar objetivos/usuários/limites.

Não use para:
- Tarefas triviais (1 arquivo, poucas linhas).
- Quando já existe um spec/PRD claro e aprovado.

## 3. Conceitos-chave

| Conceito | Explicação |
|---|---|
| **Design Tree** | Árvore de decisões: cada decisão se ramifica em outras que dependem dela. |
| **Rounds** | Rodadas. Em cada rodada, o agente pergunta **toda a fronteira** de uma vez. |
| **Frontier** | Conjunto de perguntas cujos **pré-requisitos já foram resolvidos**. Perguntas que dependem de outra ainda aberta ficam para rodada futura. |
| **Resposta recomendada** | Para cada pergunta, o agente sugere uma resposta (*➡️ ...*). Formular a pergunta de modo que "**sim**" aceite a recomendação é intencional. |
| **Facts vs Decisions** | **Facts**: o agente deve descobrir sozinho (filesystem, grep/glob, leitura, sub-agente). **Decisions**: vão ao usuário — nunca inventar decisão. |

## 4. Como invocar (no opencode)

Com skill normal instalada em `~/.config/opencode/skills/`, basta dizer:

```text
grill essa ideia: quero fazer um CLI para extrair métricas de build
```

Ou mais direto:
```text
use a skill grilling e aperte essa ideia
```

O `grill-me` dispara o `grilling` automaticamente (wrapper).

## 5. Formato de cada rodada

O agente responderá nesse formato:

```text
❓ **Q1** - **<título da pergunta>**: <corpo com contexto/opções>

➡️ <resposta recomendada pelo agente>

---

❓ **Q2** - **<título da pergunta>**: ...

➡️ <resposta recomendada>
```

## 6. Fluxo passo-a-passo

1. **Mapeamento inicial** – agente constroi árvore mínima com perguntas abertas.
2. **Rodada 1 (frontier inicial)** – apresenta perguntas cujas dependências estão satisfeitas.
3. **Você responde** – pode dizer "sim" (aceitar recomendação), "não" com justificativa, ou responder livremente.
4. **Recomputação** – agente atualiza árvore, expande fronteira com perguntas desbloqueadas.
5. **Nova rodada** – repete até **frontier vazia**.
6. **Fechamento** – agente confirma entendimento compartilhado. **Não executa código antes disso**.

## 7. Regras práticas

- **Nunca adivinhar fato.** Se precisar checar arquivo/código, usa ferramenta (sub-agente) — não pergunta ao usuário.
- **Perguntar decisões, não fatos.** "Qual deve ser o nome do comando?" → decisão (vai ao user). "Existe package.json?" → agente verifica.
- **Resposta recomendada intencional.** Se a sua intenção bate com a recomendação, basta responder `sim`.
- **Uma rodada por vez.** Responda todas as perguntas daquela rodada ou seja explícito sobre o que falta.
- **Sem ação prematura.** Só parte para implementação após confirmação explícita de entendimento compartilhado.

## 8. Exemplos rápidos

**Exemplo A – vaga**
> "grill essa ideia: app para lembrar leituras"

Rodada 1 provavelmente cobre: propósito, público-alvo, MVP vs completo, plataforma (web/CLI/app), dados locais/remotos.

**Exemplo B – refatoração**
> "grill essa ideia: quero extrair módulo X sem quebrar API pública"

Cobre: quais contratos devem permanecer estáveis, testes existentes, riscos, escopo estrito.

## 9. Diferença vs brainstorming

| Aspeto | `brainstorming` (existente) | `grilling` (novo) |
|---|---|---|
| Foco | Socrático geral + gate antes de codar | **Árvore + rounds + frontier** (mecânica sistemática) |
| Saída | 3 perguntas mínimas + clarificação | Múltiplas perguntas organizadas por dependências, com recomendação por item |
| Fatos | Pode perguntar, mas menos enfático em "descubra sozinho" | Fortemente "facts = seu trabalho; decisions = usuário" |
| Iteração | Geralmente 1–2 interações | Iterativo por rodadas até frontier vazia |

## 10. Dicas para respostas

- Responda curto: `sim`, `não — prefiro CLI`, `Q1 sim, Q2 não por motivo X`.
- Se mudar de ideia entre rodadas, diga claramente.
- Se já tem resposta pronta, cole-a diretamente.
- Não precisa reescrever a pergunta — responda pelo número (`Q1: sim`).

## 11. Notas operacionais (opencode)

- Instalado em `~/.config/opencode/skills/grill-me/` e `~/.config/opencode/skills/grilling/`
- `grill-me` tem `description` enxuta; `grilling` tem instruções completas.
- Frontmatter adaptado ao formato do opencode (removido `disable-model-invocation`).
- Invocação natural por linguagem humana (você diz "grill...").

## 12. Referências

- [mattpocock/skills – grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
- [mattpocock/skills – grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)
- Arquivo local: `~/.config/opencode/skills/grilling/SKILL.md`