# -*- coding: utf-8 -*-
"""QC gối đầu: với mỗi cụm đã có video mới — whisper cả clip (qc_run.py → qc/qc.json + qc/cum_NNN.jpg), so mờ từng câu thoại
kịch bản; câu nào chưa khớp thì cắt đúng khoảng giây của shot đó (±1 s) cho whisper nghe lại riêng (câu hét / câu ngắn hay bị
bỏ khi nghe cả clip). In một dòng kết luận mỗi cụm; KHÔNG ghi qc-ghi (người chấm xem tấm khung hình rồi ghi).
Dùng: python -X utf8 qc_lan.py <cụm…>"""
import difflib, json, os, re, subprocess, sys, tempfile
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
TOOL = Path(r"F:\Tungnd\bigup_xuong_phim_1.0.23")
sys.path.insert(0, str(Path(__file__).parent))
env = dict(os.environ, PYTHONUTF8="1")
BIBLE = {c["n"]: c for c in json.loads((DUAN / "bible.json").read_text(encoding="utf-8"))["clusters"]}


_U = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_T = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()


def _chu(k):
    if k < 20: return _U[k]
    if k < 100: return _T[k // 10] + ((" " + _U[k % 10]) if k % 10 else "")
    if k < 1000: return _U[k // 100] + " hundred" + ((" " + _chu(k % 100)) if k % 100 else "")
    if k < 1000000: return _chu(k // 1000) + " thousand" + ((" " + _chu(k % 1000)) if k % 1000 else "")
    if k < 10 ** 9: return _chu(k // 1000000) + " million" + ((" " + _chu(k % 1000000)) if k % 1000000 else "")
    return str(k)


def _so(m):
    t = m.group(0)
    k = int(re.sub(r"[^\d]", "", t))
    return " " + _chu(k) + (" dollars " if t.startswith("$") else " ")


def chuan(s):
    s = s.lower().replace("’", "'").replace("-", " ")
    s = s.replace("é", "e").replace("è", "e").replace("ç", "c").replace("à", "a")
    s = re.sub(r"\$?\d{1,3}(?:,\d{3})+|\$?\d+", _so, s)
    return re.sub(r"[^a-z0-9' ]", " ", s).split()


def diem(cau, nghe):
    cw, hw = chuan(cau), chuan(" ".join(nghe))
    cs, best = "".join(cw), 0.0
    for L in range(max(1, len(cw) - 2), len(cw) + 3):
        for i in range(0, max(0, len(hw) - L) + 1):
            win = hw[i:i + L]
            best = max(best, difflib.SequenceMatcher(None, cw, win).ratio(),
                       difflib.SequenceMatcher(None, cs, "".join(win)).ratio())
    return best


_m = None


def nghe_doan(f, a, b, lang=None):
    global _m
    from faster_whisper import WhisperModel
    _m = _m or WhisperModel("small", device="cpu", compute_type="int8")
    tmp = Path(tempfile.gettempdir()) / "qc_doan.wav"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", str(max(0, a - 1)), "-t", str(b - a + 2),
                    "-i", str(f), "-ac", "1", "-ar", "16000", str(tmp)], check=True)
    seg, _ = _m.transcribe(str(tmp), beam_size=5, vad_filter=False, language=lang)
    return [s.text.strip() for s in seg]


def main():
    cums = [int(x) for x in sys.argv[1:] if x.isdigit()]
    r = subprocess.run([sys.executable, "-X", "utf8", str(Path(__file__).parent / "qc_run.py")] + [str(n) for n in cums],
                       capture_output=True, text=True, encoding="utf-8", env=env, cwd=str(TOOL))
    if r.returncode:
        print("qc_run lỗi:", (r.stderr or "")[-600:])
    qc = {x.get("cum"): x for x in json.loads((DUAN / "qc" / "qc.json").read_text(encoding="utf-8"))}
    for n in cums:
        k = qc.get(n, {})
        f = DUAN / str(k.get("file", ""))
        nghe = k.get("cau_nghe_duoc") or []
        thieu = []
        for s in BIBLE[n]["shots"]:
            if not s["thoai"].strip():
                continue
            d = diem(s["thoai"], nghe)
            if d < 0.75 and f.exists():
                d = max(d, diem(s["thoai"], nghe_doan(f, s["a"], s["b"])))
                if d < 0.75:
                    d = max(d, diem(s["thoai"], nghe_doan(f, s["a"], s["b"], "fr")))
            if d < 0.75:
                thieu.append(f"[{s['t']}] {s['noi']}: {s['thoai']} ({d:.2f})")
        tong = sum(1 for s in BIBLE[n]["shots"] if s["thoai"].strip())
        print(f"cụm {n}: thoại {tong - len(thieu)}/{tong}, {k.get('giay')}s, tiếng Trung {bool(k.get('co_chu_han'))}, "
              f"ảnh qc/cum_{n:03d}.jpg" + (" | THIẾU: " + " · ".join(thieu) if thieu else ""))


if __name__ == "__main__":
    main()
