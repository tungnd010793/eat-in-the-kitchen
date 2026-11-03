# -*- coding: utf-8 -*-
"""QC MỘT cụm vừa render lại: chạy qc_run.py (whisper + tấm khung hình), rồi soát toàn bộ bản nghe với thoại của chính cụm đó
(cùng bộ soát mờ của qc_loop.py). Khác qc_loop: LUÔN nghe lại bản mới nhất (qc_loop bỏ qua nếu tên file mp4 trùng bản cũ).
Chạy: python -X utf8 qc_check.py <cụm> [--ghi]   (--ghi: nếu đạt thì qc-ghi --dat)"""
import difflib, json, os, re, subprocess, sys
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
TOOL = Path(r"F:\Tungnd\bigup_xuong_phim_1.0.23")
env = dict(os.environ, PYTHONUTF8="1")
n = int([a for a in sys.argv[1:] if a.isdigit()][0])
GHI = "--ghi" in sys.argv
BIBLE = {c["n"]: c for c in json.loads((DUAN / "bible.json").read_text(encoding="utf-8"))["clusters"]}

_U = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_T = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()


def _chu(k):
    if k < 20: return _U[k]
    if k < 100: return _T[k // 10] + ((" " + _U[k % 10]) if k % 10 else "")
    if k < 1000: return _U[k // 100] + " hundred" + ((" " + _chu(k % 100)) if k % 100 else "")
    if k < 1000000: return _chu(k // 1000) + " thousand" + ((" " + _chu(k % 1000)) if k % 1000 else "")
    return str(k)


def _so(m):
    t = m.group(0)
    k = int(re.sub(r"[^\d]", "", t))
    if "," not in t and not t.startswith("$") and 1100 <= k <= 2099 and k % 100:
        return " " + _chu(k // 100) + " " + _chu(k % 100) + " "
    return " " + _chu(k) + (" dollars " if t.startswith("$") else " ")


def chuan(s):
    s = s.lower().replace("’", "'").replace("-", " ")
    s = re.sub(r"(\d+)\s*ds\b", r"\1 days", s)
    s = re.sub(r"\$?\d{1,3}(?:,\d{3})+|\$?\d+", _so, s)
    return re.sub(r"[^a-z0-9' ]", " ", s).split()


def soat_lai(nghe):
    can = [s["thoai"] for s in BIBLE[n]["shots"] if s["thoai"].strip()]
    hw = chuan(" ".join(nghe))
    thieu, vt, tu, dat = [], [], 0, []
    for c in can:
        cw = chuan(c); cs = "".join(cw); best, bi = 0.0, -1
        for L in range(max(1, len(cw) - 2), len(cw) + 3):
            for i in range(tu, max(tu, len(hw) - L) + 1):
                win = hw[i:i + L]
                r = max(difflib.SequenceMatcher(None, cw, win).ratio(), difflib.SequenceMatcher(None, cs, "".join(win)).ratio())
                if r > best: best, bi = r, i
        if best >= 0.75:
            vt.append(bi); tu = bi; dat.append((round(best, 2), c))
        else:
            thieu.append((round(best, 2), c))
    return can, dat, thieu, vt != sorted(vt)


r = subprocess.run([sys.executable, "-X", "utf8", str(Path(__file__).parent / "qc_run.py"), str(n)],
                   capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(TOOL))
print((r.stdout or "")[-1500:])
if r.returncode:
    print("qc_run lỗi:", (r.stderr or "")[-400:])
k = next((x for x in json.loads((DUAN / "qc" / "qc.json").read_text(encoding="utf-8")) if x.get("cum") == n), {})
st = json.loads((DUAN / "video" / "_trang_thai.json").read_text(encoding="utf-8")).get(str(n), {})
print("file render:", st.get("file"), "| file QC:", k.get("file"))
nghe = k.get("cau_nghe_duoc") or []
print("NGHE ĐƯỢC:")
for x in nghe: print("   ·", x)
can, dat, thieu, sai_tt = soat_lai(nghe)
print(f"KỊCH BẢN CỤM {n}: {len(can)} câu thoại; khớp {len(dat)}; thiếu {len(thieu)}; sai thứ tự {sai_tt}; tiếng Trung {bool(k.get('co_chu_han'))}; "
      f"{k.get('giay')}s; LUFS {k.get('lufs')}; tool: {k.get('trang_thai')}")
for s, c in dat: print(f"   ✓ {s}  {c}")
for s, c in thieu: print(f"   ✗ {s}  {c}")
ok = not thieu and not sai_tt and not k.get("co_chu_han")
print("KẾT LUẬN:", "ĐẠT" if ok else "CHƯA ĐẠT")
if ok and GHI and str(k.get("trang_thai")) != "ĐẠT":
    subprocess.run([sys.executable, "-X", "utf8", str(TOOL / "xuong.py"), "--du-an", str(DUAN), "qc-ghi", str(n), "--dat",
                    "--ghi", "nghe đủ thoại theo kịch bản của chính cụm (render lại, soát toàn bản nghe)"],
                   capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(TOOL), timeout=120)
    print("đã qc-ghi --dat")
