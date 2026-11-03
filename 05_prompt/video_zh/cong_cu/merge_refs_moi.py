# -*- coding: utf-8 -*-
"""Gộp _zh/refs_moi/cum_NNN.json ({"N": [ảnh…]}) vào du_an.json + bible.json (sao lưu trước). Kiểm: ảnh có thật, ≤ 9, không trùng.
Chạy: python -X utf8 merge_refs_moi.py [--ghi]   (không --ghi: chỉ in kế hoạch)"""
import json, shutil, sys, time
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
GHI = "--ghi" in sys.argv
CHON = {int(x) for x in sys.argv[1:] if x.isdigit()}   # chỉ gộp các cụm này (trống = tất cả)
da = json.loads((DUAN / "du_an.json").read_text(encoding="utf-8"))
bible = json.loads((DUAN / "bible.json").read_text(encoding="utf-8"))
tm = json.loads((DUAN / "anh" / "_ten_anh.json").read_text(encoding="utf-8"))
cum = {c["n"]: c for c in da["cum"]}
cl = {c["n"]: c for c in bible["clusters"]}
loi, doi = [], 0
for f in sorted((DUAN / "_zh" / "refs_moi").glob("cum_*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    for k, refs in d.items():
        n = int(k)
        if CHON and n not in CHON:
            continue
        if n not in cum:
            loi.append(f"{f.name}: không có cụm {n}")
            continue
        if len(refs) > 9 or len(set(refs)) != len(refs):
            loi.append(f"cụm {n}: {len(refs)} ảnh (≤ 9, không trùng)")
        for r in refs:
            if not (DUAN / "anh" / f"{r}.png").exists() or r not in tm:
                loi.append(f"cụm {n}: ảnh {r} không có / chưa vào _ten_anh.json")
        cu = cum[n]["refs"]
        if refs != cu:
            doi += 1
            print(f"cụm {n}: {cu} -> {refs}")
            cum[n]["refs"] = refs
            cl[n]["refs"] = refs
for x in loi:
    print("[LỖI]", x)
print("cụm đổi refs:", doi)
if GHI and not loi and doi:
    t = time.strftime("%m%d_%H%M")
    shutil.copy2(DUAN / "du_an.json", DUAN / f"du_an_truoc_refsmoi_{t}.json")
    shutil.copy2(DUAN / "bible.json", DUAN / f"bible_truoc_refsmoi_{t}.json")
    (DUAN / "du_an.json").write_text(json.dumps(da, ensure_ascii=False, indent=1), encoding="utf-8")
    (DUAN / "bible.json").write_text(json.dumps(bible, ensure_ascii=False, indent=1), encoding="utf-8")
    print("đã ghi du_an.json + bible.json")
