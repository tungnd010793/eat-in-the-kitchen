# -*- coding: utf-8 -*-
"""Dải hình điểm nối: đuôi cụm n (từ chữ cuối - 1s tới hết, mỗi 0,6s) | 3 khung đầu cụm n+1. Ghi _zh/dung/noi/noi_NNN.jpg.
Dùng: python -X utf8 xem_noi.py <n…>"""
import json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
D = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN\_zh\dung")
exec(open(Path(__file__).parent / "lap_dung.py", encoding="utf-8").read().split("edl, md =")[0])
F = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)


def khung(f, t):
    o = Path(tempfile.gettempdir()) / "xn.jpg"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", f, "-frames:v", "1", "-vf", "scale=256:144", str(o)])
    return Image.open(o).copy()


for n in map(int, sys.argv[1:]):
    p = json.loads((D / "phan_tich" / f"cum_{n:03d}.json").read_text(encoding="utf-8"))
    pn = json.loads((D / "phan_tich" / f"cum_{n + 1:03d}.json").read_text(encoding="utf-8"))
    cn = max([x[3] for x in dong_cau(n, p["tu"])] or [20])
    ts = [round(cn - 1 + 0.6 * k, 2) for k in range(30) if cn - 1 + 0.6 * k < p["dai"] - 0.05]
    o = [(f"{n}:{t:.1f}", p["file"], t) for t in ts] + [(f"{n + 1}:{t:.1f}", pn["file"], t) for t in (0.3, 1.2, 2.2)]
    cot = 6
    tam = Image.new("RGB", (cot * 256, ((len(o) + cot - 1) // cot) * 166), "white")
    v = ImageDraw.Draw(tam)
    for i, (nh, f, t) in enumerate(o):
        x, y = (i % cot) * 256, (i // cot) * 166
        tam.paste(khung(f, t), (x, y + 22))
        v.text((x + 4, y + 2), nh + (" ◄ cụm sau" if nh.startswith(f"{n + 1}:") else ""), fill="red" if nh.startswith(f"{n + 1}:") else "black", font=F)
    tam.save(D / "noi" / f"noi_{n:03d}.jpg", quality=80)
    print(n, "chữ cuối", round(cn, 2), "cắt cảnh", [c for c in p["cat_canh"] if c > cn - 1])
