# -*- coding: utf-8 -*-
"""Lập danh sách dựng (EDL): mỗi cụm giữ đoạn [vao, ra] — cắt phần lặng dư ở đầu (cảnh mở lặp lại trạng thái cuối cụm trước) và
phần đuôi dài dòng sau câu thoại cuối; đặt kiểu chuyển cảnh; dóng từng câu thoại kịch bản vào mốc nghe được để làm phụ đề.
Đọc _zh/dung/phan_tich/cum_NNN.json (phan_tich_dung.py). Ghi _zh/dung/edl.json + edl.md.
Chạy: python -X utf8 lap_dung.py"""
import difflib, json, re
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
D = DUAN / "_zh" / "dung"
B = {c["n"]: c for c in json.loads((DUAN / "bible.json").read_text(encoding="utf-8"))["clusters"]}

DUOI_TOI_DA = 2.4        # giữ tối đa bấy nhiêu giây sau chữ cuối (phản ứng), trong cùng một cảnh
DUOI_HET_CANH = 3.6      # cụm cuối một cảnh / trước hồi tưởng: thở dài hơn trước khi chuyển
DAU_TOI_DA = 1.6         # mở cụm nối tiếp cùng cảnh: tối đa bấy nhiêu giây trước chữ đầu
DAU_DOI_CANH = 3.2       # cụm mở cảnh mới: giữ cảnh mở dài hơn
DEM_TU = 0.30            # không cắt sát chữ hơn
DOI_CANH_TAY = {44}       # loc ghi 'NHÀ → PHÒNG HỌP' nhưng shot cuối C44 quay lại bếp nhà Devin -> C44→C45 là đổi cảnh
RA_TAY = {56: 26.4}       # chỉnh tay sau khi xem dải hình điểm nối: C56 giữ nhịp Devin khép cửa (cú máy liền, không có điểm cắt)


def _noi(t):
    t = re.sub(r"\s+", " ", t).strip()
    m = re.match(r"(.*?)\s*\(([^)]*)\)?$", t)
    return (m.group(1).strip(), m.group(2).strip()) if m and "(" in t else (t, "")


def canh(n, cuoi=False):
    """Nơi lúc mở (cuoi=False) hoặc lúc kết (cuoi=True) của cụm n — loc dạng 'A (NGÀY)  →  B (NGÀY)'."""
    phan = B[n]["loc"].split("→")
    return _noi(phan[-1] if cuoi else phan[0])


def doi_canh(a, b):
    """True nếu nơi kết của cụm a khác nơi mở của cụm b (thiếu ghi giờ ở một bên thì coi như cùng giờ)."""
    if a is None or b is None or a not in B or b not in B:
        return True
    if a in DOI_CANH_TAY and b == a + 1:
        return True
    (la, ga), (lb, gb) = canh(a, True), canh(b)
    return la != lb or bool(ga and gb and ga != gb)


_ANH = {}


def anh_nho(f, t):
    """Khung xám 64x36 tại giây t (để đo độ giống hình)."""
    import subprocess
    import numpy as np
    k = (f, round(t, 2))
    if k not in _ANH:
        r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(max(0, t)), "-i", f, "-frames:v", "1",
                            "-vf", "scale=64:36,format=gray", "-f", "rawvideo", "-"], capture_output=True)
        _ANH[k] = np.frombuffer(r.stdout, dtype=np.uint8).astype(float)
    return _ANH[k]


def giong(f1, t1, f2, t2):
    import numpy as np
    a, b = anh_nho(f1, t1), anh_nho(f2, t2)
    if a.size != 2304 or b.size != 2304 or a.std() < 1 or b.std() < 1:
        return 0.0
    return float(np.corrcoef(a, b)[0, 1])


def tok(s):
    s = s.lower().replace("’", "'")
    return re.findall(r"[a-z0-9']+", s)


def dong_cau(n, tu):
    """Dóng từng câu thoại kịch bản vào chuỗi từ whisper -> [(shot, câu, đầu, cuối | None)]."""
    cau = [(i, s["thoai"].strip()) for i, s in enumerate(B[n]["shots"]) if s["thoai"].strip()]
    kb, vi = [], []
    for k, (_, c) in enumerate(cau):
        for w in tok(c):
            kb.append(w); vi.append(k)
    wn = [tok(w["w"]) for w in tu]
    flat, idx = [], []
    for j, ws in enumerate(wn):
        for w in ws:
            flat.append(w); idx.append(j)
    sm = difflib.SequenceMatcher(None, kb, flat, autojunk=False)
    gan = {}
    for a, b2, size in sm.get_matching_blocks():
        for t in range(size):
            gan.setdefault(vi[a + t], []).append(idx[b2 + t])
    kq = []
    for k, (i, c) in enumerate(cau):
        js = gan.get(k)
        n_tu = len(tok(c))
        if js and len(set(js)) >= max(1, min(2, n_tu)):
            kq.append([i, c, tu[min(js)]["a"], tu[max(js)]["b"]])
        else:
            kq.append([i, c, None, None])
    # câu không dóng được: nội suy theo mốc shot kịch bản, kẹp giữa câu trước/sau
    for k, x in enumerate(kq):
        if x[2] is None:
            s = B[n]["shots"][x[0]]
            a, b2 = float(s["a"]), float(s["b"])
            truoc = max([y[3] for y in kq[:k] if y[3] is not None] or [0])
            sau = min([y[2] for y in kq[k + 1:] if y[2] is not None] or [30])
            a = max(a, truoc + 0.1); b2 = min(b2, sau - 0.1)
            x[2], x[3] = round(a, 2), round(max(a + 1.0, b2), 2)
            x.append("noi_suy")
    return kq


def dung_hinh(p, f):
    """Các đoạn hình gần như đứng yên (freezedetect n=0.005, ≥0,5s), gộp đoạn sát nhau; lưu tạm vào file phân tích."""
    if "dung_hinh" not in p:
        import subprocess
        e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p["file"], "-vf", "freezedetect=n=0.005:d=0.5", "-an", "-f", "null", "-"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
        st = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", e)]
        en = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", e)]
        en += [p["dai"]] * (len(st) - len(en))
        gop = []
        for a, b in zip(st, en):
            if gop and a - gop[-1][1] < 0.15:
                gop[-1][1] = b
            else:
                gop.append([a, b])
        p["dung_hinh"] = [[round(a, 2), round(b, 2)] for a, b in gop]
        f.write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
    return p["dung_hinh"]


edl, md = [], ["# EDL — EAT IN THE KITCHEN", "", "| cụm | giữ | bỏ đầu | bỏ đuôi | chuyển vào | ghi chú |", "|---|---|---|---|---|---|"]
tong_goc = tong_moi = 0.0
for n in range(1, 71):
    p = json.loads((D / "phan_tich" / f"cum_{n:03d}.json").read_text(encoding="utf-8"))
    dai, cuts = p["dai"], p["cat_canh"]
    cau = dong_cau(n, p["tu"])
    dau_noi = min(x[2] for x in cau) if cau else None
    cuoi_noi = max(x[3] for x in cau) if cau else None
    ghi = []
    moi_canh = doi_canh(n - 1, n)
    het_canh = doi_canh(n, n + 1)
    # ĐẦU
    # Cảnh lặng mở đầu cụm là nhịp kể chuyện viết sẵn (insert, người bước vào, màn chiếu…) -> giữ. Chỉ bỏ shot chớp < 1,2s ở đầu
    # khi cụm nối tiếp cùng cảnh (khung lặp trạng thái cuối cụm trước) và chưa có thoại trong shot đó.
    vao = 0.0
    if n > 1 and not moi_canh and cuts and cuts[0] < 1.2 and (dau_noi is None or cuts[0] <= dau_noi - DEM_TU):
        vao = cuts[0]
        ghi.append(f"bỏ shot chớp {vao:.1f}s lặp cụm trước")
    vao = round(vao, 2)
    # ĐUÔI
    if n == 70 or cuoi_noi is None:
        ra = dai
    else:
        toi_da = DUOI_HET_CANH if het_canh else DUOI_TOI_DA
        ra = cuoi_noi + toi_da
        # shot cuối (móc của cụm) bắt đầu sau chữ cuối -> luôn cho thấy nó ≥ 1,6s (≥ 2,5s nếu hết cảnh), chỉ cắt phần ngâm dài
        shot_cuoi = max([c for c in cuts if c > cuoi_noi] or [0])
        if shot_cuoi:
            ra = max(ra, shot_cuoi + (2.5 if het_canh else 1.6))
        ra = min(dai, ra)
        # đuôi trùng điểm móc cụm sau (cùng cảnh): Seedance luôn mở cụm sau bằng một shot dựng lại đúng tư thế đó ở góc khác
        # (đo tương quan khung: không giống về hình mà trùng về nội dung). Sau chữ cuối đã có một shot phản ứng ≥ 2s thì shot
        # cuối chỉ là ngâm lặp lại -> bỏ hẳn; còn lại chỉ giữ nhịp móc 1,4s của nó.
        if not het_canh and shot_cuoi:
            if shot_cuoi - cuoi_noi >= 2.0:
                # các shot nằm giữa chữ cuối và shot cuối là nhịp kể viết sẵn (insert còng tay, tờ kết quả, mở cửa…) -> giữ
                # trọn; chỉ shot giữa nào ngâm > 3s mới cắt còn 2,4s
                giua = [c for c in cuts if cuoi_noi < c < shot_cuoi]
                ra2 = shot_cuoi
                if giua and shot_cuoi - giua[-1] > 3.0:
                    ra2 = giua[-1] + 2.4
                elif not giua and shot_cuoi - cuoi_noi > 3.0:
                    ra2 = cuoi_noi + DUOI_TOI_DA
                ra2 = min(ra, ra2)
                ghi.append(f"bỏ shot cuối {dai - shot_cuoi:.1f}s trùng mở cụm sau")
            else:
                ra2 = min(ra, shot_cuoi + 1.4)
            ra = max(ra2, cuoi_noi + 0.9)
        # đuôi đứng hình (cả khung bất động tới điểm ra) -> chỉ giữ 0,8s của nó (1,2s nếu hết cảnh)
        for a, b in dung_hinh(p, D / "phan_tich" / f"cum_{n:03d}.json"):
            if b >= ra - 0.1 and a < ra and a > cuoi_noi:
                ra2 = max(cuoi_noi + 0.7, a + (1.2 if het_canh else 0.8))
                if ra2 < ra - 0.3:
                    ghi.append(f"bỏ {ra - ra2:.1f}s đứng hình")
                    ra = ra2
                break
        ra = round(min(dai, max(ra, cuoi_noi + DEM_TU + 0.25)), 2)
        if n in RA_TAY:
            ghi.append(f"điểm ra chỉnh tay {RA_TAY[n]:.1f}s (máy tính {ra:.1f}s)")
            ra = RA_TAY[n]
        if dai - ra > 0.3:
            ghi.append(f"cắt đuôi {dai - ra:.1f}s")
    chuyen = "mo_den" if n == 1 else ("den" if moi_canh else "cat")
    edl.append({"cum": n, "file": p["file"], "dai": dai, "vao": vao, "ra": ra, "chuyen_vao": chuyen,
                "het_canh": het_canh, "cau": cau})
    tong_goc += dai; tong_moi += ra - vao
    md.append(f"| {n} | {vao:.2f}–{ra:.2f} ({ra - vao:.1f}s) | {vao:.1f} | {dai - ra:.1f} | {chuyen} | {'; '.join(ghi)}"
              + ("; " + str(sum(1 for x in cau if len(x) > 4)) + " câu nội suy" if any(len(x) > 4 for x in cau) else "") + " |")
md += ["", f"Tổng gốc {tong_goc / 60:.1f} phút → sau cắt {tong_moi / 60:.1f} phút (bỏ {(tong_goc - tong_moi) / 60:.1f} phút)."]
(D / "edl.json").write_text(json.dumps(edl, ensure_ascii=False, indent=1), encoding="utf-8")
(D / "edl.md").write_text("\n".join(md), encoding="utf-8")
print(md[-1])
