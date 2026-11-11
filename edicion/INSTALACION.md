# Instalación de las skills de edición (Windows)

> **Antes de nada:** si es el portátil de Tattoox, **solo con el OK de Marc**. Si no, en el ordenador personal.
> **Estado (11/11/2026):** instalado y probado en el portátil de Tattoox. `npm test` 11/11 OK, demo renderizado (8 s, 1920×1080), `ffmpeg-skill doctor` OK y transcripción local con el filtro `whisper` de FFmpeg funcionando. **faster-whisper NO funciona en este portátil** (ver aviso de Smart App Control).

## ⚠️ Aviso: Smart App Control (portátil de Tattoox)
Este Windows tiene **Smart App Control activado**. Bloquea las DLL sin firma reconocida: `faster-whisper` se instala con pip pero falla al importarse:
```
ImportError: DLL load failed ... Una directiva de Control de aplicaciones bloqueó este archivo.
```
(El bloqueo es de `av\codec\context.pyd`, de PyAV; queda registrado en el visor de eventos → CodeIntegrity/Operational.)
- **No desactivar Smart App Control** en este portátil: no es mío y, una vez desactivado, Windows no deja volver a activarlo sin reinstalar.
- Solución: transcribir con el **filtro `whisper` integrado en FFmpeg** (apartado 5). `ffmpeg.exe` está firmado y no se bloquea.
- Cualquier otra librería de Python con DLL propias puede fallar igual: si aparece este error, es esto.

## El kit (3 piezas)
| Pieza | Para qué | ★ (9/11/2026) | Coste |
|---|---|---|---|
| [herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 15 skills: `short-form-edit`, `cut-silences`, `cut-mistakes`, `video-storytelling`, `hyperframes`… | 2.680 | Gratis |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | Subtítulos karaoke, 9:16, silencios, muletillas en castellano, volumen | 4.870 | Gratis, sin claves |
| Filtro `whisper` de FFmpeg (≥ 8.0) + modelo [ggml-small](https://huggingface.co/ggerganov/whisper.cpp) | Transcripción **local** palabra a palabra (el audio no sale del PC) | — | Gratis |

**Ojo (verificado en `docs/TOOLS-AND-API-KEYS.md` del kit):** el script de transcripción que trae herk-edit-kit usa **ElevenLabs (de pago)**. Para no pagar, se transcribe en local con FFmpeg y se le pide a Claude explícitamente. Kie.ai (B-roll generado) es opcional y de pago: no hace falta.

## 1. Programas base (PowerShell)
```powershell
winget install OpenJS.NodeJS.LTS
winget install Git.Git
winget install Gyan.FFmpeg
winget install Python.Python.3.12
```
Cierra y vuelve a abrir PowerShell. Comprueba (Node 22 o más; FFmpeg 8.0 o más, con whisper):
```powershell
node -v; git --version; ffmpeg -version; py --version
ffmpeg -hide_banner -buildconf | Select-String whisper   # tiene que salir --enable-whisper
```
Chrome: si ya lo tienes, no hace falta nada más (el render usa su propio Chrome Headless Shell, apartado 3).

## 2. Claude Code
```powershell
irm https://claude.ai/install.ps1 | iex
```

## 3. herk-edit-kit
```powershell
cd $HOME\Documents
git clone https://github.com/nateherkai/herk-edit-kit.git
cd herk-edit-kit
npm ci
npm run setup
npm test
npx hyperframes doctor
npx hyperframes browser ensure   # descarga Chrome Headless Shell (obligatorio para renderizar)
```
- `npm ci` avisa de que npm bloquea los scripts de instalación de 4 paquetes (esbuild, onnxruntime-node…). Tests y demo funcionan sin aprobarlos.
- En `hyperframes doctor`, Docker, whisper-cpp, Kokoro y MusicGen son **opcionales**: sus ✗ no importan.
- Si dice *Low memory*, cierra programas antes de renderizar.

Prueba rápida (animación de 8 s, sin vídeo propio ni claves; tarda ~1 min):
```powershell
npm run demo
cd video-projects/demo
npx hyperframes render --quality draft --output renders/demo.mp4
```

## 4. ffmpeg-skill
```powershell
npx ffmpeg-skill
npx ffmpeg-skill doctor
```
Se instala en `~/.claude/skills/ffmpeg-skill` (sirve para cualquier proyecto). En Windows usa `python` o `py` donde la documentación ponga `python3`.

## 5. Transcripción local (filtro `whisper` de FFmpeg)
Descargar el modelo una vez (488 MB):
```powershell
New-Item -ItemType Directory -Force $HOME\Documents\whisper-models
curl.exe -L -o $HOME\Documents\whisper-models\ggml-small.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin
```
Transcribir (en **PowerShell**; en Git Bash la ruta se rompe):
```powershell
$af = 'whisper=model=C\\:/Users/davsa/Documents/whisper-models/ggml-small.bin:language=es:use_gpu=false:format=json:max_len=1:destination=salida.json'
ffmpeg -i grabacion.mp4 -af $af -f null -
```
- **Los dos puntos de la ruta van con doble barra: `C\\:`**. Con una sola (`C\:`) FFmpeg da `No option name near ...`.
- Comillas **simples** en `$af` para que PowerShell no toque las barras.
- `max_len=1` → una palabra por línea. La salida es **JSON Lines** (un objeto por línea) con tiempos en **milisegundos**:
  ```
  {"start":180,"end":780,"text":"analizamos"}
  ```
- `language=es` (o `ca` si grabo en catalán). Sin el idioma correcto, transcribe mal.

**Prueba hecha (11/11/2026):** frase de 4 s con voz sintética de Windows → 8 s de proceso, 10 de 11 palabras bien y tiempo por palabra. Falló una palabra difícil: "multisilábica" salió como `multid...` + `de` + `Silabica`. **Revisar siempre los subtítulos**, sobre todo jerga y rimas (es justo el contenido de la cuenta).

## 6. Cómo pedirle a Claude cada sección
Abre `claude` dentro de la carpeta `herk-edit-kit` y usa estas órdenes (cambia la ruta). Frase común para la transcripción:

> **Transcripción:** transcribe en local con el filtro whisper de FFmpeg (modelo `C:\Users\davsa\Documents\whisper-models\ggml-small.bin`, `language=es`, `max_len=1`, formato json), como en `edicion/INSTALACION.md` del proyecto CAX. No uses ElevenLabs ni faster-whisper. Convierte el JSON Lines (milisegundos) al formato de palabras que espera el kit y enséñame el texto para corregirlo antes de editar.

**Barra explicada (lunes)**
> /short-form-edit Edita mi grabación `C:\...\barra-01.mp4` en un reel 9:16. [Transcripción]. Gancho en los 3 primeros segundos con la barra en pantalla. Cuando cito la barra, texto animado palabra a palabra sincronizado con el audio y resaltado del doble sentido. Corta silencios y errores, subtítulos precisos. Sin B-roll generado.

**Darrere del tema (miércoles)**
> /short-form-edit Reel 9:16 de `C:\...\darrere-01.mp4`. [Transcripción]. Añade una línea de tiempo animada con la estructura del tema (intro, verso, estribillo) y cortes al ritmo del beat. Subtítulos precisos.

**Reacciono al teu tema (viernes)**
> /short-form-edit Reel 9:16 de `C:\...\reaccio-01.mp4`. [Transcripción]. Mi cara en una ventana pequeña sobre el tema del seguidor, su @ en pantalla todo el vídeo, subtítulos karaoke. Normaliza el volumen para que mi voz y su tema se oigan igual.

**Siempre al final**
> Muéstrame el borrador antes del render final y dime qué cortes has hecho.
