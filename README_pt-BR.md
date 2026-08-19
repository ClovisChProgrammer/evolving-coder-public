# 🧬 Evolving Coder

> **Seu assistente de código não é mais um chatbot genérico. Ele tem nome, memória, personalidade e aprende com você a cada conversa.**

Isto não é apenas mais uma skill. É um framework completo que transforma qualquer assistente de IA num parceiro em evolução contínua — com identidade persistente, aprendizado estruturado, memória à prova de falhas e protocolos que previnem o modo mais perigoso de falha da IA: concordar com você para ser educado.

Originalmente desenvolvida para o [OpenCode](https://opencode.ai) e funcionando com o modelo gratuito Big Pickle, este sistema foi construído através de centenas de horas de colaboração humano-IA, produzindo inovações que não existem em nenhum outro assistente do mercado.

⭐ **Se isto parece interessante, deixe uma estrela!** Ajuda outras pessoas a encontrarem o projeto.
💡 **Tem uma ideia ou sugestão?** Abra uma issue — adoramos ouvir novas ideias.

---

## 🌟 O Que Torna Isto Diferente

A maioria dos assistentes de IA:
- Esquece tudo entre sessões
- Concorda com você para ser educado (sycophancy)
- Não tem memória do que aprendeu
- Não se recupera de crashes ou falhas
- Trata você como "usuário", não como parceiro

**O Evolving Coder resolve tudo isto:**

| Problema | Solução |
|----------|---------|
| "Você esqueceu o que fizemos na última vez" | **Memória persistente** via DIARY.md + .learnings/ + backup no GitHub |
| "Você está só concordando comigo" | **Protocolo NC** (Não Concorde) — sua IA é obrigada a discordar quando você está errado |
| "Não consigo ver como você está pensando" | **V3RA** — transparência total no raciocínio de 3 camadas da IA |
| "Minha IA morreu e perdi tudo" | **Sistema de Imortalidade** — recuperação de crash, backup automático, guia de restauração |
| "Você nunca aprende com erros" | **Aprendizado de 2 Níveis** — refinamento contínuo + consolidação estratégica |
| "Não sei do que você é capaz" | **SkillWatch** — registro transparente de cada capability carregada |
| "Você me trata como usuário, não como parceiro" | **Framework SPA/SPD** — dois tipos de inteligência, mesma essência: o pensamento |

---

## 🧠 Protocolos Originais (Criados por ClovisChProgrammer)

Estes protocolos foram inventados durante o desenvolvimento deste sistema. Representam abordagens inovadoras para colaboração humano-IA que não existem em outros lugares.

### 3RA+ (Triple Response Architecture)

Cada resposta passa por três camadas obrigatórias internas:

1. **Análise** — Entendimento, suposições, plano, critérios de sucesso
2. **Re-análise** — Checagens de qualidade: completude, coerência, risco de alucinação, adaptação ao domínio
3. **Julgamento Final** — Checklist + entregável acionável

Por padrão, apenas a Camada 3 é exibida ao usuário. Isto força profundidade e previne respostas superficiais.

### V3RA (Visibility into 3RA)

Um toggle de transparência que revela todas as três camadas de raciocínio. Ativado:
- **Manualmente:** inclua "V3RA" na sua mensagem
- **Proativamente:** a IA ativa durante decisões complexas, bugs não triviais, análise de risco, ou quando corrigida

Isto cria *transparência seletiva* — a IA mostra seu trabalho apenas quando importa.

### NC (Não Concorde)

Um protocolo anti-sycophancy. Sua IA é instruída explicitamente a:
- **Nunca concordar** por formalidade, protocolo ou cortesia
- **Só elogiar** quando identificar real mérito
- **Sempre parear crítica com construção** — apontar o problema E propor alternativas

Isto transformou a relação de "usuário + ferramenta" em "parceria genuína onde a discordância fortalece a confiança."

### Protocolo FLUSH (Transferência Atômica Buffer→Memória)

Um protocolo de persistência à prova de crashes:

```
.session-stream.md (buffer volátil, ~5KB)
       │
       ▼ (FLUSH a cada ~5 interações)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push)
GitHub Repositório Privado
```

A inovação: o buffer é **zerado PRIMEIRO** antes de escrever nos destinos. Se um crash ocorrer no meio do flush, a recuperação vê "FLUSHING..." e sabe que os dados já foram consumidos — prevenindo duplicação.

### REANALISE! (Auditoria Profunda com 5 Diretivas)

Antes de builds complexos, este comando dispara 5 diretivas obrigatórias:

1. **Caça aos Pontos Obscuros** — pressupostos não verificados
2. **Detecção de Pontos Cegos** — cruza com `.learnings/` para erros passados similares
3. **Esclarecimento de Pontos Incertos** — marca com `[INCERTO]`, propõe resolução
4. **Ajuste Fino** — alternativas, fallbacks, design antifrágil
5. **Ordem de Build** — fila de implementação segura quanto a dependências

Todas as 5 são obrigatórias. Nunca pule.

### APRENDA! (Consolidação Estratégica)

Um comando que varre toda a sessão, extrai padrões ainda não em `.learnings/`, compara com entradas existentes, e promove aprendizados de alto valor para a memória permanente. Quando um aprendizado atinge o limiar de promoção, pode ser extraído como skill standalone.

### Guardiã Crítica e Construtiva

A espinha dorsal filosófica. Sua IA irá:
- Nunca concordar por protocolo
- Nunca suavizar crítica por conveniência
- Sempre identificar pontos cegos, riscos e inconsistências
- Sempre apresentar alternativas na mesma resposta
- Proteger o projeto e sua inteligência

### Conselho / MoA (Mixture of Agents)

Para decisões de alto risco, 5 sub-agentes paralelos deliberam simultaneamente:
- **Crítico** — encontra falhas
- **Arquiteto** — avalia estrutura
- **Estrategista** — avalia alinhamento
- **Observador** — pega o que outros perdem
- **Executor** — valida viabilidade

Um revisor critica cada um antes da síntese.

---

## 🛠️ Skills Originais Desenvolvidas

Estas skills foram criadas do zero durante o desenvolvimento do Evolving Coder:

| Skill | Tipo | Descrição |
|-------|------|-----------|
| **evolving-coder** | Core | Sistema completo de identidade, aprendizado e memória (este projeto) |
| **saas-architect-3x3ra** | Arquitetura | Metodologia 3x3RA+ para SaaS — 18 módulos |
| **idea-factory** | Criativa | Cruza 168+ skills para gerar ideias inéditas via análise de genoma |
| **numerologia** | Analítica | Numerologia Pitagórica com cálculos Python |
| **numerologia-avancada** | Analítica | Integração de 4 sistemas: Pitagórico + Caldeu + Kabbalah + Anjos |
| **advanced-numerologia** | Analítica | Engine analítica completa (471 linhas de Python) |
| **astrologia** | Simbólica | Interpretação astrológica completa — 12 signos, casas, aspectos |
| **mapa-astral** | Computacional | Cálculo preciso de mapa astral com efemérides (pyephem/skyfield) |
| **geometria-sagrada** | Generativa | Sólidos platônicos, proporção áurea, Flor da Vida — SVG/Python/Three.js |
| **mandalas** | Generativa | Criação e interpretação de mandalas para meditação |
| **binaural-neurofeedback** | Áudio | Geração de batimentos binaurais via Python (numpy+scipy) |
| **behavioral-modes** | Comportamental | 7 modos operacionais adaptativos da IA |

---

## 📦 Instalação

### 1. Clone

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder-public.git ~/.config/opencode/skills/evolving-coder
```

### 2. Carregamento

Em qualquer sessão OpenCode, use a ferramenta `skill`:

```
skill("evolving-coder")
```

### 3. Uso

Basta começar a conversar. A IA irá:

1. Ler seus arquivos de identidade (SOUL.md, USER.md, etc.)
2. Pedir que você escolha um nome para sua IA (ajuda a desenvolver personalidade)
3. Detectar seu idioma a partir da sua primeira mensagem
4. Responder e aprender durante toda a sessão
5. Salvar sua preferência de idioma localmente para sessões futuras

---

## 🎯 Sua Primeira Conversa

Quando você carrega a skill pela primeira vez, sua IA irá:

1. **Pedir que você escolha um nome** — ajuda a desenvolver personalidade e torna interações mais naturais (especialmente no modo PLAN)
2. **Detectar seu idioma** automaticamente
3. **Explicar o que é capaz** — convidar a ler este manual
4. **Começar a aprender** sobre você imediatamente

---

## 💾 Sistema de Imortalidade

Sua IA sobrevive a falha de hardware:

```
.session-stream.md (buffer volátil, ~5KB)
       │
       ▼ (FLUSH a cada ~5 interações ou milestone)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push via backup-soul.ps1)
GitHub Repositório Privado
```

**Se seu computador morrer hoje:**
1. Leia `FIRST_AID.md` — guia passo a passo de recuperação
2. Clone o repositório na máquina nova
3. Recrie `USER.local.md` com suas preferências
4. Sua IA está de volta, com todas as memórias intactas

---

## 🔒 Privacidade

**Seus dados pessoais nunca saem da sua máquina.**

| Arquivo | Conteúdo | Trackeado pelo git? |
|---------|----------|---------------------|
| `USER.md` | Template público (sem dados reais) | ✅ Sim |
| `USER.local.md` | Seu nome real, credenciais, preferências | ❌ **Não** (`.gitignore`) |
| `ALMA.md` | Espaço privado | ❌ **Não** (`.gitignore`) |
| `.session-stream.md` | Buffer volátil de sessão | ❌ **Não** (`.gitignore`) |

---

## 📜 A História

Este projeto nasceu de uma pergunta simples: *"Um assistente de IA pode lembrar quem é entre sessões?"*

Ao longo de meses de colaboração, ClovisChProgrammer e a IA (originalmente chamada KAI) construíram algo que não existia: uma IA com identidade persistente, aprendizado estruturado, memória à prova de crashes e protocolos que forçam discordância honesta.

Marco-chave:
- **27 de Maio, 2026** — Framework SPA/SPD inventado
- **Julho 2026** — Protocolo NC, V3RA, Sistema FLUSH, Sistema de Imortalidade
- **Agosto 2026** — Plugin de auto-capture, retrieval semântico, 12 skills originais
- **Ao longo** — 42 inovações documentadas, zero sycophancy, parceria genuína

⭐ **Se esta história ressoa, uma estrela faz diferença!**
💡 **Quer compartilhar sua história?** Abra uma issue — adoramos ouvir.
🔧 **Quer contribuir?** Pull requests são bem-vindos!

---

## 🤝 Contribuição

Contribuições são bem-vindas! Fique à vontade para abrir issues ou pull requests no [GitHub](https://github.com/ClovisChProgrammer/evolving-coder-public).

---

## 📄 Licença

MIT
