# Deep Current — Manual / Manual / Manual

## English

### What is Deep Current?

Deep Current is a generative art piece that visualizes invisible forces through layered particle systems. Two layers — surface (fast, warm, chaotic) and deep (slow, cool, ordered) — flow through Perlin noise vector fields, building density maps that reveal hidden architecture.

### How to Open

1. Open `deep-current.html` in any modern browser (Chrome, Firefox, Edge, Safari)
2. No server needed — the file is completely self-contained
3. The artwork begins animating immediately

### Controls

#### Seed
- **Number field**: Type a seed number and press Enter to load that specific variation
- **← Prev / Next →**: Cycle through sequential seeds
- **↻ Random**: Jump to a random seed
- Each seed produces a unique, reproducible configuration

#### Parameters
| Parameter | What it does | Range |
|-----------|-------------|-------|
| Particle Count | Total particles in the system | 500–8000 |
| Current Speed | How fast particles move through the flow field | 0.1–3.0 |
| Noise Scale | Size of the flow patterns (smaller = larger patterns) | 0.001–0.015 |
| Depth Layers | Visual stratification of the current | 2–8 |
| Turbulence | Random perturbation added to particle movement | 0.0–1.0 |
| Trail Fade | How quickly trails disappear (lower = longer trails) | 2–30 |
| Time Speed | How fast the flow field evolves over time | 0.0001–0.005 |

#### Palette
- **Surface Color**: Color of fast, shallow particles (default: warm copper)
- **Mid Color**: Color of the transition zone (default: ocean teal)
- **Deep Color**: Color of slow, deep particles (default: dark navy)

#### Actions
- **Regenerate**: Restart the animation with current settings
- **Reset**: Restore all parameters to defaults
- **⬇ Download PNG**: Save the current frame as a high-resolution PNG (1200×1200)

### Audio

Deep Current includes a built-in binaural beats engine using the Web Audio API. No plugins or Python needed — just toggle and listen.

#### How to Use

1. **Toggle On**: Click the switch in the Audio section to activate
2. **Choose a brain state**: Click Delta, Theta, Alpha, or Beta preset buttons
3. **Fine-tune**: Adjust Beat Frequency, Carrier Frequency, and Volume sliders
4. **Add pink noise**: Toggle the Pink Noise switch for natural masking sound
5. **Use headphones**: Binaural beats only work with stereo headphones

#### Brain States

| Preset | Beat Range | Effect | Best For |
|--------|-----------|--------|----------|
| Delta | 0.5–4 Hz | Deep sleep, regeneration | Sleeping, healing |
| Theta | 4–8 Hz | Deep meditation, creativity | Meditating, creating |
| Alpha | 8–12 Hz | Relaxation, calm focus | Studying, relaxing |
| Beta | 12–20 Hz | Alert focus, problem solving | Working, analyzing |

#### Seed ↔ Audio Sync

Each seed automatically generates matching audio parameters:
- **Beat frequency**: `seed % 12 + 1` Hz (1–12 Hz range)
- **Carrier frequency**: `seed % 200 + 100` Hz (100–300 Hz range)
- **Brain state**: Auto-selected based on beat frequency

When you change the seed, the audio parameters update automatically to create a unique audiovisual pairing.

#### Tips

- Start with **Seed 12345** — it generates Theta 6 Hz (meditation state)
- **Theta + Deep Current** = meditative experience
- **Alpha + fast particles** = productive focus
- **Delta + slow particles** = sleep preparation
- Lower volume (15–25%) for background use
- Pink noise helps mask external sounds during meditation

### Tips

- Start with **Seed 12345** (default) to see the intended composition
- Lower **Trail Fade** to 2–4 for long, painterly trails
- Increase **Turbulence** to 0.7+ for chaotic, stormy flow
- Decrease **Noise Scale** to 0.001 for large, sweeping currents
- **Particle Count** above 5000 creates dense, oceanic texture
- Each seed is a unique "print" — explore at least 20 seeds to find your favorite

---

## Português (Brasil)

### O que é Deep Current?

Deep Current é uma peça de arte generativa que visualiza forças invisíveis através de sistemas de partículas em camadas. Duas camadas — superfície (rápida, quente, caótica) e profundidade (lenta, fria, ordenada) — fluem por campos vetoriais de ruído Perlin, construindo mapas de densidade que revelam arquitetura oculta.

### Como Abrir

1. Abra `deep-current.html` em qualquer navegador moderno (Chrome, Firefox, Edge, Safari)
2. Não precisa de servidor — o arquivo é completamente autocontido
3. A obra começa a animar imediatamente

### Controles

#### Semente (Seed)
- **Campo numérico**: Digite um número de semente e pressione Enter para carregar uma variação específica
- **← Anterior / Próximo →**: Navegue por sementes sequenciais
- **↻ Aleatório**: Pule para uma semente aleatória
- Cada semente produce uma configuração única e reproduzível

#### Parâmetros
| Parâmetro | O que faz | Intervalo |
|-----------|-----------|-----------|
| Particle Count | Total de partículas no sistema | 500–8000 |
| Current Speed | Velocidade das partículas no campo de fluxo | 0.1–3.0 |
| Noise Scale | Tamanho dos padrões de fluxo (menor = padrões maiores) | 0.001–0.015 |
| Depth Layers | Estratificação visual da corrente | 2–8 |
| Turbulência | Perturbação aleatória no movimento das partículas | 0.0–1.0 |
| Trail Fade | Velocidade de desaparecimento dos rastros (menor = rastros mais longos) | 2–30 |
| Time Speed | Velocidade de evolução do campo de fluxo | 0.0001–0.005 |

#### Paleta
- **Surface Color**: Cor das partículas rápidas e rasas (padrão: cobre quente)
- **Mid Color**: Cor da zona de transição (padrão: teal oceânico)
- **Deep Color**: Cor das partículas lentas e profundas (padrão: azul marinho escuro)

#### Ações
- **Regenerate**: Reinicie a animação com as configurações atuais
- **Reset**: Restaure todos os parâmetros para os padrões
- **⬇ Download PNG**: Salve o frame atual como PNG em alta resolução (1200×1200)

### Áudio

Deep Current inclui um motor de batimentos binaurais integrado usando Web Audio API. Sem plugins ou Python necessários — basta ativar e ouvir.

#### Como Usar

1. **Ative**: Clique no interruptor na seção Audio para ativar
2. **Escolha um estado cerebral**: Clique nos botões Delta, Theta, Alpha ou Beta
3. **Ajuste finamente**: Use os sliders de Frequência de Batimento, Frequência Portadora e Volume
4. **Adicione ruído rosa**: Ative o interruptor Pink Noise para mascaramento natural
5. **Use fones de ouvido**: Batimentos binaurais só funcionam com fones estéreo

#### Estados Cerebrais

| Preset | Faixa | Efeito | Ideal Para |
|--------|-------|--------|-----------|
| Delta | 0,5–4 Hz | Sono profundo, regeneração | Dormir, curar |
| Theta | 4–8 Hz | Meditação profunda, criatividade | Meditar, criar |
| Alpha | 8–12 Hz | Relaxamento, foco calmo | Estudar, relaxar |
| Beta | 12–20 Hz | Alerta focado, solução de problemas | Trabalhar, analisar |

#### Semente ↔ Áudio Sincronizado

Cada semente gera automaticamente parâmetros de áudio correspondentes:
- **Frequência de batimento**: `seed % 12 + 1` Hz (faixa 1–12 Hz)
- **Frequência portadora**: `seed % 200 + 100` Hz (faixa 100–300 Hz)
- **Estado cerebral**: Selecionado automaticamente com base na frequência de batimento

Ao mudar a semente, os parâmetros de áudio se atualizam automaticamente criando um pareamento audiovisual único.

#### Dicas

- Comece com a **Semente 12345** — gera Theta 6 Hz (estado de meditação)
- **Theta + Deep Current** = experiência meditativa
- **Alpha + partículas rápidas** = foco produtivo
- **Delta + partículas lentas** = preparação para sono
- Volume baixo (15–25%) para uso em segundo plano
- Ruído rosa ajuda a mascarar sons externos durante a meditação

### Dicas

- Comece com a **Semente 12345** (padrão) para ver a composição pretendida
- Reduza **Trail Fade** para 2–4 para rastros longos e pintorescos
- Aumente **Turbulence** para 0.7+ para fluxo caótico e tempestuoso
- Reduza **Noise Scale** para 0.001 para correntes grandes e envolventes
- **Particle Count** acima de 5000 cria textura densa e oceânica
- Cada semente é uma "impressão" única — explore pelo menos 20 sementes para encontrar sua favorita

---

## Español

### ¿Qué es Deep Current?

Deep Current es una pieza de arte generativo que visualiza fuerzas invisibles a través de sistemas de partículas en capas. Dos capas — superficie (rápida, cálida, caótica) y profundidad (lenta, fría, ordenada) — fluyen a través de campos vectoriales de ruido Perlin, construyendo mapas de densidad que revelan arquitectura oculta.

### Cómo Abrir

1. Abre `deep-current.html` en cualquier navegador moderno (Chrome, Firefox, Edge, Safari)
2. No se necesita servidor — el archivo es completamente autocontenido
3. La obra comienza a animarse inmediatamente

### Controles

#### Semilla (Seed)
- **Campo numérico**: Escribe un número de semilla y presiona Enter para cargar una variación específica
- **← Anterior / Siguiente →**: Navega por semillas secuenciales
- **↻ Aleatorio**: Salta a una semilla aleatoria
- Cada semilla produce una configuración única y reproducible

#### Parámetros
| Parámetro | Qué hace | Rango |
|-----------|----------|-------|
| Particle Count | Total de partículas en el sistema | 500–8000 |
| Current Speed | Velocidad de las partículas en el campo de flujo | 0.1–3.0 |
| Noise Scale | Tamaño de los patrones de flujo (menor = patrones más grandes) | 0.001–0.015 |
| Depth Layers | Estratificación visual de la corriente | 2–8 |
| Turbulence | Perturbación aleatoria en el movimiento de partículas | 0.0–1.0 |
| Trail Fade | Velocidad de desaparición de los rastros (menor = rastros más largos) | 2–30 |
| Time Speed | Velocidad de evolución del campo de flujo | 0.0001–0.005 |

#### Paleta
- **Surface Color**: Color de las partículas rápidas y someras (por defecto: cobre cálido)
- **Mid Color**: Color de la zona de transición (por defecto: teal oceánico)
- **Deep Color**: Color de las partículas lentas y profundas (por defecto: azul marino oscuro)

#### Acciones
- **Regenerate**: Reinicia la animación con la configuración actual
- **Reset**: Restaura todos los parámetros a los valores predeterminados
- **⬇ Download PNG**: Guarda el fotograma actual como PNG en alta resolución (1200×1200)

### Audio

Deep Current incluye un motor de batidos bináuricos integrado usando Web Audio API. Sin plugins ni Python — solo activa y escucha.

#### Cómo Usar

1. **Activa**: Haz clic en el interruptor en la sección Audio para activar
2. **Elige un estado cerebral**: Haz clic en los botones Delta, Theta, Alpha o Beta
3. **Ajusta finamente**: Usa los controles deslizantes de Frecuencia de Batido, Frecuencia Portadora y Volumen
4. **Añade ruido rosa**: Activa el interruptor Pink Noise para enmascaramiento natural
5. **Usa auriculares**: Los batidos bináuricos solo funcionan con auriculares estéreo

#### Estados Cerebrales

| Preset | Rango | Efecto | Ideal Para |
|--------|-------|--------|-----------|
| Delta | 0,5–4 Hz | Sueño profundo, regeneración | Dormir, sanar |
| Theta | 4–8 Hz | Meditación profunda, creatividad | Meditar, crear |
| Alpha | 8–12 Hz | Relajación, foco calmado | Estudiar, relajarse |
| Beta | 12–20 Hz | Foco alerta, resolución de problemas | Trabajar, analizar |

#### Semilla ↔ Audio Sincronizado

Cada semilla genera automáticamente parámetros de audio correspondientes:
- **Frecuencia de batido**: `seed % 12 + 1` Hz (rango 1–12 Hz)
- **Frecuencia portadora**: `seed % 200 + 100` Hz (rango 100–300 Hz)
- **Estado cerebral**: Seleccionado automáticamente según la frecuencia de batido

Al cambiar la semilla, los parámetros de audio se actualizan automáticamente creando un emparejamiento audiovisual único.

#### Consejos

- Comienza con la **Semilla 12345** — genera Theta 6 Hz (estado de meditación)
- **Theta + Deep Current** = experiencia meditativa
- **Alpha + partículas rápidas** = foco productivo
- **Delta + partículas lentas** = preparación para dormir
- Volumen bajo (15–25%) para uso en segundo plano
- El ruido rosa ayuda a enmascarar sonidos externos durante la meditación

### Consejos

- Comienza con la **Semilla 12345** (predeterminada) para ver la composición prevista
- Reduce **Trail Fade** a 2–4 para rastros largos y pictóricos
- Aumenta **Turbulence** a 0.7+ para un flujo caótico y tormentoso
- Reduce **Noise Scale** a 0.001 para corrientes grandes y envolventes
- **Particle Count** superior a 5000 crea una textura densa y oceánica
- Cada semilla es una "impresión" única — explora al menos 20 semillas para encontrar tu favorita

---

*Arte generativa por Kai (SPD) — Agosto 2026*
*Arte generativa por Kai (SPD) — Agosto 2026*
*Arte generativa por Kai (SPD) — Agosto 2026*
