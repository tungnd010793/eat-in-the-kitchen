# -*- coding: utf-8 -*-
"""Dựng bible.json + du_an.json["cum"] + anh/_ten_anh.json cho EAT IN THE KITCHEN từ kịch bản chốt (04_kich-ban-chinh-thuc.md).

Giữ nguyên mọi khoá ảnh đã có trong du_an.json (nhan_vat, bang_4_goc, dao_cu, boi_canh…), chỉ ghi lại khoá "cum".
Refs mặc định từng cụm: panel bối cảnh TRƯỚC → bảng nhân vật (người nói trước, rồi người im) → đạo cụ SAU; tối đa 9 ảnh.
Người viết bài được thêm / bớt panel qua _zh/refs_moi/cum_NNN.json (QUY_CHUAN_VIET.md mục 7); merge_refs_moi.py gộp lại.
Dùng: python -X utf8 build_du_an.py
"""
import json
import re
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
KB = Path(r"F:\Tungnd\Github\eat-in-the-kitchen\04_kich-ban-chinh-thuc.md")
DATA = DUAN / "_zh" / "data"

TEN = {"MARGUERITE": "MARGUERITE", "DEVIN": "DEVIN", "RAVEN": "RAVEN", "CHARLENE": "CHARLENE", "INÈS": "INES",
       "PRENTICE": "PRENTICE", "ASHANTI": "ASHANTI", "SISTER BERNICE": "BERNICE", "SISTER PEARL": "PEARL",
       "QUẢN LÝ NHÀ HÀNG": "MANAGER", "BẢO VỆ NHÀ HÀNG": "BOUNCER", "NHÂN VIÊN NHÀ ĐẤT": "AGENT", "BẢO VỆ KHU": "GUARD",
       "BẢO VỆ TOÀ NHÀ": "SECURITY", "DR. OKONJO": "OKONJO", "TANISHA": "TANISHA", "PHÓNG VIÊN": "REPORTER",
       "CẢNH SÁT": "OFFICER", "CHỊ ĐIỀU PHỐI": "COORDINATOR", "ĐỒNG NGHIỆP KHO": "COWORKER", "QUẢN LÝ KHO": "FOREMAN",
       "NGƯỜI XIN VIỆC": "APPLICANT"}

# bộ đồ theo cụm (05_prompt/ghi-chu-dung/tu-do-nhan-vat.md mục 1; mỗi cụm MỘT bảng mỗi người)
def _r(a, b):
    return set(range(a, b + 1))


DO = {
    "MARGUERITE": [("M0A", _r(4, 9)), ("M0", _r(1, 11)), ("M1", _r(12, 32) | _r(39, 43)), ("M2", _r(34, 38)),
                   ("M3W", _r(52, 55) | _r(57, 62)), ("M3", {49, 51, 66}), ("M4", _r(68, 70))],
    "DEVIN": [("V0", {2, 3} | _r(12, 14) | _r(18, 20) | _r(39, 44)), ("V2", _r(4, 11)), ("V1", _r(21, 33) | _r(45, 49)),
              ("V3", _r(34, 38)), ("V4H", {56}), ("V4", _r(50, 62)), ("V7", {63}), ("V5", {64, 65, 66}), ("V8", {67}),
              ("V6", _r(68, 70))],
    "RAVEN": [("R1", _r(4, 11)), ("R0", {1, 2, 3, 21, 33, 44}), ("R2", _r(12, 20) | _r(39, 43) | {48, 49}),
              ("R3", _r(22, 28) | _r(34, 38)), ("R4", {56}), ("R5", _r(50, 62)), ("R6", {63}), ("R7", {64})],
    "CHARLENE": [("CH1", _r(4, 10)), ("CH3", _r(22, 28) | _r(34, 38)), ("CH4", {50}), ("CH5C", {56}), ("CH5W", _r(57, 62)),
                 ("CH5", _r(52, 55)), ("CH6", {63}), ("CH7", {64}), ("CH2", set(range(1, 71)))],
    "INES": [("I1", _r(22, 38)), ("I2", set(range(1, 71)))],
    "PRENTICE": [("P1", set(range(1, 71)))], "ASHANTI": [("A1", set(range(1, 71)))],
    "BERNICE": [("SB2", {64}), ("SB1", set(range(1, 71)))], "PEARL": [("SP2", {64}), ("SP1", set(range(1, 71)))],
    "MANAGER": [("QL1", set(range(1, 71)))], "BOUNCER": [("BV1", set(range(1, 71)))], "AGENT": [("AG1", set(range(1, 71)))],
    "GUARD": [("PT1", set(range(1, 71)))], "SECURITY": [("BV2", set(range(1, 71)))], "OKONJO": [("O1", set(range(1, 71)))],
    "TANISHA": [("T1", set(range(1, 71)))], "REPORTER": [("RP1", set(range(1, 71)))], "OFFICER": [("OF1", set(range(1, 71)))],
    "COORDINATOR": [("DP1", set(range(1, 71)))], "COWORKER": [("DN1", set(range(1, 71)))],
    "FOREMAN": [("QK1", set(range(1, 71)))], "APPLICANT": [("XV1", set(range(1, 71)))],
}


def sheet_cua(ten, n):
    for ma, ds in DO[ten]:
        if n in ds:
            return f"SHEET_{ten}_{ma}"
    raise KeyError((ten, n))


PROP_LUAT = [  # (đạo cụ, mẫu tìm trong cụm, chỉ những cụm này; None = mọi cụm)
    ("GUMBO_POT", r"nồi gang", None),
    ("BLUE_RIM_BOWL", r"bát sứ trắng viền xanh", None),
    ("BURGUNDY_BAG", r"túi xách da đỏ rượu", {1, 2, 3}),
    ("BLACK_BAG", r"túi xách MỚI|túi xách mới|túi đen bóng", None),
    ("FLIP_PHONE", r"nắp gập", None),
    ("LOUISIANA_FRAME", r"khung ảnh", {11, 32}),
    ("LOUISIANA_FRAME_NEW", r"kính đã thay", None),
    ("CANVAS_SUITCASE", r"vali vải|vali nâu", None),
    ("KRAFT_ENVELOPE", r"phong bì giấy kraft|phong bì giấy nâu", None),
    ("GATE_KEYS", r"chùm chìa khoá đồng", None),
    ("PROPOSAL", r"kẹp gáy nhựa đen", None),
    ("HOSPITAL_BADGE", r"thẻ đeo cũ|thẻ bệnh viện cũ", None),
    ("GOLD_WATCH", r"đồng hồ nữ vàng|hộp nhung", None),
    ("LIVESTREAM_RIG", r"tay cầm chống rung", None),
    ("RECIPE_CARD", r"tờ công thức", None),
    ("EIGHT_ENVELOPES", r"tám phong bì", None),
    ("DESK_BOX", r"thùng giấy", {47, 48}),
]


def parse(kb):
    L = kb.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    cl, cur, mode = [], None, "head"
    for ln in L:
        m = re.match(r"^CỤM (\d+) — (.*)$", ln)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "head": [], "shots": [], "ket": [], "moc": "", "raw": [ln]}
            cl.append(cur); mode = "head"; continue
        if cur is None:
            continue
        if re.match(r"^-{50,}$", ln):
            cur = None; continue
        cur["raw"].append(ln)
        if ln.startswith("KẾT:"):
            mode = "ket"; cur["ket"].append(ln[4:].strip()); continue
        if ln.startswith("MÓC:"):
            cur["moc"] = ln[4:].strip(); mode = "moc"; continue
        s = re.match(r"^\[\s*(\d+)–(\d+)\s?s\]\s+(.+?)\s+—\s+(.*)$", ln)
        if s:
            mode = "shot"
            cur["shots"].append({"a": int(s.group(1)), "b": int(s.group(2)), "co": s.group(3), "hinh": s.group(4),
                                 "noi": "", "thoai": ""})
            continue
        d = re.match(r"^ {10}([^\s:][^:]{0,40}?): (.*)$", ln)
        if d and mode == "shot":
            nhan = d.group(1).strip()
            assert nhan in TEN, (cur["n"], nhan)
            assert not cur["shots"][-1]["thoai"], (cur["n"], "hai câu thoại một shot")
            cur["shots"][-1]["noi"] = TEN[nhan]; cur["shots"][-1]["thoai"] = d.group(2).strip(); continue
        if mode == "head":
            cur["head"].append(ln)
        elif mode == "shot" and ln.strip():
            cur["shots"][-1]["hinh"] += " " + ln.strip()
        elif mode == "ket" and ln.strip():
            cur["ket"].append(ln.strip())
        elif mode == "moc" and ln.strip():
            cur["moc"] += " " + ln.strip()
    return cl


def nap_bang():
    """{tên bảng: {panels, cum}} từ bible bối cảnh (scratchpad boi_canh_{A,B,C}.json đã chép vào _zh/data/boi_canh_*.json)."""
    ra = {}
    for f in sorted(DATA.glob("boi_canh_*.json")):
        for ten, b in json.loads(f.read_text(encoding="utf-8")).items():
            ra[ten] = {"panels": b["panels"], "cum": set(b.get("cum") or [])}
    ra["LAUNDRY"] = {"panels": ["LOC_LAUNDRY_NIGHT"], "cum": {10}}
    return ra


# Nơi chính của cụm khi nhiều bảng cùng ghi một cụm (cụm chuyển cảnh / biến thể): thứ tự = thứ tự xuất hiện trong cụm
THU_TU = {
    3: ["BOWIE_HOUSE_DAY_BANG", "BOWIE_FRONT_DAY_BANG"], 10: ["BOWIE_PARTY_NIGHT_BANG", "LAUNDRY", "BOWIE_FRONT_NIGHT_BANG"],
    18: ["BOWIE_HOUSE_MESSY_BANG", "BOWIE_FRONT_DAY_BANG"], 20: ["BOWIE_HOUSE_MESSY_BANG", "BOWIE_FRONT_DAY_BANG"],
    26: ["KEYSTONE_CONF_BANG", "GROCERY_BANG"], 42: ["LOT7_FOYER_BANG", "LOT7_EXT_THU_BANG"],
    43: ["LOT7_FOYER_BANG", "LOT7_EXT_THU_BANG", "SALES_OFFICE_BANG"], 44: ["BOWIE_HOUSE_NIGHT_BANG", "KEYSTONE_CONF_NIGHT_BANG"],
    47: ["KEYSTONE_CONF_BANG", "KEYSTONE_FLOOR_BANG"], 48: ["BOWIE_HOUSE_MESSY_BANG", "BOWIE_FRONT_DAY_BANG"],
    49: ["LOT7_FOYER_BANG", "LOT7_EXT_THU_BANG"], 50: ["BOWIE_FRONT_SNOW_BANG", "CHARLENE_APT_BANG"],
    51: ["CHARLENE_APT_BANG", "LOT7_FOYER_BANG"], 66: ["LOT7_FOYER_BANG"], 68: ["LOT7_FOYER_BANG", "LOT7_EXT_CHIEU_BANG", "LOT7_DINING_BANG"],
}


def main():
    cl = parse(KB)
    assert [c["n"] for c in cl] == list(range(1, 71)), [c["n"] for c in cl][:5]
    BANG = nap_bang()
    du_f = DUAN / "du_an.json"
    du = json.loads(du_f.read_text(encoding="utf-8"))
    bible_cl, du_cum, canh_bao = [], [], []
    for c in cl:
        n = c["n"]
        head = c["head"]
        loc = next((x for x in head if x.strip()), "")
        cast_line = next((x for x in head if x.startswith("Nhân vật:")), "")
        cast = []
        for t in re.split(r"\s*·\s*", cast_line.replace("Nhân vật:", "").strip()):
            t = re.sub(r"\(.*?\)", "", t).strip()
            if t:
                assert t in TEN, (n, t)
                if TEN[t] not in cast:
                    cast.append(TEN[t])
        for s in c["shots"]:
            if s["noi"] and s["noi"] not in cast:
                cast.append(s["noi"]); canh_bao.append(f"cụm {n}: {s['noi']} nói mà không có ở dòng Nhân vật")
        if n == 4 and "PEARL" not in cast:
            cast.append("PEARL")            # tiệc: Sister Pearl ở ghế thứ tư (C4, toàn cảnh) — có ảnh SP1
        boards = THU_TU.get(n) or [b for b, v in BANG.items() if n in v["cum"]]
        for b in boards:
            assert b in BANG, (n, b)
        if not boards:
            canh_bao.append(f"cụm {n}: KHÔNG có bảng bối cảnh nào")
        text = " ".join(s["hinh"] for s in c["shots"]) + " " + " ".join(c["ket"])
        props = [p for p, pat, ds in PROP_LUAT if (ds is None or n in ds) and re.search(pat, text)]
        noi_ds = []
        for s in c["shots"]:
            if s["noi"] and s["noi"] not in noi_ds:
                noi_ds.append(s["noi"])
        ca = [t for t in noi_ds if t in cast] + [t for t in cast if t not in noi_ds]
        con = max(0, 9 - len(ca) - min(2, len(props)))
        panels = []
        if boards:
            chinh = BANG[boards[0]]["panels"]
            phu = [p for b in boards[1:] for p in BANG[b]["panels"][:2]]
            panels = (chinh[:max(2, con - len(phu))] + phu)[:max(con, 2)]
        props_gui = props[:max(0, 9 - len(ca) - len(panels))][:2]
        refs = panels + [sheet_cua(t, n) for t in ca] + ["PROP_" + p for p in props_gui]
        if len(refs) > 9:
            canh_bao.append(f"cụm {n}: {len(refs)} ảnh > 9 — người viết phải bớt panel ({refs})")
        shots = [{"t": f"{s['a']}-{s['b']}", "a": s["a"], "b": s["b"], "co": s["co"], "hinh": s["hinh"], "noi": s["noi"],
                  "thoai": s["thoai"]} for s in c["shots"]]
        assert shots[0]["a"] == 0 and shots[-1]["b"] == 30 and all(shots[i]["b"] == shots[i + 1]["a"] for i in range(len(shots) - 1)), n
        bible_cl.append({"n": n, "title": c["title"], "loc": loc, "head": head, "cast": cast, "cast_gui": ca,
                         "bo_khung": ["DAU", "GIUA", "CUOI"], "shots": shots, "refs": refs, "boards": boards,
                         "props_tim_thay": props, "end_state": " ".join(c["ket"]), "moc": c["moc"],
                         "raw": "\n".join(c["raw"])})
        du_cum.append({"n": n, "boi_canh": boards[0] if boards else "", "am_thanh": "",
                       "tinh_than": " ".join(x.strip() for x in head if x.startswith("Tinh")),
                       "bat_dau": c["shots"][0]["hinh"][:300], "ket_thuc": " ".join(c["ket"]), "truoc_do": "",
                       "do": {t: sheet_cua(t, n).split("_")[-1] for t in ca},
                       "shots": [{"a": float(s["a"]), "b": float(s["b"]), "co": s["co"].upper(), "ai": "",
                                  "hinh": "" if s["thoai"] else s["hinh"], "noi": s["noi"], "thoai": s["thoai"]}
                                 for s in c["shots"]], "refs": refs})
    # tên ảnh: nv / boi_canh / dao_cu
    tm = {}
    for ten, v in du["nhan_vat"].items():
        for ma in v["do"]:
            ma = ma.split("<")[0].strip()
            tm[f"SHEET_{ten}_{ma}"] = {"loai": "nv", "ten": ten}
    for b, v in BANG.items():
        for p in v["panels"]:
            tm[p] = {"loai": "boi_canh", "ten": p}
    for p in du["dao_cu"]:
        tm["PROP_" + p] = {"loai": "dao_cu", "ten": "PROP_" + p}
    (DUAN / "anh" / "_ten_anh.json").write_text(json.dumps(tm, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in bible_cl:
        for r in c["refs"]:
            assert r in tm and (DUAN / "anh" / f"{r}.png").exists(), (c["n"], r)
    chars = sorted({t for c in bible_cl for t in c["cast"]})
    bible = {"meta": {"name": "EAT IN THE KITCHEN"}, "characters": [{"name": t} for t in chars], "clusters": bible_cl}
    (DUAN / "bible.json").write_text(json.dumps(bible, ensure_ascii=False, indent=1), encoding="utf-8")
    du["cum"] = du_cum
    du_f.write_text(json.dumps(du, ensure_ascii=False, indent=1), encoding="utf-8")
    print("cụm:", len(bible_cl), "| ảnh/cụm tối đa:", max(len(c["refs"]) for c in bible_cl),
          "| thoại:", sum(1 for c in bible_cl for s in c["shots"] if s["thoai"]))
    for x in canh_bao:
        print("  !", x)


if __name__ == "__main__":
    main()
