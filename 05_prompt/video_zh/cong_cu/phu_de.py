# -*- coding: utf-8 -*-
"""Phụ đề tiếng Việt + bản nhẹ để QC.
  - mốc từng câu: _zh/dung/edl.json (câu kịch bản đã dóng vào mốc nghe được) + _zh/dung/moc_cum.json (đầu từng cụm trong phim)
  - lời Việt: _zh/dung/sub_vi.json (theo chỉ số shot)
  - ra: xuat/EAT_IN_THE_KITCHEN_VI.srt, _zh/dung/qc_vi.ass (phụ đề + nhãn "Cụm NN" góc trái trên để báo lỗi theo cụm),
        xuat/EAT_IN_THE_KITCHEN_QC_720p_SUB_VI.mp4 (720p, nhẹ, phụ đề in cứng)
Chạy: python -X utf8 phu_de.py [--khong-render]"""
import json, subprocess, sys
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
D = DUAN / "_zh" / "dung"
XUAT = DUAN / "xuat"
EDL = json.loads((D / "edl.json").read_text(encoding="utf-8"))
MOC = {int(k): v for k, v in json.loads((D / "moc_cum.json").read_text(encoding="utf-8")).items()}
VI = json.loads((D / "sub_vi.json").read_text(encoding="utf-8"))

dong = []      # (đầu, cuối, chữ, cụm)
thieu = []
for e in EDL:
    n = e["cum"]; m = MOC[n]
    vi = {x["shot"]: x["vi"] for x in VI.get(str(n), [])}
    for x in e["cau"]:
        shot, _, a, b = x[:4]
        t = vi.get(shot)
        if not t:
            thieu.append((n, shot)); continue
        dau = m["bat_dau"] + (a - e["vao"]) - 0.05
        cuoi = m["bat_dau"] + (b - e["vao"]) + 0.35
        dau = max(dau, m["bat_dau"]); cuoi = min(cuoi, m["bat_dau"] + m["dai"] - 0.05)
        if cuoi - dau < 0.3:
            continue
        dong.append([dau, cuoi, t, n])
dong.sort()
for i, d in enumerate(dong):          # tối thiểu 1,0s; không đè câu sau
    d[1] = max(d[1], d[0] + 1.0)
    if i + 1 < len(dong):
        d[1] = min(d[1], dong[i + 1][0] - 0.04)


def srt_t(s):
    ms = round(s * 1000); h, ms = divmod(ms, 3600000); mi, ms = divmod(ms, 60000); se, ms = divmod(ms, 1000)
    return f"{h:02d}:{mi:02d}:{se:02d},{ms:03d}"


def ass_t(s):
    cs = round(s * 100); h, cs = divmod(cs, 360000); mi, cs = divmod(cs, 6000); se, cs = divmod(cs, 100)
    return f"{h}:{mi:02d}:{se:02d}.{cs:02d}"


XUAT.mkdir(exist_ok=True)
(XUAT / "EAT_IN_THE_KITCHEN_VI.srt").write_text(
    "\n".join(f"{i}\n{srt_t(a)} --> {srt_t(b)}\n{t}\n" for i, (a, b, t, _) in enumerate(dong, 1)), encoding="utf-8-sig")

ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1280", "PlayResY: 720", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
       "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Sub,Arial,40,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,2.6,1.2,2,60,60,38,1",
       "Style: Nhan,Arial,22,&H00B4FFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,3,0,0,7,14,14,12,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for e in EDL:
    m = MOC[e["cum"]]
    ass.append(f"Dialogue: 1,{ass_t(m['bat_dau'])},{ass_t(m['bat_dau'] + m['dai'])},Nhan,,0,0,0,,Cụm {e['cum']:02d}")
XUONG = "\\N"     # xuống dòng trong ASS
for a, b, t, _ in dong:
    ass.append(f"Dialogue: 0,{ass_t(a)},{ass_t(b)},Sub,,0,0,0,,{t.replace(chr(10), XUONG)}")
(D / "qc_vi.ass").write_text("\n".join(ass), encoding="utf-8-sig")
print(f"{len(dong)} câu phụ đề; thiếu lời Việt: {thieu}")

if "--khong-render" not in sys.argv:
    ra = XUAT / "EAT_IN_THE_KITCHEN_QC_720p_SUB_VI.mp4"
    cmd = ["ffmpeg", "-hide_banner", "-y", "-i", str(XUAT / "EAT_IN_THE_KITCHEN_FULLHD.mp4"),
           "-vf", "scale=1280:720:flags=bicubic,ass=qc_vi.ass", "-c:v", "libx264", "-preset", "veryfast", "-crf", "27",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-ac", "2", "-movflags", "+faststart", str(ra)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(D))
    print("bản QC:", "xong" if r.returncode == 0 else "LỖI " + (r.stderr or "")[-500:], ra)
