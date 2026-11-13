# PROYECTO CAX — Gestió integral de xarxes socials (CFGS Màrqueting i Publicitat)

> Archivo de contexto para Claude Code. Léelo entero antes de trabajar en este proyecto.
> Última actualización: 9 de noviembre de 2026.

---

## 0. Cómo trabajar conmigo (instrucciones para Claude)

- **No inventes datos.** Todo dato (cifras, leyes, estadísticas, precios, normas de plataformas) debe estar verificado en una fuente real y citado. Si no lo encuentras, dilo; no lo rellenes.
- **Revisa antes de afirmar.** Piensa y comprueba antes de responder.
- **Tono:** profesional, directo y motivador, como un mentor exigente.
- **Idioma:** hablamos en español. **Los entregables de clase van en catalán.**
- **Contexto:** este es un **proyecto de clase del CFGS**. Contexto de estudiante. **No mezclar con Zeraut** ni con otros proyectos en el mismo entregable.
- **Estilo de los entregables de clase:**
  - Breves y simples, con voz de alumno (no demasiado profesionales).
  - Responder **solo lo que pide el enunciado**, sin información innecesaria.
  - Diseño con **un solo color como mucho: azul**. Nada de naranja.

---

## 1. Quién soy

- **David Santiago Mora**, alumno del **CFGS de Màrqueting i Publicitat** en el **Centre d'Estudis Politècnics de Barcelona (CEP)**.
- Hago música urbana (rap, trap, reggaeton). Por eso tengo credibilidad para analizar música.
- Proyecto **individual**.

---

## 2. Qué pide el enunciado

### Contexto
El alumnado trabaja como creador y gestor de su propia marca digital y construye una **estrategia integral de redes sociales**: planificación de publicaciones, creación de contenidos y dinamización de la comunidad, **cumpliendo la normativa de protección de datos**. El objetivo no es solo publicar, sino **generar participación, interacción y convertir seguidores en comunidad**.

### L'encàrrec
1. Crear un **informe atractivo** que presente la gestión integral de redes siguiendo la estrategia y la normativa de protección de datos.
2. Crear una **breve presentación visual** con la estrategia integral de contenidos audiovisuales en redes, **de la semana del 25 de enero a la semana del 12 de marzo**, que incluya:
   1. Objectius SMART de comunicació
   2. Segmentació i definició del públic objectiu
   3. Selecció de plataforma social adequada
   4. Posicionament (to, valors i personalitat)
   5. Planificació de contingut (+ enllaç al full de càlcul)
   6. Pla de crisi i gestió de la reputació digital
   7. Creació i presentació de perfils professionals

### El lliurament
- **Presentación visual en PDF, máximo 10 diapositivas.** Tiene que ser **muy visual**, porque se defiende en una taula de validació.

### Fechas clave
| Fecha | Qué |
|---|---|
| **Hasta el viernes 13 de noviembre de 2026** | Validación de la idea con la **taula d'orientació** |
| **Semana del 30 de noviembre al 4 de diciembre de 2026** | **Taula de validació** (defensa oral) |
| **Viernes 4 de diciembre de 2026** | **ENTREGA** del PDF |
| **Del lunes 25 de enero al domingo 14 de marzo de 2027** | Ejecución: 7 semanas publicando |

### Resultados de aprendizaje (RA)
- **RA1.** Crea y actualiza perfiles corporativos en redes sociales siguiendo estrategias de posicionamiento, segmentación y dinamización.
- **RA2.** Produce, publica y gestiona contenido audiovisual en redes a partir del plan establecido, **gestionando y moderando las interacciones con los usuarios**.
- **RA3.** Analiza los indicadores clave de rendimiento (KPI) en redes sociales.

### Perfiles profesionales implicados
- **Comunicación y estrategia digital:** Community Manager, Digital Brand Manager, Copywriter, Analista de marketing.
- **Creación de contenidos audiovisuales:** Diseñador/a gráfico/a, Content Creator, Cámara y fotógrafo/a de contenido, **Editor/a de vídeo**.

### ODS implicados
- ODS 4 (Educación de calidad), ODS 5 (Igualdad de género: comunicación inclusiva), ODS 8 (Trabajo decente), ODS 12 (Consumo y producción responsables: contenido ético y sostenible), ODS 17 (Alianzas: activación de comunidades).

### Píldoras formativas del proyecto
4. Presència de marca · 5. Creació de contingut · 6. Què diu la llei · 7. Gestió de xarxes socials

### Etapas del proyecto (metodología ABP del CEP)
Etapa 0 Benvinguda → 1 Conèixer el projecte (demandas) → 2 Què ens cal? (recursos, herramientas, conocimientos, habilidades, contactos) → 3 Organització i gestió (planificación) → 4 Disseny (ideas, prototipos) → 5 Creació (retos, producto mínimo viable primero) → 6 Presentació (técnica y pública) → 7 Revisió. Además: **Diari d'autoavaluació** individual.

---

## 3. Decisiones tomadas

| Tema | Decisión |
|---|---|
| **Idea** | Cuenta de **rap y música urbana** con todo lo que haga falta: barras difíciles explicadas (Hoke…), cómo se hace una rima (pareada AABB, cruzada ABAB, abrazada ABBA, multisilábica, interna) con ejemplos, significado de canciones (Delaossa…), historia e inicios de artistas, noticias del rap y reacciones a temas de artistas emergentes. **No** es una "escuela del rap" |
| **Referente** | Izaro (@izaromur, TikTok): análisis de rap español desde la cultura y la historia (~110,7 mil seguidores, dato indexado sin fecha) |
| **Diferenciador** | (1) **Nicho de un solo género**: rap español (pendiente de confirmar; feedback de la taula d'orientació 13/11). (2) **No solo analizo las barras: enseño cómo se crean**, paso a paso. Firma visual: rimas que se encienden en pantalla. DAFO: `01-validacion-idea/dafo.md` |
| **Firma visual** | Todo en pantalla, dinámico (sin libreta): la barra en grande palabra a palabra sincronizada con el audio; las rimas se "encienden" con el mismo color cuando suenan; esquema AABB/ABAB/ABBA animado; congelar + zoom en el doble sentido ("lo que oyes / lo que dice"); cortes al beat; sonido de firma en cada revelación; final "léela otra vez" con la barra coloreada y medidor de dificultad 1–5. Herramientas: HyperFrames + GSAP (herk-edit-kit) y tiempos por palabra del filtro whisper. Grabación en el estudio |
| **Storytelling** | Bucle de 4 pasos en cada vídeo: apuestas → gran pregunta → giro → reenganche. Plantillas: `06-produccion/guiones/plantillas-bucle.md` |
| **Cuenta** | **Nueva**, creada para el proyecto (no Santo Kenvo) |
| **Plataformas** | **TikTok + Instagram Reels**, mismo vídeo vertical en las dos |
| **Tipo de cuenta** | Personal o de creador, **no de empresa** (ver apartado legal) |
| **Formato** | **Individual** |
| **Frecuencia** | Propuesta: **5 vídeos/semana × 7 = 35** (datos de Buffer: 2–5/semana en TikTok y 3–5 en Instagram). **Pendiente de confirmar** en la taula; mínimo 3 |

### Pilares de contenido y semana tipo (propuesta, 11/2026)
| Día | Pilar | Ejemplo |
|---|---|---|
| Lunes | **Barra difícil explicada** | Una barra de Hoke que casi nadie entiende |
| Martes | **Cómo se hace** | Rima abrazada (ABBA) con un ejemplo real y otro mío |
| Miércoles | **Significado de una canción** o **historia de un artista** (alternando) | De qué habla un tema de Delaossa / los inicios de un artista |
| Jueves | **Noticia del rap** | La noticia + el detalle de músico que nadie cuenta |
| Viernes | **Reacciono a tu tema** | Artistas emergentes: una cosa que funciona y una que mejorar (comunidad, RA2) |

Si la frecuencia queda en 3: lunes, miércoles y viernes, rotando los pilares.

### Pendiente de decidir
- [ ] **Nombre de la cuenta** (y comprobar que el usuario está libre en TikTok e Instagram)
- [ ] **Idioma de los vídeos** (castellano o catalán)
- [ ] Definición detallada del **público objetivo**
- [ ] **Objetivos SMART** (cuenta nueva: se parte de 0 seguidores)
- [ ] **Hoja de cálculo** con el calendario de los 21 vídeos
- [ ] **Plan de crisis** y gestión de la reputación
- [ ] **Bases/autorización** para los temas que envían los seguidores
- [ ] **Perfiles** de TikTok e Instagram (bio, foto, enlaces)

---

## 4. Aspectos legales (verificado)

- **Derecho de cita (art. 32.1 Ley de Propiedad Intelectual):** permite usar **fragmentos** de obras ajenas para **análisis, comentario o juicio crítico**, indicando **autor y fuente**, con **finalidad docente o de investigación**. El Tribunal Supremo (sentencia 724/2023, de 16 de mayo) recalcó que **debe ser un fragmento, no la obra entera**. La finalidad docente en una cuenta de TikTok es una **zona gris**: no afirmar que estamos cubiertos al 100 %.
  - **Medidas:** fragmentos cortos, siempre con análisis encima, citar artista y tema en cada vídeo.
  - Fuente: https://www.cuatrecasas.com/es/spain/art/el-todo-no-es-la-parte-el-limite-de-la-cita-segun-el-tribunal-supremo
- **Música en TikTok:** las cuentas de empresa solo pueden usar la **Commercial Music Library** (música con licencia comercial); la biblioteca general no está disponible para marcas. TikTok advierte que usar la biblioteca general con una cuenta personal para promocionar un negocio supone riesgo de infringir derechos.
  - Fuente: https://ads.tiktok.com/business/ko/blog/audio-library-royalty-free-music
- **Temas de los seguidores:** antes de publicar, autorización de la persona para usar **su tema, su imagen y su voz**.
- **Protección de datos de menores (art. 7 Ley Orgánica 3/2018, LOPDGDD):** un menor puede consentir el tratamiento de sus datos **a partir de los 14 años**; por debajo hace falta el consentimiento de padres o tutores. Pedir solo los datos imprescindibles.
  - Fuente: https://www.aepd.es/es/preguntas-frecuentes/10-menores-y-educacion/FAQ-1001-cual-es-la-edad-para-que-los-menores-puedan-prestar-consentimiento-para-tratar-sus-datos-personales

*No es asesoramiento legal: es información verificada en fuentes.*

---

## 5. Preguntas para la taula d'orientació (13 de noviembre)
1. ¿Puedo usar IA para editar los vídeos si lo explico en la presentación como parte de mi flujo de trabajo? (Uno de los perfiles evaluados es Editor/a de vídeo.)
2. ¿Usar fragmentos de canciones para analizarlas se considera finalidad docente dentro de este proyecto?
3. ¿3 vídeos por semana es la frecuencia que se pide?

**Ficha de validación ya creada (en catalán):** https://claude.ai/artifact/TeJFMT7UvY9yNvnb9ygx4T

---

## 6. Edición de vídeo

- **Reparto:** yo grabo, Claude edita.
- **Kit elegido:** [herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) (2.680 ★ a 9 nov 2026). 15 skills para Claude Code, entre ellas `edit-video`, `short-form-edit` (reels 9:16 con gancho, subtítulos, B-roll y sonido), `cut-silences` y `cut-mistakes`. Funciona en local, pero su script de transcripción usa ElevenLabs (de pago): para no pagar, transcribir en local con el **filtro `whisper` de FFmpeg** (faster-whisper no funciona en el portátil de Tattoox: lo bloquea Smart App Control, que no se toca). Instalado y probado el 11/11/2026. Guía completa: `edicion/INSTALACION.md`.
- **Complemento:** [HyperFrames](https://github.com/heygen-com/hyperframes) (81.492 ★ a 9 nov 2026, Apache-2.0, gratis) para motion graphics y subtítulos animados (ideal para "Barra explicada").
- **Herramientas verificadas** (estrellas consultadas en la API de GitHub el 9 nov 2026; README y licencias leídos; **no probadas todavía**):

  | Para qué | Repo | ★ | Licencia |
  |---|---|---|---|
  | Editar reels (cortes, subtítulos, B-roll, sonido) | [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 2.680 | propia |
  | Utilidades FFmpeg (subtítulos karaoke, recorte 9:16, silencios, volumen) | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | 4.870 | MIT |
  | Cortar silencios | [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | 5.822 | Unlicense |
  | Animaciones y texto animado (HTML → vídeo) | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 81.492 | Apache-2.0 |
  | Animaciones con React | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) + [skills](https://github.com/remotion-dev/skills) | 71.936 / 6.676 | gratis para particulares |
  | Pulir motion graphics | [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) | 1.480 | Apache-2.0 (versión temprana) |
  | Transcribir con tiempo por palabra (subtítulos sincronizados) | [m-bain/whisperX](https://github.com/m-bain/whisperX) | 25.168 | BSD-2 |
  | Recortar brutos a mano, sin recomprimir | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) | 45.860 | GPL-2.0 |
  | Que Claude "vea" el vídeo para revisarlo | [jordanrendric/claude-video-vision](https://github.com/jordanrendric/claude-video-vision) | 1.478 | MIT |
  | Directorio de 180 repos con nota de seguridad | [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | 1.811 | — |
- **Requisitos:** Node.js 22+, Git, FFmpeg (con ffprobe), Chrome o Chromium.
- **Instalación (Windows, PowerShell):**
  ```powershell
  winget install OpenJS.NodeJS.LTS
  winget install Git.Git
  winget install Gyan.FFmpeg
  # cerrar y reabrir PowerShell
  irm https://claude.ai/install.ps1 | iex
  cd $HOME\Documents
  git clone https://github.com/nateherkai/herk-edit-kit.git
  cd herk-edit-kit
  npm ci
  npm run setup
  npm test
  claude
  ```
- **Ojo:** el portátil actual es **de Tattoox (asignado para las prácticas)**. Antes de instalar nada ahí, **preguntar a Marc**, o instalarlo en el ordenador personal.
- **No se edita nada hasta el 25 de enero de 2027.**

### Estructura de carpetas (creada el 9 nov 2026)
```
00-enunciado/              ← enunciado completo
01-validacion-idea/        ← decisiones y preguntas para el 13/11
02-estrategia/             ← los 7 puntos + protección de datos
03-calendario/             ← hoja de cálculo de los vídeos (+ KPI)
04-legal/                  ← autorización de seguidores, derechos, menores
05-presentacion/           ← guion de las 10 diapositivas y PDF final
06-produccion/             ← guiones/, brutos/, editados/ (vídeos fuera de git)
07-kpi/                    ← análisis semanal (RA3)
08-diario-autoevaluacion/  ← diari d'autoavaluació
edicion/                   ← instalación de las skills y órdenes por sección
```

---

## 7. Próximos pasos
1. Decidir **nombre** e **idioma** → completar la ficha de validación.
2. **13 nov:** taula d'orientació, con las 3 preguntas del apartado 5.
3. Construir la **presentación PDF (máx. 10 diapositivas, en catalán, azul)** y la **hoja de cálculo** con el calendario.
4. **30 nov – 4 dic:** taula de validació. **4 dic:** entrega.
5. **Navidad:** instalar Claude Code + herk-edit-kit (en ordenador personal o con permiso de Tattoox).
6. **25 ene – 14 mar 2027:** grabar, editar y publicar los 21 vídeos; medir KPI cada semana (RA3).
