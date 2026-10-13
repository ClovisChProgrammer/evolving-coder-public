# MANUAL DO TEACH — PT-BR

> Autor: Matt Pocock (mattpocock/skills) · Licença: MIT · Adaptado para opencode/KAI
> Última atualização: 2026-10-13

## 1. Objetivo

A skill `teach` ensina um tópico de forma **estruturada e stateful** ao longo de múltiplas sessões. Ao invés de resposta pontual, cria um **workspace de ensino** no diretório atual com lições HTML, registros de aprendizado, recursos e missão.

## 2. Quando usar

Use quando:
- Quer aprender algo do zero ou aprofundar (ex.: QA/Playwright, regex, bash, arquitetura).
- Precisa de trilha com exercícios e revisão.
- Quer manter memória entre sessões (o workspace persiste).
- Prefere aulas curtas com "win" tangível.

Não use para:
- Pergunta pontual/resposta única.
- Consulta rápida ("como faz X?") — melhor resposta direta.

## 3. Conceitos-chave

| Conceito | Explicação |
|---|---|
| **Stateful** | Estado vive no diretório onde você rodou `/teach` (ou invocou a skill). |
| **MISSION.md** | Razão real para aprender. Guia toda escolha de lição. |
| **Zona de Desenvolvimento Proximal (ZPD)** | "Desafiado só o suficiente" — nem fácil demais nem impossível. |
| **Lições (`./lessons/*.html`)** | Unidades auto-contidas, curtas, bonitinhas (estilo Tufte). Cada uma entrega 1 ganho. |
| **Registros (`./learning-records/*.md`)** | ADRs leves do aprendizado: insights não-obvios, correções, mudanças de rumo. |
| **Referências (`./reference/*.html`)** | "Cola" compacta: glossário, cheatsheet, algoritmos. |
| **Assets (`./assets/*`)** | Componentes reutilizáveis (CSS, quiz, simulador). Reuso é regra. |
| **RESOURCES.md** | Fontes confiáveis (artigos, docs oficiais, vídeos). |
| **NOTES.md** | Preferências/tom/ritmo anotados pelo agente. |

## 4. Como invocar

No diretório desejado (ex.: `C:\Users\clovi\learn\qa-playwright`):

```text
me ensina QA com Playwright do zero
```

Ou:
```text
use a skill teach: quero aprender bash para automação
```

## 5. Estrutura criada

```text
<cwd>/
├── MISSION.md
├── RESOURCES.md
├── NOTES.md
├── assets/           # CSS/quiz/simulador reutilizáveis
├── lessons/          # 0001-nome.html, 0002-nome.html,...
├── learning-records/ # 0001-insight.md,...
└── reference/        # cheatsheets/glossários HTML
```

Arquivos de formato vivem em `~/.config/opencode/skills/teach/*-FORMAT.md`.

## 6. Fluxo inicial

1. **Identifica missão** – se `MISSION.md` não existir, agente pergunta: por que quer aprender? objetivo prático? prazo? já sabe algo?
2. **Descobre ZPD** – lê learning-records existentes (se houver). Senão, começa do mínimo viável.
3. **Popula RESOURCES.md** – busca fontes confiáveis (oficiais > blogs genéricos).
4. **Cria 1ª lição** – curta, prática, ligada à missão. Abre arquivo HTML.
5. **Continua iterativo** – após concluir lição, atualiza learning-record, propõe próxima (desafio "só o suficiente").

## 7. Princípios pedagógicos

| Princípio | Aplicação |
|---|---|
| **Curto > extenso** | Lições pequenas. Evita sobrecarga de working memory. |
| **Prática antes de teoria pesada** | Ensina o necessário p/ fazer algo útil agora. |
| **Desirable difficulty** | Recuperação ativa (quiz sem dicas), espaçamento quando repetir. **Não** exagera. |
| **Interleaving com cautela** | Mistura tópicos relacionados só em exercícios práticos. |
| **Fidelidade às fontes** | Cita fontes confiáveis. Prefere docs oficiais. |
| **Reuso** | Antes de criar CSS/quiz novo, vê `assets/`. Se útil p/ futuras lições, extrai componente. |
| **Beautiful but functional** | HTML limpo, legível (Tufte-ish). Foco em clareza. |
| **Grounded na missão** | Toda lição responde: "isso ajuda a alcançar a missão?" |

## 8. Boas práticas

- **1 win por lição.** Ex.: "conseguir rodar 1 teste Playwright com headless".
- **HTML autocontido.** CSS/JS mínimos em arquivo ou via `assets/`.
- **Links internos.** Liga lição ↔ referência ↔ outra lição.
- **Reminder final.** Cada lição deve lembrar: "Pergunte ao agente qualquer dúvida".
- **Aprendizado explícito.** Ao final de sessão, atualiza `learning-records/000X-*.md` com aprendizados reais.
- **ZPD dinâmico.** Se ficou fácil → sobe; se travou → desce.
- **Nunca confiar só em memória paramétrica.** Busca fontes quando incerto.

## 9. Exemplos de invocação

**Aprender Playwright do zero (com objetivo prático)**
```text
me ensina Playwright focado em criar 3 testes E2E simples pra um form
```

**Aprender Bash para automações**
```text
me ensina bash com foco em scripts pra Windows/PowerShell crossover? 
```
(mas foque em bash se ambiente Linux-like; adapte ao seu caso)

**Aprofundar regex**
```text
me ensina regex com exercícios prontos pra aplicar em logs
```

## 10. Integração com seu curso QA/Playwright

Ideal p/ consolidar: crie workspace em pasta dedicada (ex.: `qa-playwright-course/`). Assim:
- `MISSION.md` guarda "por que" (certificação/prática real)
- `lessons/` vira trilha incremental
- `learning-records/` mapeia pontos fracos
- `reference/playwright-cheatsheet.html` cresce com você

## 11. Notas operacionais (opencode)

- Instalado em `~/.config/opencode/skills/teach/`
- Contém `SKILL.md` + 4 `*-FORMAT.md` + `LICENSE`
- Frontmatter adaptado ao opencode
- Invocação por linguagem natural
- Cria estrutura só no diretório atual (não polui global)

## 12. Referências

- [mattpocock/skills – teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach)
- Arquivos locais: `~/.config/opencode/skills/teach/SKILL.md`, `MISSION-FORMAT.md`, `LEARNING-RECORD-FORMAT.md`, `RESOURCES-FORMAT.md`, `GLOSSARY-FORMAT.md`