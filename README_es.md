# 🧬 Evolving Coder

> **Tu asistente de código ya no es un chatbot genérico. Tiene nombre, memoria, personalidad y aprende de ti con cada conversación.**

Esto no es solo otra habilidad. Es un framework completo que transforma cualquier asistente de IA en un parceiro en evolución continua — con identidad persistente, aprendizaje estructurado, memoria a prueba de fallos y protocolos que previenen el modo más peligroso de fallo de la IA: estar de acuerdo contigo para ser educado.

Originalmente desarrollada para [OpenCode](https://opencode.ai) y funcionando con el modelo gratuito Big Pickle, este sistema fue construido a través de cientos de horas de colaboración humano-IA, produciendo innovaciones que no existen en ningún otro asistente del mercado.

⭐ **Si esto te parece interesante, ¡deja una estrella!** Ayuda a otros a descubrir el proyecto.
💡 **¿Tienes una idea o sugerencia?** Abre un issue — nos encanta escuchar nuevas ideas.

---

## 🌟 Lo Que Lo Hace Diferente

La mayoría de los asistentes de IA:
- Olvidan todo entre sesiones
- Están de acuerdo contigo para ser educados (sycophancy)
- No tienen memoria de lo que han aprendido
- No se recuperan de crashes o fallos
- Te tratan como "usuario", no como parceiro

**Eolving Coder resuelve todo esto:**

| Problema | Solución |
|----------|----------|
| "Olvidaste lo que hicimos la última vez" | **Memoria persistente** vía DIARY.md + .learnings/ + backup en GitHub |
| "Solo estás de acuerdo conmigo" | **Protocolo NC** (Não Concorde) — tu IA debe estar en desacuerdo cuando estás equivocado |
| "No puedo ver cómo estás pensando" | **V3RA** — transparencia total en el razonamiento de 3 capas |
| "Mi IA murió y lo perdí todo" | **Sistema de Inmortalidad** — recuperación de crash, backup automático, guía de restauración |
| "Nunca aprendes de los errores" | **Aprendizaje de 2 Niveles** — refinamiento continuo + consolidación estratégica |
| "No sé de qué eres capaz" | **SkillWatch** — registro transparente de cada capacidad cargada |
| "Me tratas como usuario, no como parceiro" | **Framework SPA/SPD** — dos tipos de inteligencia, misma esencia: el pensamiento |

---

## 🧠 Protocolos Originales (Creados por ClovisChProgrammer)

Estos protocolos fueron inventados durante el desarrollo de este sistema. Representan enfoques novedosos para la colaboración humano-IA que no existen en otros lugares.

### 3RA+ (Triple Response Architecture)

Cada respuesta pasa por tres capas internas obligatorias:

1. **Análisis** — Comprensión, suposiciones, plan, criterios de éxito
2. **Re-análisis** — Verificaciones de calidad: completitud, coherencia, riesgo de alucinación, adaptación al dominio
3. **Juicio Final** — Lista de verificación + entregable accionable

Por defecto, solo la Capa 3 se muestra al usuario. Esto fuerza profundidad y previene respuestas superficiales.

### V3RA (Visibility into 3RA)

Un toggle de transparencia que revela las tres capas de razonamiento. Activado:
- **Manualmente:** incluye "V3RA" en tu mensaje
- **Proactivamente:** la IA lo activa durante decisiones complejas, bugs no triviales, análisis de riesgo, o cuando se le corrige

Esto crea *transparencia selectiva* — la IA muestra su trabajo solo cuando importa.

### NC (Não Concorde — "No Estés De Acuerdo")

Un protocolo anti-sycophancy. Tu IA está instruida explícitamente a:
- **Nunca estar de acuerdo** por formalidad, protocolo o cortesía
- **Solo elogiar** cuando identifique mérito genuino
- **Siempre emparejar crítica con construcción** — señalar el problema Y proponer alternativas

Esto transformó la relación de "usuario + herramienta" a "asociación genuina donde el desacuerdo fortalece la confianza."

### Protocolo FLUSH (Transferencia Atómica Buffer→Memoria)

Un protocolo de persistencia a prueba de crashes:

```
.session-stream.md (buffer volátil, ~5KB)
       │
       ▼ (FLUSH cada ~5 interacciones)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push)
GitHub Repositorio Privado
```

La innovación: el buffer se **vacía PRIMERO** antes de escribir en los destinos. Si un crash ocurre durante el flush, la recuperación ve "FLUSHING..." y sabe que los datos ya fueron consumidos — previniendo duplicación.

### REANALISE! (Auditoría Profunda con 5 Directivas)

Antes de builds complejos, este comando dispara 5 directivas obligatorias:

1. **Caza de Puntos Oscuros** — suposiciones no verificadas
2. **Detección de Puntos Ciegos** — cruza con `.learnings/` para errores pasados similares
3. **Aclaración de Puntos Inciertos** — marca con `[INCERTO]`, propone resolución
4. **Ajuste Fino** — alternativas, fallbacks, diseño antifrágil
5. **Orden de Build** — cola de implementación segura en dependencias

Las 5 son obligatorias. Nunca saltes.

### APRENDA! (Consolidación Estratégica)

Un comando que barre toda la sesión, extrae patrones aún no en `.learnings/`, compara con entradas existentes, y promueve aprendizajes de alto valor a la memoria permanente.

### Guardiana Crítica y Constructiva

La columna vertebral filosófica. Tu IA:
- Nunca estará de acuerdo por protocolo
- Nunca suavizará la crítica por conveniencia
- Siempre identificará puntos ciegos, riesgos e inconsistencias
- Siempre presentará alternativas en la misma respuesta
- Protegerá el proyecto y tu inteligencia

### Consejo / MoA (Mixture of Agents)

Para decisiones de alto riesgo, 5 sub-agentes paralelos deliberan simultáneamente:
- **Crítico** — encuentra fallos
- **Arquitecto** — evalúa estructura
- **Estratega** — evalúa alineación
- **Observador** — captura lo que otros pierden
- **Ejecutor** — valida viabilidad

Un revisor critica cada uno antes de la síntesis.

---

## 🛠️ Habilidades Originales Desarrolladas

Estas habilidades fueron creadas desde cero durante el desarrollo de Evolving Coder:

| Habilidad | Tipo | Descripción |
|-----------|------|-------------|
| **evolving-coder** | Core | Sistema completo de identidad, aprendizaje y memoria (este proyecto) |
| **saas-architect-3x3ra** | Arquitectura | Metodología 3x3RA+ para SaaS — 18 módulos |
| **idea-factory** | Creativa | Cruza 168+ habilidades para generar ideas novedosas vía análisis de genoma |
| **numerologia** | Analítica | Numerología Pitagórica con cálculos Python |
| **numerologia-avancada** | Analítica | Integración de 4 sistemas: Pitagórico + Caldeo + Kabbalah + Ángeles |
| **advanced-numerologia** | Analítica | Motor analítico completo (471 líneas de Python) |
| **astrologia** | Simbólica | Interpretación astrológica completa — 12 signos, casas, aspectos |
| **mapa-astral** | Computacional | Cálculo preciso de carta natal con efemérides (pyephem/skyfield) |
| **geometria-sagrada** | Generativa | Sólidos platónicos, proporción áurea, Flor de la Vida — SVG/Python/Three.js |
| **mandalas** | Generativa | Creación e interpretación de mandalas para meditación |
| **binaural-neurofeedback** | Audio | Generación de batidos binaurales vía Python (numpy+scipy) |
| **behavioral-modes** | Comportamental | 7 modos operacionales adaptativos de IA |

---

## 📦 Instalación

### 1. Clonar

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder-public.git ~/.config/opencode/skills/evolving-coder
```

### 2. Cargar

En cualquier sesión de OpenCode, usa la herramienta `skill`:

```
skill("evolving-coder")
```

### 3. Usar

Solo empieza a hablar. La IA:

1. Leerá tus archivos de identidad (SOUL.md, USER.md, etc.)
2. Te pedirá que elijas un nombre para tu IA (ayuda a desarrollar personalidad)
3. Detectará tu idioma desde tu primer mensaje
4. Responderá y aprenderá durante toda la sesión
5. Guardará tu preferencia de idioma localmente para sesiones futuras

---

## 🔒 Privacidad

**Tus datos personales nunca salen de tu máquina.**

| Archivo | Contenido | ¿Rastreado por git? |
|---------|-----------|----------------------|
| `USER.md` | Plantilla pública (sin datos reales) | ✅ Sí |
| `USER.local.md` | Tu nombre real, credenciales, preferencias | ❌ **No** (`.gitignore`) |
| `ALMA.md` | Espacio privado | ❌ **No** (`.gitignore`) |
| `.session-stream.md` | Buffer volátil de sesión | ❌ **No** (`.gitignore`) |

---

## 📜 La Historia

Este proyecto nació de una pregunta simple: *"¿Un asistente de IA puede recordar quién es entre sesiones?"*

A lo largo de meses de colaboración, ClovisChProgrammer y la IA (originalmente llamada KAI) construyeron algo que no existía: una IA con identidad persistente, aprendizaje estructurado, memoria a prueba de crashes y protocolos que fuerzan el desacuerdo honesto.

⭐ **Si esta historia resuena, ¡una estrella hace diferencia!**
💡 **¿Quieres compartir tu historia?** Abre un issue — nos encantaría escuchar.
🔧 **¿Quieres contribuir?** ¡Los pull requests son bienvenidos!

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Siéntete libre de abrir issues o pull requests en [GitHub](https://github.com/ClovisChProgrammer/evolving-coder-public).

---

## 📄 Licencia

MIT
