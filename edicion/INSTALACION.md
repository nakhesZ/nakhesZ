# Instalación de las skills de edición (Windows)

> **Antes de nada:** si es el portátil de Tattoox, **solo con el OK de Marc**. Si no, en el ordenador personal.
> **Estado:** comandos sacados de los README oficiales (leídos el 9/11/2026). En la nube **no** se pudieron ejecutar (`npm ci` bloqueado por permisos), así que la primera instalación real es la tuya: si algo falla, copia el error y me lo pasas.

## El kit (3 piezas)
| Pieza | Para qué | ★ (9/11/2026) | Coste |
|---|---|---|---|
| [herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 15 skills: `short-form-edit`, `cut-silences`, `cut-mistakes`, `video-storytelling`, `hyperframes`… | 2.680 | Gratis |
| [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | Subtítulos karaoke, 9:16, silencios, muletillas en castellano, volumen | 4.870 | Gratis, sin claves |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Transcripción **local** palabra a palabra (el audio no sale del PC) | 26.621 | Gratis |

**Ojo (verificado en `docs/TOOLS-AND-API-KEYS.md` del kit):** el script de transcripción que trae herk-edit-kit usa **ElevenLabs (de pago)**. Para no pagar, se usa **Whisper local** (faster-whisper) y se le pide a Claude explícitamente. Kie.ai (B-roll generado) es opcional y de pago: no hace falta.

## 1. Programas base (PowerShell)
```powershell
winget install OpenJS.NodeJS.LTS
winget install Git.Git
winget install Gyan.FFmpeg
winget install Python.Python.3.12
```
Cierra y vuelve a abrir PowerShell. Comprueba (Node tiene que ser 22 o más):
```powershell
node -v; git --version; ffmpeg -version; py --version
```
Chrome: si ya lo tienes, no hace falta nada más.

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
```
Prueba rápida (animación de 8 s, sin vídeo propio ni claves):
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

## 5. Transcripción local
```powershell
py -m pip install faster-whisper
```
La primera vez descarga el modelo (tarda un poco).

## 6. Cómo pedirle a Claude cada sección
Abre `claude` dentro de la carpeta `herk-edit-kit` y usa estas órdenes (cambia la ruta):

**Barra explicada (lunes)**
> /short-form-edit Edita mi grabación `C:\...\barra-01.mp4` en un reel 9:16. Transcribe con Whisper local (faster-whisper), no ElevenLabs. Gancho en los 3 primeros segundos con la barra en pantalla. Cuando cito la barra, texto animado palabra a palabra sincronizado con el audio y resaltado del doble sentido. Corta silencios y errores, subtítulos precisos. Sin B-roll generado.

**Darrere del tema (miércoles)**
> /short-form-edit Reel 9:16 de `C:\...\darrere-01.mp4`. Whisper local. Añade una línea de tiempo animada con la estructura del tema (intro, verso, estribillo) y cortes al ritmo del beat. Subtítulos precisos.

**Reacciono al teu tema (viernes)**
> /short-form-edit Reel 9:16 de `C:\...\reaccio-01.mp4`. Whisper local. Mi cara en una ventana pequeña sobre el tema del seguidor, su @ en pantalla todo el vídeo, subtítulos karaoke. Normaliza el volumen para que mi voz y su tema se oigan igual.

**Siempre al final**
> Muéstrame el borrador antes del render final y dime qué cortes has hecho.
