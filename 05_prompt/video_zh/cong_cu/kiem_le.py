# -*- coding: utf-8 -*-
"""Kiểm bài của MỘT người viết khi đã đổi ảnh gửi bằng _zh/refs_moi/cum_NNN.json (chưa gộp vào du_an.json).
Chạy đúng bộ kiểm của skill (kiem_prompt_zh.kiem + kiem_gan_het), refs lấy từ refs_moi nếu có, không thì từ du_an.json.
Không ghi file nào. Dùng: python -X utf8 kiem_le.py <cụm…>"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Admin\.claude\skills\viet-prompt-seedance-zh-tay\scripts")
import kiem_prompt_zh as K  # noqa: E402

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
b = json.loads((DUAN / "bible.json").read_text(encoding="utf-8"))
cl = {c["n"]: c for c in b["clusters"]}
refs = {c["n"]: c["refs"] for c in json.loads((DUAN / "du_an.json").read_text(encoding="utf-8"))["cum"]}
tm = json.loads((DUAN / "anh" / "_ten_anh.json").read_text(encoding="utf-8"))
ten_phim = {str(c.get("name", "")).upper() for c in b.get("characters", [])}
tong = 0
for n in [int(x) for x in sys.argv[1:]] or sorted(cl):
    rm = DUAN / "_zh" / "refs_moi" / f"cum_{n:03d}.json"
    r = json.loads(rm.read_text(encoding="utf-8"))[str(n)] if rm.exists() else refs.get(n, [])
    f = DUAN / "_zh" / "prompt" / f"cum_{n:03d}.txt"
    if not f.exists():
        print(f"cụm {n}: THIẾU {f}"); tong += 1; continue
    txt = f.read_text(encoding="utf-8")
    tron = re.sub(r"（@图片\d+）", "", txt).replace("@", "")
    loi, cb = K.kiem(n, cl[n], r, tm, tron, "", ten_phim)
    loi += K.kiem_gan_het(txt, r, tm, ten_phim)
    by = len(txt.encode("utf-8"))
    if by > 15700:
        loi.append(f"{by} byte > 15.700 (B14: không gửi được)")
    elif by > 15000:
        cb.append(f"{by} byte > 15.000 — rút gọn")
    tong += len(loi)
    print(f"cụm {n}: {'OK' if not loi else f'{len(loi)} LỖI'}" + (f", {len(cb)} cảnh báo" if cb else "") + f" · {by} byte · refs {'refs_moi' if rm.exists() else 'du_an'}")
    for x in loi:
        print("  LỖI  ", x)
    for x in cb:
        print("  C.BÁO", x)
sys.exit(1 if tong else 0)
