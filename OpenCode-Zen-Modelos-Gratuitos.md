# OpenCode Zen — Modelos GRATUITOS (Free)

> **Data da pesquisa:** 10/10/2026
> **Fonte:** docs oficiais do OpenCode Zen, model card da Xiaomi, tabelas de eval DeepInfra, BenchLM, LLM Stats, OpenCode Data.
> **Aviso importante (vale para todos):** durante o período gratuito, **seus dados podem ser usados para treinar o modelo** (exceto Space Bunny e LongCat — zero-retention). Nunca envie código confidencial, de cliente ou dados privados por modelos free. Para trabalho privado, use modelos pagos.

---

## 1. MiMo-V2.6-Flash Free — o que é

**Modelo:** Xiaomi MiMo-V2.6-Flash (open-weight, licença MIT), lançado em 21/09/2026.

| Spec | Valor |
|---|---|
| Arquitetura | MoE esparso — 309B parâmetros totais, **15B ativos por token** |
| Contexto | **1M tokens** (≈ 1.6 mil páginas de texto) |
| Saída máxima | **128K tokens** por resposta |
| Entrada | texto, **imagem, vídeo, áudio** (multimodal nativo) |
| Saída | **somente texto** |
| Capacidades | reasoning (pensa antes de responder), tool calling, structured output (JSON), streaming, web search, context caching |
| ID no OpenCode | `opencode/mimo-v2.6-flash-free` (endpoint `https://opencode.ai/zen/v1/chat/completions`) |

**Condição do "Free":** gratuito por tempo limitado. A Xiaomi/OpenCode usam o período para coletar feedback e melhorar o modelo — **os dados enviados podem ser usados para treino**.

**Treino:** modelo treinado com RL massivo (~US$ 378K), com ~2/3 das tarefas sendo de código. Supera de forma abrangente o MiMo-V2.5-Pro (geração anterior).

### 1.1 Profundidade por domínio

#### 💻 Programação e agentes — NÍVEL: EXCELENTE (o eixo mais forte)
É aqui que o modelo brilha. Ele foi treinado especificamente para isso:

- **DeepSWE v1.1: 67.9** — benchmark de engenharia de software de longo prazo. Para referência: Claude Opus 5 = 74, GPT-5.6 Sol = 73. Ou seja: **perto do topo do mercado, de graça**.
- **Terminal Bench 2.1: 87.6%** — trabalhar sozinho no terminal (rodar comandos, depurar, navegar repositórios).
- **OSWorld: 80.8%** — operar o computador (GUI: cliques, janelas, apps).
- **MiMo VisualCoding: 71.5** — codar interfaces visuais (frontend, design no código).
- Pode manter sessões de agente longas (contexto de 1M aguenta repositórios inteiros + histórico de ferramentas).

**Uso ideal:** features, refactors, debugging, agentes autônomos, manipulação de codebase inteiro.

#### 🧮 Cálculos e matemática — NÍVEL: BOM (mas sem prova oficial)
- É um modelo de **reasoning** (raciocínio encadeado): índice de raciocínio 73.4 no BenchLM, rank **#28 geral** de 637 modelos.
- **Porém:** a Xiaomi **não publicou resultados em AIME/GPQA** (os benchmarks de matemática padrão). Não dá para afirmar nível de olimpíada — [INCERTO].
- Para **matemática pura**, existe alternativa free melhor: **Ling 3.0 Flash Fin Free** (AIME26: 93.2%, GPQA: 85%, HMMT: 87%).

**Uso ideal:** cálculo aplicado, lógica, análise de dados, formalização matemática dentro de código. Para prova de matemática difícil, preferir Ling Fin.

#### 🎨 Desenho e pintura — NÍVEL: NÃO GERA IMAGEM
- **A saída dele é somente texto. Ele não pinta, não desenha, não gera imagem.** Ponto.
- O que ele **faz**: *entende* imagens de entrada (analisar, criticar, comparar, extrair informação) e **escreve código que produz arte**: SVG, shaders GLSL, p5.js, CSS art, canvas HTML.
- Índice MiMo VisualCoding 71.5 = bom em transformar descrição visual em código.

**Uso ideal:** gerar arte por código, analisar/descrever imagens, escrever prompts para geradores de imagem. Para gerar imagem de fato → modelo dedicado (Nano Banana/Gemini Image, Stable Diffusion etc.).

#### ✍️ Roteiros e texto — NÍVEL: BOM
- 128K de saída por resposta + 1M de contexto = aguenta roteiro longo, documentação técnica, narrativa, artigos, scripts de vídeo/podcast.
- Multimodal na entrada: dá para mandar um vídeo/imagem como referência e pedir o roteiro em cima dela.
- Não há benchmark de "creative writing" publicado — a qualidade estética fina é [INCERTO], mas o texto técnico/narrativo é competente.

**Uso ideal:** roteiros, documentação, specs, copy, resumos de material longo (incluindo PDF/vídeo como entrada).

#### 🎬 Vídeo — NÍVEL: NÃO GERA (só analisa)
- **Não gera vídeo nem áudio.** Saída é texto.
- O que ele **faz**: *entende* vídeo de entrada (narrativa, cortes, erros, storyboards, transcrição visual) e escreve: roteiro, storyboard, **prompt** pronto para geradores externos (Veo, Kling, MiniMax Video), ou código de animação (CSS/JS/canvas).

**Uso ideal:** análise de vídeo, storyboard, prompt-engineering para geradores, scripts de animação.

#### 🖥️ Agente / operar o computador (CUA) — NÍVEL: MUITO BOM
- Integra percepção multimodal + ação: vê a tela e clica.
- OSWorld 80.8%, JobBench 61.2%, Toolathlon 73.6%, CyberGym 95.1% (segurança).
- **Uso ideal:** automação de tarefas no PC, agentes que usam ferramentas, web scraping interativo.

---

## 2. Comparativo — TODOS os models FREE do OpenCode Zen

**Lista oficial dos free em 10/10/2026** (docs.opencode.ai/docs/zen): Big Pickle, Space Bunny Free, LongCat 2.5 Preview Free, MiMo-V2.6-Flash Free, MiMo-V2.5 Free, Ling 3.0 Flash Fin Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Muse Spark 1.3 Contributor Free, Jev 1.13 Free.

| # | Modelo | Autor | Contexto / Saída | Entrada | Melhor para | Cuidado |
|---|---|---|---|---|---|---|
| 1 | **MiMo-V2.6-Flash Free** | Xiaomi | 1M / 128K | texto+imagem+vídeo+áudio | Coding/agente de alto nível; visão multimodal | Dados p/ treino; sem benchmarks de math |
| 2 | **Space Bunny Free** | stealth (oculto) | 1M / 524K | texto+imagem | Uso geral pesado; **privacidade** (zero-retention, sem treino) | Identidade oculta; pode ser trocado em silêncio |
| 3 | **Big Pickle** | stealth (provável GLM-4.6 da Zhipu) | 200K / 32K | texto | Daily-driver de código (classe Sonnet 4.5/4.6) | 32K de saída = mais apertado da frota; 200K só |
| 4 | **Muse Spark 1.3 Contributor Free** | Meta | 1M / 131K | texto+imagem+vídeo+pdf+áudio | Multimodal geral + reasoning forte (#3 em uso na rede) | "Contributor" = coleta de feedback |
| 5 | **Ling 3.0 Flash Fin Free** | InclusionAI | 262K / 32K | texto | **Matemática** (AIME26 93.2%) e finanças | Especializado em finanças; saída 32K |
| 6 | **MiMo-V2.5 Free** | Xiaomi | 200K / 32K | texto+imagem | Geração anterior, estável | Muito fraco vs. V2.6; 32K out |
| 7 | **Nemotron 3 Ultra Free** | NVIDIA | ~262K | **só texto** | Reasoning textual | **Endpoint trial: NÃO enviar dados privados** |
| 8 | **Nemotron 3.5 Lightning Free** | NVIDIA | 262K / 32K | **só texto** | Leveza/speed (30B A3B, open weights) | Sem visão; sem multimodal |
| 9 | **LongCat 2.5 Preview Free** | Meituan | 1M / 131K | texto+imagem | Contexto longo + privacidade (zero-retention) | Preview; uso ainda mínimo |
| 10 | **Jev 1.13 Free** | desconhecido | — | — | Incógnita (endpoint próprio `systemone`) | Dados escassos — [INCERTO] |

### 2.1 Explicação linha a linha

**1. MiMo-V2.6-Flash Free (Xiaomi)** — o mais completo em capacidade bruta: multimodal de verdade (entende vídeo e áudio), contexto de 1M, saída de 128K e qualidade de código quase-frontier. É a melhor escolha quando a tarefa é difícil E multimodal. Cuidado único: durante o free, dados podem ir para treino.

**2. Space Bunny Free (stealth)** — modelo misterioso (identidade não revelada), mas com duas vantagens únicas: **zero-retention** (seus dados NÃO são guardados nem usados para treino) e o maior contexto de saída da frota free (524K). É o mais usado da rede inteira (53T tokens processados). Ideal para código privado pequeno/médio e para quem se preocupa com privacidade. Risco: pode ser trocado por baixo do capô sem aviso.

**3. Big Pickle (stealth, provável GLM-4.6)** — consenso da comunidade de que é um GLM-4.6 da Zhipu, classe Claude Sonnet 4.5/4.6 em código. Excelente custo-benefício (zero) para o dia a dia de programação. Limitações reais: só 200K de contexto (não pega o repo inteiro) e 32K de saída (quebrar gerações grandes em pedaços).

**4. Muse Spark 1.3 Contributor Free (Meta)** — o outro gigante multimodal free: 1M de contexto, entrada de texto+imagem+vídeo+pdf+áudio, reasoning e tool calling. Nos rankings internos do OpenCode ele pontua reasoning/coding no topo. Alternativa direta ao MiMo com sabor mais "geral". O nome "Contributor" indica que é um tier de contribuidor — coleta feedback.

**5. Ling 3.0 Flash Fin Free (InclusionAI/Ant)** — especialista: matemática e finanças. Tem os números de math mais fortes de todos os free (AIME26 93.2%, HMMT 87%, GPQA 85%). Contexto modesto (262K) e saída de 32K. **Escolha certa para cálculo e prova difícil.**

**6. MiMo-V2.5 Free (Xiaomi)** — a geração anterior do item 1. Fica na lista como opção estável, mas perde em tudo para o V2.6 (contexto 200K vs 1M, saída 32K vs 128K, qualidade inferior). Use só se o V2.6 estar com problema.

**7. Nemotron 3 Ultra Free (NVIDIA)** — reasoning textual bom, mas **só texto** (sem imagem) e com um detalhe grave: o endpoint é de trial/trial-only — a NVIDIA pode inspecionar. **Não envie nada privado.** Serviço oficial grátis da NVIDIA durante avaliação.

**8. Nemotron 3.5 Lightning Free (NVIDIA)** — variante leve (30B A3B, pesos abertos): rápido, bom para tarefas simples e rápidas. Sem visão, sem multimodal, saída de 32K. O "cavalinho de carga leve".

**9. LongCat 2.5 Preview Free (Meituan)** — preview do modelo da empresa de delivery Meituan. Contexto de 1M + **zero-retention** (privacidade como o Space Bunny). Ainda é preview e quase ninguém usa (risco de instabilidade/qualidade irregular). Bom para testar contexto longo com privacidade.

**10. Jev 1.13 Free** — maior incógnita: endpoint próprio (`v1/systemone`), identidade não revelada, pouquíssimos dados públicos. Trate como experimental — [INCERTO] em tudo.

### 2.2 Resumo visual por tipo de uso

| Precisa de... | Free recomendado |
|---|---|
| Código difícil / agente autônomo | **MiMo-V2.6-Flash** ou **Big Pickle** |
| Matemática / cálculo puro | **Ling 3.0 Flash Fin** |
| Analisar imagem, vídeo, áudio | **Muse Spark 1.3** ou **MiMo-V2.6-Flash** |
| Privacidade (código sensível, sem treino) | **Space Bunny** ou **LongCat 2.5** |
| Texto rápido, tarefas leves | **Nemotron 3.5 Lightning** |
| Gerar imagem / vídeo | **nenhum free daqui** → usar gerador dedicado |

---

## 3. Citações rápidas (para colar no OpenCode)

```
opencode/mimo-v2.6-flash-free      # Xiaomi — coding/agente/multimodal
opencode/space-bunny-free          # stealth — privacidade + 1M ctx
opencode/big-pickle                # stealth — código do dia a dia
opencode/muse-spark-1.3-contributor-free  # Meta — multimodal geral
opencode/ling-3.0-flash-fin-free   # matemática e finanças
opencode/nemotron-3.5-lightning-free      # texto rápido
```

---

## Fontes

- Docs oficiais Zen: `https://opencode.ai/docs/zen` (lista free + pricing + avisos de privacidade)
- Model card Xiaomi: `https://mimo.mi.com/models/en-US/mimo-v2.6-flash`
- Release V2.6 + evals: `https://mimo.mi.com/docs/en-US/news/latest/v2-6` e tabela DeepInfra (`https://deepinfra.com/XiaomiMiMo/MiMo-V2.6-Flash`)
- BenchLM (`benchlm.ai`), LLM Stats (`llm-stats.com`), Artificial Analysis
- OpenCode Data (`opencode.ai/data`) — uso/trafego dos modelos
- pi.dev — metadata de Space Bunny e LongCat (contexto/saída/entrada)

*Pesquisa realizada por KAI em 10/10/2026. Verificar periodicamente — a lista free muda sem aviso.*
