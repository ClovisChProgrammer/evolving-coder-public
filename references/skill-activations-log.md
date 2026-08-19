# Skill Activation Log — Template

Este arquivo é o **template de referência** para o Protocolo SkillWatch.

---

## Formato do Arquivo por Projeto

Cada projeto na raiz terá um `.skill-log.md` com esta estrutura:

```markdown
# Skill Log — [Nome do Projeto]

Iniciado: YYYY-MM-DD
Última atualização: YYYY-MM-DD

---

## Sessão YYYY-MM-DD

| # | Skill | Linhas | Motivo | Instância |
|---|-------|--------|--------|-----------|
| 1 | evolving-coder | 312L | Startup obrigatório | automática |
| 2 | python-patterns | 441L | Estrutura de projeto | matching |
| 3 | database-design | 158L | Schema de dados | matching |
| 4 | lint-and-validate | 170L | Pós-edição de código | automática |

### Observações

- [Notas sobre escolhas de skill, ativações manuais, etc.]

### Resumo da Sessão

- Skills carregadas: 4
- Skills únicas: 4
- Total de linhas processadas: 1081
- Mais usada: database-design (2 cargas)

---

## Sessão YYYY-MM-DD (se houver múltiplas no mesmo projeto)

...
```

---

## Gatilhos de Instância

| Instância | Quando |
|-----------|--------|
| `automática` | Sistema carregou via matching automático |
| `matching` | Pedido do usuário casou com descrição da skill |
| `manual` | Carreguei explicitamente via ferramenta `skill` |
| `startup` | Skill obrigatória carregada na inicialização |

---

## Mensagens de Anúncio

### Ao carregar skill

```
🔧 SkillWatch: carreguei [nome] ([N]L) — [motivo]
```

### Resumo de final de sessão

```
📊 SkillWatch — Resumo da Sessão
   Skills carregadas: [N]
   Skills únicas usadas: [N]
   Total de linhas processadas: [N]
   Skills mais usadas: [top 3]
```

### Ativação manual sem matching

```
🔧 SkillWatch: habilitei manualmente [nome] ([N]L) — seu pedido menciona [contexto]
```

---

## Notas

- O arquivo `.skill-log.md` fica na raiz de cada projeto
- É versionado (pode ser commitado) — Clóvis gosta de ver o histórico
- Se o arquivo não existir no projeto, crio um novo na primeira SkillWatch
- Se já existir, adiciono uma nova sessão ao final
