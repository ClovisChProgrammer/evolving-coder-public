# Evolving Coder

[![OpenCode](https://img.shields.io/badge/OpenCode-compatible-blue)](https://opencode.ai)

> 🌐 **Otros idiomas:**
> [🇬🇧 English](README.md) ·
> [🇧🇷 Português](README_pt-BR.md)

Una habilidad de auto-mejora para **OpenCode** que mantiene la identidad de tu asistente, aprende de cada interacción y extrae conocimiento reutilizable — todo mientras respeta tu privacidad.

---

## 📋 Descripción

Esta habilidad transforma tu agente de IA en un asistente en mejora continua con:

- **Identidad definida** — principios, reglas de comportamiento y memoria que persisten entre sesiones
- **Detección automática de idioma** — responde en tu idioma (es, pt-BR, en, etc.) desde el primer mensaje
- **Aprendizaje continuo** — registra correcciones técnicas, preferencias del usuario, contexto de proyectos y adaptaciones de comunicación
- **Detección de patrones** — identifica problemas recurrentes y los promueve a la memoria permanente
- **Extracción de habilidades** — convierte aprendizajes valiosos en habilidades OpenCode reutilizables

---

## 🚀 Inicio Rápido

### 1. Instalación

Clona la habilidad al directorio de habilidades de OpenCode:

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder.git ~/.config/opencode/skills/evolving-coder
```

### 2. Carga

En cualquier sesión de OpenCode, usa la herramienta `skill`:

```
skill("evolving-coder")
```

### 3. Uso

Solo empieza a hablar. El agente:

1. Leerá tus archivos de identidad (SOUL.md, USER.md, etc.)
2. Detectará tu idioma desde tu primer mensaje
3. Responderá y aprenderá durante toda la sesión
4. Guardará tu preferencia de idioma localmente para sesiones futuras

---

## 📁 Estructura

```
~/.config/opencode/skills/evolving-coder/
├── SKILL.md              # Instrucciones principales (cargado vía skill tool)
├── SOUL.md               # Identidad y principios del asistente
├── USER.md               # Plantilla pública de perfil (sin datos personales)
├── USER.local.md         # 🔒 Perfil privado (creado localmente, en .gitignore)
├── AGENTS.md             # Reglas operacionales y flujo de trabajo
├── IDENTITY.md           # Plantilla de identidad (nombre, criatura, vibe, emoji)
├── .learnings/           # 📝 Registros de aprendizaje por proyecto
│   ├── LEARNINGS.md
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
├── scripts/
│   ├── extract-skill.ps1  # Extracción de habilidades (Windows PowerShell)
│   └── extract-skill.sh   # Extracción de habilidades (Unix)
├── references/
│   ├── aprenda-procedure.md
│   ├── examples.md
│   ├── hooks-setup.md
│   ├── opencode-integration.md
│   ├── reanalyse-procedure.md
│   ├── skill-activations-log.md
│   ├── skillwatch-protocol.md
│   └── url-access-fallback.md
├── assets/
│   ├── SKILL-TEMPLATE.md
│   ├── LEARNINGS.md
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
├── README.md              # 🇬🇧 English
├── README_pt-BR.md        # 🇧🇷 Portugués
└── README_es.md           # 🇪🇸 Este archivo
```

---

## 🌍 Soporte de Idiomas

La habilidad detecta tu idioma **automáticamente** desde tu primer mensaje:

| Tu mensaje comienza con... | Idioma detectado |
|---------------------------|------------------|
| "Hola", "buenos días", "gracias" | 🇪🇸 **es** (Español) |
| "Olá", "oi", "bom dia" | 🇧🇷 **pt-BR** (Portugués) |
| "Hello", "hi", "good morning" | 🇬🇧 **en** (Inglés) |
| Otro o ambiguo | 🇬🇧 **en** (por defecto, preguntará) |

**Una vez detectada**, tu preferencia se guarda en `USER.local.md` (solo local, nunca se sube al repositorio).

> El contenido técnico (código, comandos, logs) permanece en inglés independientemente de tu idioma.

---

## 🧠 Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| **🧠 Identidad** | SOUL.md define quién eres; USER.md recuerda a quién ayudas |
| **📝 Aprendizaje** | Registra correcciones técnicas, preferencias personales, contexto de proyectos |
| **🔄 Patrones** | Rastrea problemas recurrentes y promueve a memoria permanente |
| **📦 Extracción** | Convierte aprendizajes valiosos en habilidades reutilizables vía `scripts/extract-skill.ps1` |
| **🎯 Modo Dual** | Programación técnica + desarrollo personal conversacional |
| **🌐 Multilingüe** | Detecta y responde automáticamente en es, pt-BR, en, y otros |
| **🔒 Privacidad** | Datos personales quedan en `USER.local.md` (en `.gitignore`) |

---

## 🔄 Cómo Funciona — Metodología APR

Cada interacción sigue tres pasos:

1. **Aprender** — Consultar `.learnings/` y archivos de identidad antes de responder
2. **Practicar** — Aplicar el conocimiento acumulado (técnico + contexto del usuario)
3. **Refinar** — Después de la interacción, registrar nuevos aprendizajes

### Formato de Registro

```
## [LRN-YYYYMMDD-XXX] categoría

**Area**: frontend | backend | user_preference | project_context | ...
**Priority**: low | medium | high | critical
**Status**: pending | resolved | promoted

### Summary | Details | Suggested Action
```

Cuando un aprendizaje se repite (≥3 veces, ≥2 tareas, ventana de 30 días), se **promueve** a la memoria permanente (SOUL.md, USER.md, o AGENTS.md).

---

## 🔒 Privacidad

**Tus datos personales nunca salen de tu máquina.**

| Archivo | Contenido | Rastreado por git? |
|---------|-----------|--------------------|
| `USER.md` | Plantilla pública (sin datos reales) | ✅ Sí |
| `USER.local.md` | Tu nombre real, credenciales, preferencias | ❌ **No** (en `.gitignore`) |
| `.learnings/` | Registros de sesión y aprendizajes | ❌ **No** (en `.gitignore`) |

### Cómo funciona

1. En la primera ejecución, el agente detecta tu idioma y crea `USER.local.md`
2. Puedes completar tu perfil (nombre, profesión, preferencias) — totalmente opcional
3. El archivo está protegido por `.gitignore` y nunca se commitea o envía
4. Cada proyecto tiene su propio directorio `.learnings/` (también en `.gitignore`)

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues o pull requests en [GitHub](https://github.com/ClovisChProgrammer/evolving-coder).

---

## 📄 Licencia

MIT


