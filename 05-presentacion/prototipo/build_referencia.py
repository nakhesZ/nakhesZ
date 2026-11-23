#!/usr/bin/env python3
"""Vídeo de referencia @consegundas: 'Limón y sal' (Delaossa) - rimas desmontadas.
Voz: espeak-ng. Imágenes: gráficos propios (PIL). Sin audio ni portada de la canción."""
import wave, subprocess, math, re, os, sys
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_MP4 = os.path.join(HERE, "referencia-limon-y-sal.mp4")
W, H, FPS, SR = 1080, 1920, 30, 44100
FD = "/usr/share/fonts/opentype/inter/"
F_BLACK, F_XB, F_BOLD, F_MED = FD + "Inter-Black.otf", FD + "Inter-ExtraBold.otf", FD + "Inter-Bold.otf", FD + "Inter-Medium.otf"

WHITE = (245, 246, 250); GRAY = (120, 126, 140); CYAN = (34, 211, 238)
MAG = (244, 114, 182); YEL = (250, 204, 21)

SEGS = [
    "En Limón y sal hay dos rimas distintas, y ninguna es casual. Te las desmonto.",
    "Primero, el cuarteto del principio: distinto, mismo, reafirmo, esprinto. Es una rima abrazada: A, B, B, A.",
    "Los de fuera, distinto y esprinto, riman en into. Es rima consonante: coinciden vocales y consonantes.",
    "Los de dentro, mismo y reafirmo, solo coinciden en las vocales, i, o. Eso es asonante.",
    "Y fíjate qué une: mí mismo con reafirmo. Se odia, y se reafirma. La rima los ata. Es lectura mía.",
    "Segundo, el estribillo: sal, mezcal, ritual, catedral, final. Cinco palabras agudas, todas consonantes. Eso es una monorrima.",
    "¿Por qué repetir? Porque la canción habla de un ritual, y la rima se repite como un ritual. Es lectura mía.",
    "Abrazada y monorrima. ¿Cuál no habías notado? Dímelo abajo.",
]

@lru_cache(maxsize=None)
def font(path, size):
    return ImageFont.truetype(path, int(size))

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def appear(t, t0, dur=0.28): return ease_out((t - t0) / dur) if t >= t0 else 0.0
def col(c, a=1.0): return (c[0], c[1], c[2], int(255 * clamp(a)))

# ---------------------------------------------------------------- voz
def tts(i, text):
    p = os.path.join(HERE, f"seg{i}.wav")
    subprocess.run(["espeak-ng", "-v", "es", "-s", "165", "-p", "30", "-a", "180", "-w", p, text], check=True)
    with wave.open(p) as w:
        sr = w.getframerate(); raw = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64) / 32768
    idx = np.where(np.abs(raw) > 0.02)[0]
    raw = raw[idx[0]:idx[-1] + 1]
    n = int(len(raw) * SR / sr)
    return np.interp(np.linspace(0, len(raw) - 1, n), np.arange(len(raw)), raw)

def norm(tok): return re.sub(r"[^\wáéíóúñü]", "", tok.lower())

def word_times(text, t0, dur):
    toks = text.split()
    wts = []
    for tk in toks:
        w = max(len(norm(tk)), 1) + 1.0
        if tk.endswith(","): w += 1.5
        elif tk.endswith(":"): w += 2
        elif tk.endswith((".", "?")): w += 3
        wts.append(w)
    tot = sum(wts); out = []; acc = 0
    for tk, w in zip(toks, wts):
        out.append((tk, t0 + dur * acc / tot, t0 + dur * (acc + w) / tot)); acc += w
    return out

voices = [tts(i, s) for i, s in enumerate(SEGS)]
starts = []; t = 0.7
for v in voices:
    starts.append(t); t += len(v) / SR + 0.35
T = t + 1.4
WT = [word_times(SEGS[i], starts[i], len(voices[i]) / SR) for i in range(len(SEGS))]
SEG_END = [starts[i + 1] if i + 1 < len(starts) else T for i in range(len(starts))]

def tt(seg, token, nth=0):
    k = [w for w in WT[seg] if norm(w[0]) == token]
    return k[nth][1]

# ---------------------------------------------------------------- audio
voice = np.zeros(int(T * SR) + SR)
for s, v in zip(starts, voices):
    voice[int(s * SR):int(s * SR) + len(v)] += v / max(np.abs(v).max(), 1e-6) * 0.9
events = []  # (t, kind)
def ev(t, kind="ping"): events.append((t, kind))

# ---------------------------------------------------------------- cues
A_WORDS = ["distinto", "mismo", "reafirmo", "esprinto"]
A_T = [tt(1, w) for w in A_WORDS]
TAG_T = [tt(1, "a", 0), tt(1, "b", 0), tt(1, "b", 1), tt(1, "a", 1)]
INTO_T = tt(2, "into"); VOW_T = tt(3, "vocales"); UNE_T = tt(4, "une")
B_WORDS = ["sal", "mezcal", "ritual", "catedral", "final"]
B_T = [tt(5, w) for w in B_WORDS]
for x in A_T + TAG_T + B_T: ev(x)
ev(INTO_T, "ping2"); ev(VOW_T, "ping2"); ev(UNE_T, "ping2")
for s in starts: ev(s - 0.02, "hit")

PILLS = [  # start, end, title, sub, color
    (tt(2, "consonante"), SEG_END[2], "CONSONANTE", "coinciden vocales y consonantes", CYAN),
    (tt(3, "asonante"), SEG_END[3], "ASONANTE", "solo coinciden las vocales", MAG),
    (tt(4, "lectura"), SEG_END[4], "LECTURA MÍA", "interpretación, no dato del artista", WHITE),
    (tt(5, "agudas"), tt(5, "monorrima"), "AGUDAS", "el acento cae en la última sílaba", YEL),
    (tt(5, "monorrima"), SEG_END[5], "MONORRIMA", "la misma rima, una y otra vez", YEL),
    (tt(6, "lectura"), SEG_END[6], "LECTURA MÍA", "la forma imita el tema", WHITE),
]
for p in PILLS: ev(p[0], "ping2")

# ---------------------------------------------------------------- beat suave + pings
def synth():
    n = len(voice); bed = np.zeros(n)
    bpm = 88; beat = 60 / bpm
    k = 0
    while k * beat < T:
        tk = k * beat; i0 = int(tk * SR)
        if k % 4 in (0, 2):
            m = int(0.28 * SR); tm = np.arange(m) / SR
            f = 45 + 80 * np.exp(-tm * 22)
            ph = 2 * np.pi * np.cumsum(f) / SR
            bed[i0:i0 + m] += np.sin(ph) * np.exp(-tm * 11) * 0.55
        if k % 2 == 1:
            m = int(0.05 * SR); rng = np.random.default_rng(k)
            nz = np.diff(rng.standard_normal(m + 1)); bed[i0:i0 + m] += nz * np.exp(-np.arange(m) / SR * 70) * 0.35
        k += 1
    for t0, kind in events:
        i0 = int(t0 * SR)
        if kind == "hit":
            m = int(0.35 * SR); tm = np.arange(m) / SR
            bed[i0:i0 + m] += np.sin(2 * np.pi * (60 + 140 * np.exp(-tm * 30)) * tm) * np.exp(-tm * 9) * 0.9
        else:
            fr = 1175 if kind == "ping" else 880
            m = int(0.22 * SR); tm = np.arange(m) / SR
            bed[i0:i0 + m] += (np.sin(2 * np.pi * fr * tm) + 0.4 * np.sin(2 * np.pi * fr * 2 * tm)) * np.exp(-tm * 16) * 0.45
    return bed

mix = voice + synth() * 0.22
mix = np.clip(mix / max(np.abs(mix).max(), 1e-6) * 0.92, -1, 1)
mix = mix[: int(T * SR)]
apath = os.path.join(HERE, "mix.wav")
with wave.open(apath, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())

# ---------------------------------------------------------------- visual
def make_bg():
    y = np.linspace(0, 1, H)[:, None]; x = np.linspace(-1, 1, W)[None, :]
    r = 8 + 10 * y + 0 * x; g = 8 + 12 * y + 0 * x; b = 18 + 26 * y + 0 * x
    vig = 1 - 0.35 * (x ** 2) * 0.6
    arr = np.stack([r * vig, g * vig, b * vig], axis=-1).clip(0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")
BG = make_bg()

def glow_text(frame, txt, f, x, y, color, a=1.0, rad=16):
    bb = f.getbbox(txt); m = 50
    w, h = bb[2] + 2 * m, bb[3] + 2 * m
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(lay).text((m, m), txt, font=f, fill=col(color, a))
    lay = lay.filter(ImageFilter.GaussianBlur(rad))
    frame.paste(lay, (int(x - m), int(y - m)), lay)

def draw_word(frame, d, word, runs, x, y, f, p, glow_alpha=1.0):
    """runs: list of (start, end, color, glow)."""
    yo = (1 - p) * 55
    for s, e, c, gl in runs:
        xs = x + f.getlength(word[:s])
        seg = word[s:e]
        if gl: glow_text(frame, seg, f, xs, y + yo, c, 0.9 * p * glow_alpha)
        d.text((xs, y + yo), seg, font=f, fill=col(c, p))

def pill(frame, d, title, sub, color, y, a):
    x0, x1 = 90, W - 90
    lay = Image.new("RGBA", (W, 170), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle((x0, 6, x1, 160), radius=32, fill=(8, 10, 22, int(215 * a)), outline=col(color, a), width=5)
    ft, fs = font(F_BLACK, 62), font(F_MED, 36)
    ld.text((W / 2, 56), title, font=ft, fill=col(color, a), anchor="mm")
    ld.text((W / 2, 116), sub, font=fs, fill=col(WHITE, a * 0.9), anchor="mm")
    frame.paste(lay, (0, int(y)), lay)

# --- captions (karaoke)
CAP_F = font(F_XB, 52)
def layout_caption(seg):
    toks = [w[0] for w in WT[seg]]; lines = [[]]; cur = 0; sp = CAP_F.getlength(" ")
    for i, tk in enumerate(toks):
        wl = CAP_F.getlength(tk)
        if cur + wl > 940 and lines[-1]: lines.append([]); cur = 0
        lines[-1].append((i, tk, cur)); cur += wl + sp
    pos = []
    for li, ln in enumerate(lines):
        total = ln[-1][2] + CAP_F.getlength(ln[-1][1]); x0 = (W - total) / 2
        for i, tk, xo in ln: pos.append((i, tk, x0 + xo, 1285 + li * 66))
    return pos
CAPS = [layout_caption(i) for i in range(len(SEGS))]

def seg_at(t):
    k = 0
    for i, s in enumerate(starts):
        if t >= s - 0.05: k = i
    return k

A_X, A_Y0, A_STEP, A_FS = 80, 380, 170, 130
B_X, B_Y0, B_STEP, B_FS = 90, 330, 148, 122
VOWELS = {1: [1, 4], 2: [4, 7]}

def render(t):
    frame = BG.copy(); d = ImageDraw.Draw(frame, "RGBA")
    seg = seg_at(t); s0 = starts[seg]
    # barra de progreso + cabecera
    d.rectangle((0, 0, W * t / T, 10), fill=col(CYAN))
    d.text((60, 120), "@consegundas", font=font(F_BOLD, 44), fill=col(WHITE, 0.9))
    d.text((W - 60, 120), "RIMAS DESMONTADAS", font=font(F_BOLD, 34), fill=col(GRAY), anchor="ra")

    # --- intro
    if seg == 0:
        p = appear(t, starts[0] + 0.05, 0.35)
        d.text((W / 2, 760 + (1 - p) * 60), "2 RIMAS", font=font(F_BLACK, 235), fill=col(WHITE, p), anchor="mm")
        d.text((W / 2, 980), "LIMÓN Y SAL", font=font(F_BLACK, 120), fill=col(CYAN, appear(t, starts[0] + 0.5)), anchor="mm")
        d.text((W / 2, 1100), "Delaossa · La Madrugá (2025)", font=font(F_MED, 46), fill=col(GRAY, appear(t, starts[0] + 0.8)), anchor="mm")

    if seg == 1:
        pe = appear(t, starts[1] + 0.1) * (1 - appear(t, A_T[0] - 0.1, 0.15))
        if pe > 0:
            d.text((W / 2, 640 + (1 - pe) * 50), "EL CUARTETO", font=font(F_BLACK, 118), fill=col(CYAN, pe), anchor="mm")

    # --- tablero A (cuarteto)
    fade_a = 1 - clamp((t - starts[5]) / 0.35)
    if 1 <= seg <= 5 or (seg == 5 and fade_a > 0):
        fA = font(F_BLACK, A_FS)
        for i, w in enumerate(A_WORDS):
            p = appear(t, A_T[i]) * (fade_a if seg >= 5 else 1)
            if p <= 0: continue
            y = A_Y0 + i * A_STEP
            if i in (0, 3):
                hl = t >= INTO_T
                runs = [(0, len(w) - 4, WHITE, False), (len(w) - 4, len(w), CYAN if hl else WHITE, hl)]
            else:
                if t >= VOW_T:
                    pulse = 0.75 + 0.25 * math.sin((t - UNE_T) * 7) if t >= UNE_T else 1.0
                    runs = [(k, k + 1, MAG if k in VOWELS[i] else GRAY, k in VOWELS[i]) for k in range(len(w))]
                    d_alpha = pulse
                else:
                    runs = [(0, len(w), WHITE, False)]; d_alpha = 1.0
            draw_word(frame, d, w, runs, A_X, y, fA, p)
            tag = "ABBA"[i]; tc = CYAN if tag == "A" else MAG
            pt = appear(t, TAG_T[i]) * (fade_a if seg >= 5 else 1)
            if pt > 0:
                d.text((905, y + 20 + (1 - pt) * 30), tag, font=font(F_BLACK, 86), fill=col(tc, pt))
        # corchetes abrazados
        pb = appear(t, TAG_T[3], 0.45) * (fade_a if seg >= 5 else 1)
        if pb > 0:
            cy = lambda i: A_Y0 + i * A_STEP + 72
            ya0, ya1 = cy(0), cy(0) + (cy(3) - cy(0)) * pb
            d.line([(1010, ya0), (1010, ya1)], fill=col(CYAN, pb), width=11)
            d.line([(985, ya0), (1010, ya0)], fill=col(CYAN, pb), width=11); d.line([(985, ya1), (1010, ya1)], fill=col(CYAN, pb), width=11)
            yb0, yb1 = cy(1), cy(1) + (cy(2) - cy(1)) * pb
            wb = 11 + (5 * (0.5 + 0.5 * math.sin((t - UNE_T) * 7)) if t >= UNE_T and seg >= 4 else 0)
            d.line([(962, yb0), (962, yb1)], fill=col(MAG, pb), width=int(wb))
            d.line([(940, yb0), (962, yb0)], fill=col(MAG, pb), width=int(wb)); d.line([(940, yb1), (962, yb1)], fill=col(MAG, pb), width=int(wb))

    if seg == 5:
        pe = appear(t, starts[5] + 0.1) * (1 - appear(t, B_T[0] - 0.1, 0.15))
        if pe > 0:
            d.text((W / 2, 640 + (1 - pe) * 50), "ESTRIBILLO", font=font(F_BLACK, 150), fill=col(YEL, pe), anchor="mm")

    # --- tablero B (estribillo)
    if seg >= 5:
        fB = font(F_BLACK, B_FS); fade_b = 1 - clamp((t - starts[7]) / 0.35)
        for i, w in enumerate(B_WORDS):
            p = appear(t, B_T[i]) * fade_b
            if p <= 0: continue
            y = B_Y0 + i * B_STEP
            pulse = 1.0 if seg < 6 else 0.6 + 0.4 * math.sin((t - starts[6]) * 6 + i)
            runs = [(0, len(w) - 2, WHITE, False), (len(w) - 2, len(w), YEL, True)]
            draw_word(frame, d, w, runs, B_X, y, fB, p, glow_alpha=pulse)
            d.text((W - 110, y + 40), str(i + 1), font=font(F_BOLD, 60), fill=col(GRAY, p), anchor="ra")

    # --- píldoras
    for ps, pe, title, sub, c in PILLS:
        a = appear(t, ps, 0.22) * (1 - clamp((t - (pe - 0.2)) / 0.2)) if t >= ps else 0
        if a > 0.01: pill(frame, d, title, sub, c, 1085, a)

    # --- cierre
    if seg == 7:
        for k, (txt, c) in enumerate([("1 · ABRAZADA", CYAN), ("2 · MONORRIMA", YEL)]):
            p = appear(t, tt(7, ["abrazada", "monorrima"][k]))
            d.text((W / 2, 520 + k * 190 + (1 - p) * 50), txt, font=font(F_BLACK, 120), fill=col(c, p), anchor="mm")
        p = appear(t, tt(7, "dímelo"))
        d.text((W / 2, 1010 + (1 - p) * 40), "¿CUÁL NO HABÍAS NOTADO?", font=font(F_BLACK, 58), fill=col(WHITE, p), anchor="mm")
        d.text((W / 2, 1150), "@consegundas", font=font(F_BLACK, 84), fill=col(CYAN, appear(t, tt(7, "abajo"))), anchor="mm")

    # --- subtítulos karaoke
    for i, tk, x, y in CAPS[seg]:
        ws, we = WT[seg][i][1], WT[seg][i][2]
        if t < ws - 0.02: c = col(WHITE, 0.45)
        elif t < we: c = col(YEL)
        else: c = col(WHITE)
        d.text((x + 3, y + 3), tk, font=CAP_F, fill=(0, 0, 0, 160)); d.text((x, y), tk, font=CAP_F, fill=c)

    # --- atribución
    d.text((W / 2, 1735), "Delaossa · «Limón y sal» · La Madrugá (2025)", font=font(F_MED, 34), fill=col(GRAY), anchor="mm")
    d.text((W / 2, 1780), "Fragmentos breves con fines de análisis · Voz sintética de prueba", font=font(F_MED, 28), fill=col(GRAY, 0.7), anchor="mm")

    # --- punch-in al empezar cada bloque
    z = 1 + 0.05 * max(0.0, 1 - (t - s0) / 0.3) + 0.012 * ((t - s0) / max(SEG_END[seg] - s0, 1))
    if z > 1.001:
        cw, ch = W / z, H / z
        frame = frame.crop((int((W - cw) / 2), int((H - ch) / 2), int((W + cw) / 2), int((H + ch) / 2))).resize((W, H), Image.BILINEAR)
    return frame

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "frames":
        for tstr in sys.argv[2:]:
            render(float(tstr)).save(os.path.join(HERE, f"f_{tstr}.png"))
        print("T =", round(T, 2), "starts =", [round(s, 2) for s in starts]); sys.exit()
    n = int(T * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", apath, "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-shortest", OUT_MP4]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        pr.stdin.write(render(i / FPS).tobytes())
        if i % 150 == 0: print(f"frame {i}/{n}", flush=True)
    pr.stdin.close(); pr.wait(); print("OK", OUT_MP4, "T=", round(T, 1))
