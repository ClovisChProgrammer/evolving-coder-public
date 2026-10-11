# privacidade-classificacao.md — Classificação de Projeto & Privacidade por Padrão

> Protocolo sob demanda. Fonte autoritativa da regra: `instructions/global-rules.md` REGRA #7.
> Objetivo: nenhum dado sensível de cliente/regulado sai para um modelo que treina com dados — **por padrão**, sem perguntar, salvo classificação explícita como público.

---

## 1. Princípio

**Privado por padrão.** Um projeto sem classificação é tratado como `confidencial`. Só é tratado como aberto se houver **opt-out explícito** (marcador dizendo `público`).

Razão: o custo de erro é assimétrico. Mandar dado de cliente para modelo que treina = vazamento irreversível; rodar um projeto aberto no modo privado = apenas perda de qualidade/velocidade, reversível.

---

## 2. Taxonomia (3 classes)

| Classe | Definição | Rota de modelo |
|--------|-----------|----------------|
| `confidencial` | Dados de cliente, caso jurídico, dado regulado (LGPD/PII), segredos, contratos, saúde, financeiro pessoal de terceiros | **Zero-retention obrigatório**: agente `privado` (Space Bunny; LongCat no fallback) |
| `interno` | Projeto próprio sem PII de terceiros, mas não destinado a publicação | Zero-retention preferível: `privado` (SB/LC) |
| `público` | Código/docs abertos, conteúdo já público, tarefas sem dado sensível | Livre (default global: `mimo-v2.6-flash-free`; ou `big-pickle`) |

Classe **ausente** → assume `confidencial`.

---

## 3. Marcador (dispensa a pergunta)

Ordem de precedência (primeiro que existir vence):

1. **Campo no `Andamentos KAI.md`** do projeto (formato já existente no fluxo):
   ```
   Classificação: confidencial   # ou: interno | público
   ```
2. **Arquivo marcador `.cliente` ou `.privado`** na raiz do projeto → força `confidencial`.
3. **Arquivo marcador `.publico`** na raiz → força `público` (opt-out explícito).
4. Nada encontrado → **`confidencial`** (default-safe).

Não perguntar ao usuário. Ler o marcador no startup e agir.

---

## 4. Portão no início da sessão (comportamento obrigatório)

No startup, depois de identificar o diretório de trabalho:

1. Ler o marcador (§3) → determinar a classe.
2. Se classe ∈ {`confidencial`, `interno`} **e** o agente/modelo atual **não** é zero-retention (ex.: default `mimo`, `big-pickle`, `muse-spark`, `nemotron`, `ling`):
   - **PARAR** antes de processar conteúdo sensível.
   - Avisar e instruir: *"Este projeto está classificado como `{classe}`. O modelo atual (`{modelo}`) treina com dados. Troque para o agente `privado` (Tab / `@privado`) antes de prosseguir."*
   - **Não** é possível trocar o modelo no meio de uma sessão → a troca tem de acontecer no início.
3. Se o agente atual já é `privado` (zero-retention) → prosseguir normalmente.

Exceção: tarefas comprovadamente sem dado sensível (ex.: editar um README genérico) podem seguir, mas **avisar** que o projeto é classificado privado e o modelo não é zero-retention.

---

## 5. Guarda mid-session (telemetria de risco)

Mesmo dentro de um projeto `público`/`interno`, se o conteúdo do turno casar padrões sensíveis, **parar e avisar** (não seguir em silêncio; não trocar modelo sozinho):

- CPF `\d{3}\.\d{3}\.\d{3}-\d{2}` · CNPJ `\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}`
- Cartão `\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}`
- E-mail pessoal, telefone, endereço
- `senha|password|token|secret|api[_-]?key|bearer` seguido de valor
- Conteúdo de `.env`, chaves privadas (`-----BEGIN ... PRIVATE KEY-----`)
- Paths sob pasta de cliente / caso

Ação: `⚠️ Este turno contém dado {tipo} e o modelo atual (`{modelo}`) treina com dados. Recomendo migrar a sessão para o agente `privado`.` — e aguardar decisão.

---

## 6. Mapa classe → modelo (free-first, decidido por Clóvis)

- **`privado` (agente)**: `opencode/space-bunny-free` (SB) — 524K output, mais estável, generalista.
  - Fallback nativo: `opencode/longcat-2.5-preview-free` (LC) — mesma classe zero-retention, via `model-fallback.js`.
- **Conversa/plan pessoal privado**: LC (preferência de Clóvis — reflexivo, estável em pt-BR).
- **Código privado**: SB.
- **`público`**: default global `mimo-v2.6-flash-free`; `big-pickle` quando precisar de outro sotaque.

Matriz de privacidade no `plugins/model-fallback.js`: `space-bunny-free` e `longcat-2.5-preview-free` = `zeroretention` (rank 2). O seletor de sucessor só cai para tier ≥ o modelo falho → um modelo zero-retention nunca rebaixa para `training`/`trial`.

---

## 7. Limite honesto (não esconder)

- **SB/LC não é garantia.** Space Bunny tem provider oculto e "pode ser trocado em silêncio"; LongCat é **preview**. São **mitigação**, não blindagem.
- Para dado **regulado real** (sigilo profissional, dado sensível de saúde/financeiro de terceiros), a rota correta é **modelo local** (Ollama) ou **provider pago com zero-retention contratual** — decisão de Clóvis.
- **Nunca migrar sozinho** para local/pago. Sempre avisar; nunca decidir.
- SB/LC **não têm benchmark de código** → qualidade de coding privado é [INCERTO].

---

## 8. Limitação conhecida do fallback

`model-fallback.js` aprende o modelo primário via `message.updated` (só após a 1ª resposta). Se a **1ª mensagem** de uma sessão `privado` falhar antes de qualquer resposta, o plugin usa `DEFAULT_MODEL` (`mimo`, training) como referência de falha → poderia escolher um sucessor que treina. **Mitigação:** usar o agente `privado` com modelo já zero-retention e evitar 1º turno pesado. **A corrigir:** capturar o modelo/agente no `session.*` de abertura. [A INVESTIGAR no SDK]

---

## 9. Artefatos relacionados

- Regra autoritativa: `instructions/global-rules.md` REGRA #7
- Agente: `~/.config/opencode/agents/privado.md`
- Fallback: `plugins/model-fallback.js` (matriz de privacidade)
- Aprendizado: `.learnings/LRN-20261011-001-*`
