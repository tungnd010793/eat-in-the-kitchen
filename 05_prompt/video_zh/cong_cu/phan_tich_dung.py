# -*- coding: utf-8 -*-
"""Phân tích từng cụm để dựng: nghe lại bằng whisper (từng từ có mốc giờ), dò điểm cắt cảnh, dò khoảng lặng, đo độ dài.
Ghi _zh/dung/phan_tich/cum_NNN.json. Chạy: python -X utf8 phan_tich_dung.py [cụm…]   (trống = 1..70; cụm đã có file thì bỏ qua)"""
import json, re, subprocess, sys
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
RA = DUAN / "_zh" / "dung" / "phan_tich"
RA.mkdir(parents=True, exist_ok=True)
ST = json.loads((DUAN / "video" / "_trang_thai.json").read_text(encoding="utf-8"))
DS = [int(x) for x in sys.argv[1:] if x.isdigit()] or list(range(1, 71))


def ff(args):
    return subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stderr


def do_dai(f):
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", ff(["-i", str(f)]))
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def cat_canh(f):
    e = ff(["-i", str(f), "-vf", "select='gt(scene,0.28)',showinfo", "-an", "-f", "null", "-"])
    return [round(float(x), 2) for x in re.findall(r"pts_time:([\d.]+)", e)]


def lang(f):
    e = ff(["-i", str(f), "-af", "silencedetect=noise=-38dB:d=0.35", "-vn", "-f", "null", "-"])
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", e)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", e)]
    return [[round(a, 2), round(b, 2)] for a, b in zip(st, en + [None] * (len(st) - len(en))) if b is not None] + \
           ([[round(st[-1], 2), None]] if len(st) > len(en) else [])


from faster_whisper import WhisperModel  # noqa: E402
model = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=8)   # máy thiếu cublas64_12.dll -> CPU
for n in DS:
    out = RA / f"cum_{n:03d}.json"
    if out.exists():
        continue
    f = DUAN / ST[str(n)]["file"]
    segs, _ = model.transcribe(str(f), language="en", word_timestamps=True, vad_filter=False, beam_size=5)
    words, segl = [], []
    for s in segs:
        segl.append({"a": round(s.start, 2), "b": round(s.end, 2), "text": s.text.strip()})
        for w in s.words or []:
            words.append({"a": round(w.start, 2), "b": round(w.end, 2), "w": w.word.strip(), "p": round(w.probability, 2)})
    d = {"cum": n, "file": str(f), "dai": round(do_dai(f), 3), "cat_canh": cat_canh(f), "lang": lang(f), "doan": segl, "tu": words}
    out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"cụm {n}: {d['dai']}s · {len(words)} từ · lời cuối {words[-1]['b'] if words else '-'}s · cắt cảnh {d['cat_canh']}", flush=True)
print("HẾT", flush=True)
