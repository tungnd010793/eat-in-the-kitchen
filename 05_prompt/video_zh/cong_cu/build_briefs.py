# -*- coding: utf-8 -*-
"""Dữ liệu cho bước viết tay 70 bài tiếng Trung của EAT IN THE KITCHEN:
(1) _zh/anh_tham_chieu.json + _zh/nguoi_nen.json từ câu chuẩn _zh/data/*.json (viết theo ảnh thật);
(2) tấm ghép ảnh gửi có nhãn @图片N: _zh/soat/anh_gui/cum_NNN.jpg;
(3) brief từng cụm: _zh/brief/cum_NNN.md (ảnh gửi, câu chuẩn có sẵn, kịch bản cụm, KẾT cụm trước, MỞ cụm sau).
Đọc refs từ du_an.json["cum"] (đã gộp refs_moi nếu có). Chạy: python -X utf8 build_briefs.py [cụm…]
"""
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DUAN = Path(r"F:\Tungnd\phim\EAT_IN_THE_KITCHEN")
ZH = DUAN / "_zh"
DATA = ZH / "data"
TU_DO = Path(r"F:\Tungnd\Github\eat-in-the-kitchen\05_prompt\ghi-chu-dung\tu-do-nhan-vat.md")
LOOK_ZH = "中性白平衡，白色干净不偏黄，暖意只来自画面里看得见的灯和窗边光，色彩自然温润，中等对比，暗部有细节，面部明亮清楚，色温、光影、亮度参考场景图"
CAU_CHOT = ("所有人的眼白都干净，不发红；所有人都是正常人眼，眼睛不发光；每个人的肤色深浅与各自人物图一致，深棕皮肤自然不泛灰、不油亮，保留自然肤质；"
            + LOOK_ZH + "，不过度锐化。整体ARRI Alexa 35电影感，变形宽银幕构图，真实景深，细腻35mm颗粒，自然眨眼与呼吸，16:9。无字幕、无背景音乐、无配乐、无旁白。")
SO = "一两三四五六七八九十"


def doc(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def nap():
    bang = {}
    for f in ("panels_A.json", "panels_C.json"):
        bang.update(doc(DATA / f))
    nv = {"nhan_dien": {}, "trang_phuc": {}, "lay_phan": {}, "ghi_chu": {}, "prop": {}}
    for f in ("nhan_vat_chinh.json", "phu_dao_cu.json"):
        d = doc(DATA / f)
        for k in nv:
            nv[k].update(d.get(k) or {})
    return bang, nv


def bang_cua_panel(bang):
    ra = {}
    for b, v in bang.items():
        ps = list(v["panels"])
        for k, p in enumerate(ps):
            ra[p] = (b, k, ps)
    return ra


def doi_dien(p, ps):
    if len(ps) != 4:
        return None
    return ps[(ps.index(p) + 2) % 4]


def ghep(n, refs, tm):
    rong, cot = 640, 3
    o = []
    for i, r in enumerate(refs, 1):
        im = Image.open(DUAN / "anh" / f"{r}.png").convert("RGB")
        im = im.resize((rong, round(im.height * rong / im.width)))
        o.append((f"@图片{i}  {r}", im))
    cao = max(im.height for _, im in o) + 30
    hang = (len(o) + cot - 1) // cot
    tam = Image.new("RGB", (cot * rong, hang * cao), "white")
    ve = ImageDraw.Draw(tam)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 22)
    except OSError:
        font = ImageFont.load_default()
    for i, (t, im) in enumerate(o):
        x, y = (i % cot) * rong, (i // cot) * cao
        tam.paste(im, (x, y + 30))
        ve.text((x + 6, y + 4), t, fill="black", font=font)
    f = ZH / "soat" / "anh_gui" / f"cum_{n:03d}.jpg"
    f.parent.mkdir(parents=True, exist_ok=True)
    tam.save(f, quality=85)
    return f


def main():
    chi = {int(x) for x in sys.argv[1:]}
    bang, nv = nap()
    pb = bang_cua_panel(bang)
    tm = doc(DUAN / "anh" / "_ten_anh.json")
    b = doc(DUAN / "bible.json")
    du = doc(DUAN / "du_an.json")
    refs_cum = {c["n"]: c["refs"] for c in du["cum"]}
    cl = {c["n"]: c for c in b["clusters"]}

    # (1) anh_tham_chieu.json + nguoi_nen.json
    atc = {}
    for p, (bg, k, ps) in pb.items():
        atc[p] = {"loai": "boi_canh", "bang": bg, "noi": bang[bg]["noi"], "mo_ta": bang[bg]["panels"][p]}
    for r, v in tm.items():
        if v["loai"] == "nv":
            atc[r] = {"loai": "nv", "ten": v["ten"], "nhan_dien": nv["nhan_dien"].get(v["ten"], ""),
                      "trang_phuc": nv["trang_phuc"].get(r, ""), "lay_phan": nv["lay_phan"].get(r, "")}
        elif v["loai"] == "dao_cu":
            atc[r] = {"loai": "dao_cu", "mo_ta": nv["prop"].get(r, "")}
    (ZH / "anh_tham_chieu.json").write_text(json.dumps(atc, ensure_ascii=False, indent=1), encoding="utf-8")
    (ZH / "nguoi_nen.json").write_text(json.dumps({bg: v["nguoi_nen"] for bg, v in bang.items()}, ensure_ascii=False,
                                                  indent=1), encoding="utf-8")
    thieu = [r for r in {x for rs in refs_cum.values() for x in rs} if r not in atc or not (atc[r].get("mo_ta") or atc[r].get("trang_phuc"))]
    if thieu:
        print("! thiếu câu chuẩn:", sorted(thieu))

    # (2)(3) tấm ghép + brief
    for n in sorted(cl):
        if chi and n not in chi:
            continue
        c, refs = cl[n], refs_cum[n]
        f_ghep = ghep(n, refs, tm)
        ma = {r: i for i, r in enumerate(refs, 1)}

        def ten_ma(r):
            v = tm[r]
            return f"{v['ten']}（@图片{ma[r]}）" if r in ma else v["ten"]

        L = [f"# CỤM {n} — {c['title']}", "",
             f"Nơi (kịch bản): {c['loc']}   |   bảng: {', '.join(c['boards'])}   |   cast kịch bản: {', '.join(c['cast'])}",
             f"Tấm ghép ảnh gửi (có nhãn @图片N, MỞ BẰNG Read): `{f_ghep}`", "",
             "## Ảnh gửi mặc định — thứ tự = @图片N (thêm / bớt PANEL: QUY_CHUAN_VIET.md mục 7)"]
        for r in refs:
            v = tm[r]
            if v["loai"] == "boi_canh" and r in pb:
                bg, k, ps = pb[r]
                dd = doi_dien(r, ps)
                L.append(f"- @图片{ma[r]}  {r}  (panel bảng {bg}, ô {k + 1}" +
                         (f"; panel ĐỐI DIỆN = {dd}: {'CÓ' if dd in ma else 'KHÔNG'} gửi)" if dd else ")"))
            elif v["loai"] == "nv":
                L.append(f"- @图片{ma[r]}  {v['ten']}  (nhân vật, ảnh `{r}.png`, bộ đồ {r.split('_')[-1]})")
            else:
                L.append(f"- @图片{ma[r]}  {r}  (đạo cụ)")
        con = [p for p in c.get("props_tim_thay", []) if "PROP_" + p not in ma]
        if con:
            L.append(f"- Đạo cụ kịch bản nhắc mà CHƯA gửi (thêm nếu là đồ then chốt và còn chỗ ≤ 9): {', '.join('PROP_' + p for p in con)}")
        L += ["", "## CÂU CHUẨN — chép NGUYÊN VĂN, gắn mã `（@图片N）` đúng số ở trên khi chép vào bài", ""]
        for bg in c["boards"]:
            v = bang[bg]
            L.append(f"### Nơi `{bg}` — tên nơi: {v['noi']}")
            for p, cau in v["panels"].items():
                L.append(f"- {p}{'（@图片' + str(ma[p]) + '）' if p in ma else '  [KHÔNG GỬI]'}：{cau}")
            if v.get("phuong_vi"):
                L.append(f"- câu phương vị: {v['phuong_vi']}")
            L.append(f"- người nền mặc định (chỉnh số lượng / vị trí theo kịch bản cụm): {v['nguoi_nen']}")
            L.append("")
        nvs = [r for r in refs if tm[r]["loai"] == "nv"]
        if nvs:
            L.append(f"### Nhân vật — câu mở: 【人物参考图】{SO[len(nvs) - 1]}张浅灰色纯色背景的人物图，每张左边是一个人的脸部特写，右边是同一个人的全身照，只用来认人和确定服装，不要照搬它们的构图和姿势：")
            for r in nvs:
                t = tm[r]["ten"]
                L.append(f"- {t}（@图片{ma[r]}）：{nv['nhan_dien'].get(t, '??')}。")
                L.append(f"  - trang phục ({r}): {nv['trang_phuc'].get(r, '??')}")
                if nv["lay_phan"].get(r):
                    L.append(f"  - câu lấy phần (ngay dưới dòng nhận diện): {nv['lay_phan'][r].replace('{T}', t).replace('{N}', str(ma[r]))}")
            L.append("")
        pr = [r for r in refs if tm[r]["loai"] == "dao_cu"]
        if pr:
            L.append(f"### Đạo cụ — câu mở: 【道具图】{SO[len(pr) - 1]}张浅灰色纯色背景的道具图，只用来认道具的样子，画面里不要出现灰色背景：")
            for r in pr:
                L.append(f"- {r}（@图片{ma[r]}）：{nv['prop'].get(r, '??')}。")
            L.append("")
        L += ["### Câu chốt [保持不变] (chép y hệt, từ 所有人的眼白都干净 tới hết)", CAU_CHOT, ""]
        gc = [f"- {t}: " + " · ".join(nv["ghi_chu"].get(t, [])) for t in c["cast"] if nv["ghi_chu"].get(t)]
        if gc:
            L += ["## Ghi chú liên tục nhân vật"] + gc + [""]
        fr = [s for s in c["shots"] if s["thoai"] and re.search(r"\b(Elle|vous|Non, non|Je vais|Qui a|Et la)\b", s["thoai"])]
        if fr:
            L += ["## Thoại TIẾNG PHÁP trong cụm (QUY_CHUAN mục 3a)"] + [f"- [{s['t']}秒] {s['noi']}: {{{s['thoai']}}}" for s in fr] + [""]
        if n > 1:
            L += [f"## KẾT cụm trước ({n - 1}) = vị trí mở cụm này nếu cụm nối liền", cl[n - 1]["end_state"], ""]
        L += [f"## KỊCH BẢN CỤM {n} (nguyên văn 04_kich-ban-chinh-thuc.md)", "```", c["raw"], "```", ""]
        if n < 70:
            nx = cl[n + 1]
            L += [f"## MỞ cụm sau ({n + 1}) — KẾT của cụm này phải nối được vào đây", nx["loc"],
                  next((x for x in nx["head"] if x.startswith("Nhân vật")), ""), f"[{nx['shots'][0]['t']}s] {nx['shots'][0]['hinh']}", ""]
        f = ZH / "brief" / f"cum_{n:03d}.md"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("\n".join(L), encoding="utf-8")
    print("xong brief + tấm ghép")


if __name__ == "__main__":
    main()
