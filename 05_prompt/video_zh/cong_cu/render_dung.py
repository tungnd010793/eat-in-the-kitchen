# -*- coding: utf-8 -*-
"""Dựng phim theo _zh/dung/edl.json.
  bước 1 (tung_cum): mỗi cụm cắt [vao, ra], nâng 1920x1080 (lanczos + làm nét nhẹ), 24 fps, cân tiếng về -16 LUFS theo số đo QC,
          mờ đen 0,35s khi đổi cảnh/hồi tưởng, vuốt tiếng 40–60 ms ở mối nối để không lụp bụp -> _zh/dung/tg/cum_NNN.mkv
  bước 2 (ghep): nối thẳng (video copy, không nén lại lần hai), tiếng AAC 256k qua bộ giới hạn đỉnh -1 dBTP
          -> xuat/EAT_IN_THE_KITCHEN_FULLHD.mp4 ; ghi _zh/dung/moc_cum.json (mốc đầu từng cụm trong phim, để làm phụ đề)
Chạy: python -X utf8 render_dung.py [tung_cum|ghep|tat_ca] [cụm…]"""
import json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
D = DUAN / "_zh" / "dung"
TG = D / "tg"; TG.mkdir(exist_ok=True)
XUAT = DUAN / "xuat"; XUAT.mkdir(exist_ok=True)
EDL = json.loads((D / "edl.json").read_text(encoding="utf-8"))
LUFS = {r["cum"]: r.get("lufs") for r in json.loads((DUAN / "qc" / "qc.json").read_text(encoding="utf-8"))}
MUC = -16.0
DEN = 0.35
FPS = 24
# sửa hình lúc dựng: cụm -> [(giây đầu, giây cuối theo file gốc, x, y, rộng, cao theo tỉ lệ khung gốc)] = phóng cận vùng đó trong
# khoảng giây ấy (che lỗi dàn cảnh mà không mất câu thoại). Đọc _zh/dung/sua_hinh.json nếu có.
SUA = {int(k): v for k, v in (json.loads((D / "sua_hinh.json").read_text(encoding="utf-8")) if (D / "sua_hinh.json").exists() else {}).items()}


def do_dai(f):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f)], capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", e)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def mot(e):
    n = e["cum"]
    ra_f = TG / f"cum_{n:03d}.mov"
    so_khung = round((e["ra"] - e["vao"]) * FPS)
    dai = so_khung / FPS
    vf = ["fps=24", "scale=1920:1080:flags=lanczos", "unsharp=5:5:0.35:5:5:0", "format=yuv420p", "setsar=1"]
    af = ["aresample=48000"]
    l = LUFS.get(n)
    if isinstance(l, (int, float)):
        af.append(f"volume={round(MUC - l, 2)}dB")
    vao_den = e["chuyen_vao"] in ("den", "mo_den")
    ra_den = e["het_canh"] or n == 70
    if vao_den:
        vf.append(f"fade=t=in:st=0:d={DEN if n > 1 else 0.8}")
    if ra_den:
        d_ra = 1.2 if n == 70 else DEN
        vf.append(f"fade=t=out:st={dai - d_ra:.3f}:d={d_ra}")
    af.append(f"afade=t=in:st=0:d={0.25 if vao_den else 0.04}")
    af.append(f"afade=t=out:st={dai - (0.3 if ra_den else 0.06):.3f}:d={0.3 if ra_den else 0.06}")
    loc_v = ["-vf", ",".join(vf)]
    if SUA.get(n):
        # mỗi đoạn sửa: crop vùng (tỉ lệ) rồi phủ lên đúng khoảng giây; giây tính theo file đã -ss nên trừ vao
        g = ["[0:v]scale=1920:1080:flags=lanczos,setsar=1[g0]"]
        for i, (a, b, x, y, w, h) in enumerate(SUA[n]):
            a, b = a - e["vao"], b - e["vao"]
            g.append(f"[0:v]crop=iw*{w}:ih*{h}:iw*{x}:ih*{y},scale=1920:1080:flags=lanczos,setsar=1[z{i}]")
            g.append(f"[g{i}][z{i}]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'[g{i + 1}]")
        g.append(f"[g{len(SUA[n])}]" + ",".join(x for x in vf if not x.startswith("scale=")) + "[v]")
        loc_v = ["-filter_complex", ";".join(g), "-map", "[v]", "-map", "0:a"]
    cmd = ["ffmpeg", "-hide_banner", "-y", "-ss", f"{e['vao']:.3f}", "-i", e["file"], "-frames:v", str(so_khung), "-t", f"{dai:.3f}",
           *loc_v, "-af", ",".join(af), "-c:v", "h264_nvenc", "-preset", "p7", "-tune", "hq", "-rc", "vbr",
           "-cq", "17", "-b:v", "0", "-maxrate", "30M", "-bufsize", "60M", "-profile:v", "high", "-bf", "3",
           "-spatial-aq", "1", "-temporal-aq", "1", "-pix_fmt", "yuv420p", "-g", "48", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", str(ra_f)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return n, r.returncode, (r.stderr or "")[-300:] if r.returncode else ""


def tung_cum(ds):
    with ThreadPoolExecutor(3) as ex:
        for n, rc, err in ex.map(mot, [e for e in EDL if not ds or e["cum"] in ds]):
            print(f"cụm {n}: {'xong' if rc == 0 else 'LỖI ' + err}", flush=True)


def ghep():
    ds = TG / "danh_sach.txt"
    ds.write_text("\n".join(f"file 'cum_{e['cum']:03d}.mov'" for e in EDL), encoding="utf-8")
    moc, t = {}, 0.0
    for e in EDL:
        moc[e["cum"]] = {"bat_dau": round(t, 3), "vao": e["vao"], "dai": round(do_dai(TG / f"cum_{e['cum']:03d}.mov"), 3)}
        t += moc[e["cum"]]["dai"]
    (D / "moc_cum.json").write_text(json.dumps(moc, ensure_ascii=False, indent=1), encoding="utf-8")
    ra = XUAT / "EAT_IN_THE_KITCHEN_FULLHD.mp4"
    # chuẩn hoá tiếng 2 lượt về -14 LUFS (YouTube), đỉnh thật ≤ -1,5 dBTP
    do = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "concat", "-safe", "0", "-i", str(ds), "-vn",
                         "-af", "loudnorm=I=-14:TP=-1.5:LRA=16:print_format=json", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(TG)).stderr
    j = json.loads(do[do.rindex("{"):do.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=16:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
          f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    print("đo tiếng:", j["input_i"], "LUFS, đỉnh", j["input_tp"], flush=True)
    cmd = ["ffmpeg", "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(ds), "-c:v", "copy",
           "-af", ln + ",aresample=48000", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", str(ra)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(TG))
    print("ghép:", "xong" if r.returncode == 0 else "LỖI " + (r.stderr or "")[-400:], ra, f"{t / 60:.2f} phút", flush=True)


if __name__ == "__main__":
    buoc = sys.argv[1] if len(sys.argv) > 1 else "tat_ca"
    cums = [int(x) for x in sys.argv[2:] if x.isdigit()]
    if buoc in ("tung_cum", "tat_ca"):
        tung_cum(cums)
    if buoc in ("ghep", "tat_ca"):
        ghep()
