# -*- coding: utf-8 -*-
"""Chạy QC của tool (loi.qc.soat) cho vài cụm, nhưng thay MỘT lệnh ffprobe (độ dài file) bằng ffmpeg vì máy chưa có ffprobe.
Không sửa tool; chỉ vá trong tiến trình này. Dùng: python -X utf8 qc_run.py <cụm…>"""
import re, subprocess, sys
from pathlib import Path

TOOL = Path(r"F:\Tungnd\bigup_xuong_phim_1.0.23")
DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
sys.path.insert(0, str(TOOL))
_run = subprocess.run


def _duration(path):
    r = _run(["ffmpeg", "-hide_banner", "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", (r.stderr or "") + (r.stdout or ""))
    return (int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))) if m else 0.0


def run(args, *a, **k):
    if isinstance(args, (list, tuple)) and args and args[0] == "ffprobe" and "format=duration" in " ".join(map(str, args)):
        return subprocess.CompletedProcess(args, 0, stdout=f"{_duration(args[-1]):.3f}\n", stderr="")
    return _run(args, *a, **k)


subprocess.run = run
from loi import qc as qc_mod  # noqa: E402
import xuong  # noqa: E402

cums = [int(x) for x in sys.argv[1:] if x.isdigit()]
duan = DUAN
da = xuong._nap(duan)
qc_mod.soat(duan, da, cums or None)
