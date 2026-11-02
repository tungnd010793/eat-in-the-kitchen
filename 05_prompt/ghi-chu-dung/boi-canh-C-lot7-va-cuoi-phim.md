> Claude soạn ngày 02/11/2026 khi đọc trọn 70 cụm để dựng ảnh. Số dòng dạng (L123) hay "dòng 123" tính từ dòng `## KỊCH BẢN CHI TIẾT 70 CỤM` của `03_kich-ban-chinh-sua.md` (dòng 490 của file đó là L1); cộng 489 để ra số dòng trong 03.

# Bối cảnh nhóm C — bảng 4 góc · EAT IN THE KITCHEN

Nguồn: `kb.txt` (kịch bản chi tiết 70 cụm, bản 1 — 02/11/2026). Đã đọc trọn từng dòng: C42, C43 (0–16 s), C49, C50 (13–30 s), C51, C52–C70; đọc thêm C1–C3, C37–C41 để kiểm mã và lai lịch căn nhà Lot 7.
Tool: `bang_4_goc.py` — panel k nhìn thẳng tường k; tường bên PHẢI máy = k+1, bên TRÁI = k−1, sau lưng = k+2 (mod 4).
Luật đời thực: `14_doi_song_that_black_america.md` mục 1.1, 2, 3, 4, 4.1, 5 (5.6, 5.7), 6, 12. Ánh sáng: `05_prompt/00_LOOK_MAU.md` (cân trắng ánh ngày trung tính, ấm chỉ từ đèn nhìn thấy, mid-key).
File máy đọc: `boi_canh_C.json` (cùng thư mục). Script dựng + kiểm: `tools_C/build_boi_canh_C.py`.

---

## 0. Tóm tắt — 12 bảng

| # | Bảng | Nơi | Trạng thái | Vẽ từ | Panel 1 · 2 · 3 · 4 (= tường 1 · 2 · 3 · 4) | Cụm |
|---|---|---|---|---|---|---|
| 1 | `LOT7_FOYER_BANG` | Lot 7 — sảnh hai tầng + phòng làm việc | ngày | — | LOT7_FOYER_DOORS · LOT7_STAIRS · LOT7_FOYER_ARCH · LOT7_WORK | 42, 43 (0–16 s), 49, 51 (21–30 s), 66, 68 |
| 2 | `LOT7_DINING_BANG` | Lot 7 — phòng ăn | chiều (nắng thấp) | — | LOT7_DINING_ARCH · LOT7_DINING_WINDOWS · LOT7_DINING_KITCHEN · LOT7_DINING_BUFFET | 68 (27–30 s), 69, 70 |
| 3 | `LOT7_EXT_BANG` | Lot 7 — trước nhà, tháng Giêng | tuyết | — | LOT7_EXT_HOUSE · LOT7_EXT_EAST · **LOT7_EXT** · LOT7_EXT_WEST | 57–62 |
| 4 | `LOT7_EXT_THU_BANG` | Lot 7 — trước nhà, tháng Mười | thu | LOT7_EXT_BANG | LOT7_EXT_OCT_HOUSE · LOT7_EXT_OCT_EAST · LOT7_EXT_OCT · LOT7_EXT_OCT_WEST | 42, 43, 49 (nhìn qua cửa mở) |
| 5 | `LOT7_EXT_CHIEU_BANG` | Lot 7 — trước nhà, cuối tháng Chín | chiều | LOT7_EXT_BANG | LOT7_EXT_SEP_HOUSE · LOT7_EXT_SEP_EAST · LOT7_EXT_SEP · LOT7_EXT_SEP_WEST | 68 (khuyến nghị) |
| 6 | `CHARLENE_APT_BANG` | Căn hộ Charlene | ngày | — | CHARLENE_KITCHEN · CHARLENE_WINDOW · CHARLENE_DOOR · CHARLENE_SOFA | 50 (13–30 s), 51 (0–21 s) |
| 7 | `CHARLENE_APT_DEM_BANG` | Căn hộ Charlene | đêm | CHARLENE_APT_BANG | CHARLENE_KITCHEN_NIGHT · CHARLENE_WINDOW_NIGHT · CHARLENE_DOOR_NIGHT · CHARLENE_SOFA_NIGHT | 56 |
| 8 | `HOSP_BANG` | Phòng bệnh đơn | ngày | — | HOSP_BED · HOSP_WINDOW · HOSP_DOOR · HOSP_CHAIR | 52–55 |
| 9 | `COURT_HALL_BANG` | Hành lang toà Upper Marlboro | ngày | — | COURT_DOORS · COURT_HALL_EAST · COURT_WINDOWS · COURT_HALL_WEST | 63 |
| 10 | `CHURCH_HALL_BANG` | Hội trường hầm nhà thờ Baptist | ngày | — | **CHURCH_HALL** · CHURCH_HALL_TABLES · CHURCH_HALL_OUT · CHURCH_HALL_EXIT | 64 |
| 11 | `WAREHOUSE_BANG` | Kho phân phối | ngày | — | **WAREHOUSE** · WAREHOUSE_DOCK · WAREHOUSE_BREAK · WAREHOUSE_CONVEYOR | 65 |
| 12 | `DEVIN_STUDIO_BANG` | Phòng studio thuê của Devin | đêm | — | **DEVIN_STUDIO** · DEVIN_STUDIO_BED · DEVIN_STUDIO_DOOR · DEVIN_STUDIO_TABLE | 67 |

In đậm là mã có sẵn trong dòng KẾT của kịch bản, dùng lại cho panel khớp nhất. **Không dùng `FOYER_STAIRS`**: mã này đã có trong kịch bản nhưng là sảnh **nhà Devin ở Bowie** (KẾT C1, C2, C3), không phải Lot 7. **Không dùng `LOT7_IN` làm tên panel**: kịch bản dùng nó cho cả góc làm việc (KẾT C66) lẫn phòng ăn (KẾT C68, C69, C70), nên đã tách thành các panel `LOT7_*` riêng.

## 1. Quy ước

- `tuong` theo chiều kim đồng hồ nhìn từ trên xuống. La bàn Bắc/Đông/Nam/Tây trong file này chỉ là công cụ suy luận; chỉ ghi vào câu ánh sáng khi cần nói hướng nắng ("west windows", "south windows").
- Cú qua vai: "máy đặt sau vai PHẢI X" thì vai X nằm ở mép TRÁI khung, vì máy đứng bên phải X nên X ở bên trái máy. Kịch bản viết đúng luật này ở mọi chỗ đã kiểm (C49 2–5 s, C57 8–10 s, C58 26–30 s, C54 2–5 s).
- Chuỗi `tuong` viết chữ thường đầu câu, không có dấu chấm cuối, vì `prompt_mac_dinh()` chèn nó vào giữa câu ("the far wall is …; on the LEFT-HAND side …"). Đã chạy thử `prompt_mac_dinh()` cho cả 12 bảng: không còn ".;" hoặc "..".
- Kiểm chữ: dùng regex `TU_CHI_NGUOI` của `export_kich_ban_md.py`, cộng danh sách cấm của brief (người, thân thể, quần áo, chữ showroom, chữ phong cách, đồ Công giáo). Kết quả **0 lỗi**. Lần quét chuỗi con chỉ bắt được "chandelier", vì nó chứa chuỗi "hand"; regex ranh giới từ của tool không cắt từ này. Mọi chữ, số, biển, giấy tờ, màn hình đều ghi "blank / no lettering / dark".
- Số từ mỗi `tuong`: 27–47 (hai chuỗi 46–47 từ). Mỗi tường có 3–6 món.

---

## 2. LOT 7 — TRONG NHÀ (`LOT7_FOYER_BANG`, `LOT7_DINING_BANG`)

Lai lịch (C37–C41): Inès tặng bà căn nhà của cô ở Mitchellville, đã sang tên bà; bà nhận với điều kiện trả dần. Bà nhận chìa khoá ngày 10/10/2026 tại văn phòng bán hàng của khu có cổng (lô 12 vẫn còn đang bán).

### 2.1 Bằng chứng — vị trí máy và hướng nhìn

| Cụm · giây | Câu kịch bản | Ghi nhận |
|---|---|---|
| C42 0–2 | "Máy đặt giữa sảnh nhìn về cửa đôi" … "ngoài cửa: bậc thềm đá và cây lá vàng tháng Mười" | cửa đôi; ngoài trời tháng 10 |
| C42 2–4 | "Máy đặt trong ngưỡng cửa nhìn vào phòng ăn" … "nắng chéo qua cửa sổ cao rọi lên tóc muối tiêu"; vai Raven "tiền cảnh mép phải" | cửa đôi ↔ phòng ăn đối diện; có cửa sổ cao |
| C42 4–7 | "Máy đặt giữa sảnh nhìn về cửa đôi" … Raven "ngửa cổ nhìn lên đèn chùm lớn và cầu thang cong"; bảo vệ "đứng ở ngưỡng cửa sau lưng họ" | đèn chùm, cầu thang cong |
| C42 16–25 | "Máy nhìn vào phòng ăn" (cận bà) | |
| C42 KẾT | "Máy đặt giữa sảnh nhìn về cửa đôi … Marguerite … đứng giữa sảnh, lưng về phòng ăn" | trục cửa ↔ phòng ăn |
| C43 0–16 | "Máy đặt giữa sảnh nhìn về cửa đôi" / "Máy nhìn vào phòng ăn" / "qua khung cửa đôi đang mở … xuống bậc thềm đá, dưới hàng cây lá vàng tháng Mười" | ngoài trời tháng 10 qua cửa mở |
| C49 0–2 | "Máy đặt trong sảnh, chếch về phía góc làm việc, nhìn về cửa đôi" … "qua khung cửa là bậc thềm đá, lối xe vòng lát đá có chiếc sedan xám …, cổng sắt đen để mở ở cuối lối xe, hàng cây sồi lá vàng tháng Mười, nắng trưa" | góc làm việc nằm một bên sảnh |
| C49 2–5 | "Máy đặt sau vai phải bà trong sảnh nhìn ra cửa" — vai bà "mờ ở mép trái khung" | |
| C49 8–11, 16–21 | "Máy đặt ngoài ngưỡng … nhìn vào trong" — "bàn ăn óc chó mờ xa sau lưng bà" | trục cửa ↔ phòng ăn |
| C49 27–30, KẾT | "sau ô kính cửa là hai bóng người mờ" | cửa đôi có ô kính |
| C51 21–30 | "máy nhìn về góc làm việc nhà Lot 7" … "ngồi sau bàn gỗ", "kệ từ điển sau lưng", "kéo ngăn kéo bàn gỗ", "măng tô len kem vắt trên lưng ghế" | bàn quay ra, kệ sau lưng |
| C66 0–2 | "Máy đặt phía phòng khách nhìn về góc làm việc" — "khung ảnh gỗ nhỏ — ảnh căn nhà gỗ sơn vàng nhạt có hiên trước ở Louisiana" ở góc bàn | |
| C66 2–5 | "Máy đặt sau bàn nhìn về phòng khách" — người xin việc "trên ghế đối diện bàn" | ngược 180° |
| C66 15–19 | "Máy nhìn về phòng khách" — tay áo bà "ở mép phải khung"; người xin việc "đi về phía sảnh, ra khỏi mép trái khung" | **sảnh ở TRÁI khi nhìn từ bàn ra** |
| C66 19–23 | "Máy đặt ở phía sảnh nhìn về phòng ăn" — Inès "đứng tựa khung cửa vòm phòng ăn … nhìn sang phía góc làm việc (ngoài khung bên phải)" | **góc làm việc ở PHẢI khi nhìn vào phòng ăn** |
| C66 23–27 | "Máy nhìn về góc làm việc" — bà "quay mặt từ phía Inès sang phía sảnh và cửa đôi (ngoài khung bên phải)" | **cửa đôi ở PHẢI khi nhìn góc làm việc** |
| C68 0–2 | "Máy đặt trong sảnh, chếch về phía phòng khách, nhìn về cửa đôi" — "qua khung cửa là lối xe lát đá, hàng cây sồi xanh đậm và nắng chiều thấp vàng" | ngoài trời tháng 9 |
| C68 2–27 | "Máy trong sảnh nhìn ra cửa" / "Máy đặt ngoài ngưỡng nhìn vào" — "nắng chiều sau lưng anh" | |
| C68 27–30, KẾT | "xoay chậm … về phía cửa vòm phòng ăn: … bàn ăn óc chó bày MỘT bộ bát đĩa sứ trắng viền xanh ở đầu bàn, bình hoa cúc vàng; nắng thấp xiên vàng" · "tủ buffet gỗ óc chó và tủ bát kính ở tường bên; lối vào bếp ở cuối phòng ăn" | đồ của phòng ăn |
| C69 0–3 | "Máy đặt ở góc phòng ăn nhìn về cửa vòm" — Devin "đứng cạnh đầu bàn …, lưng về phía cửa vòm"; bà đi "tới tủ buffet gỗ óc chó ở tường bên, kéo một ngăn kéo" | đầu bàn ở phía cửa vòm |
| C69 5–15 | "Máy đặt sau đầu bàn nhìn về tủ buffet" / "Máy nhìn về tủ buffet" | |
| C69 27–30 | "Devin liếc về phía lối vào bếp ở cuối phòng ăn — thấy một góc đảo bếp đá trắng" | |
| C70 0–8 | "Máy đặt ở lối vào bếp nhìn về bàn ăn" / "Máy nhìn về bàn ăn" | ngược của cửa vòm |
| C70 14–20 | "Máy đặt ở góc phòng ăn nhìn về đầu bàn" — bà lấy bát "từ tủ bát kính ở tường bên" | |
| C70 26–30 | "Máy đặt ở góc phòng ăn cạnh cửa vòm, nhìn dọc bàn về phía bếp" — hai mẹ con "ở đầu bàn … gần máy", "nắng chiều thấp vàng chiếu xiên qua phòng; lối vào bếp trống ở cuối phòng" | khung cuối phim |

### 2.2 Đồ cố định
Sảnh: cửa đôi gỗ có ô kính, cửa sổ cao (vòm) trên cửa, đèn chùm lớn, cầu thang cong, bậc thềm đá ngay ngoài cửa.
Góc làm việc: bàn gỗ có ngăn kéo, ghế có lưng (vắt măng tô), kệ từ điển sau lưng bàn, khung ảnh căn nhà vàng ở góc bàn, ghế đối diện bàn (đồ di động).
Phòng ăn: cửa vòm, bàn ăn gỗ óc chó dài (đầu bàn ở phía cửa vòm), tủ buffet óc chó và tủ bát kính (cùng một tường bên), lối vào bếp ở cuối phòng (có đảo bếp đá trắng), nắng thấp chiếu xiên.

### 2.3 Suy bố cục — vì sao hai bảng trong nhà
1. **Cửa đôi ↔ phòng ăn đối diện nhau** (C42 2–4, C42 KẾT, C49 16–21). Đặt cửa đôi ở Nam, cửa vòm phòng ăn ở Bắc. Mặt tiền nhìn về Nam khớp ánh sáng: lúc 11:20 tháng Mười, nắng rọi chéo qua cửa sổ vòm trên cửa (C42 "nắng chéo qua cửa sổ cao"); C49 ngoài cửa là "nắng trưa".
2. **Nhìn vào phòng ăn thì góc làm việc ở bên phải** (C66 19–23). Nhìn về Bắc thì bên phải là Đông, nên góc làm việc ở phía Đông. Khớp với C49 0–2 và C68 0–2: máy "chếch về phía góc làm việc / phòng khách" khi nhìn cửa đôi.
3. **Nhìn góc làm việc thì cửa đôi ở bên phải** (C66 23–27). Cho bàn quay mặt về Tây, ra sảnh, lưng tựa tường Đông có kệ từ điển. Khi đó máy nhìn về Đông, bên phải là Nam, đúng phía cửa đôi.
4. **Ngồi sau bàn nhìn "phòng khách" thì sảnh ở bên trái** (C66 15–19). Máy nhìn về Tây, bên trái là Nam, nên người xin việc đi về phía cửa đôi và ra khỏi mép trái.
5. **Cầu thang** chỉ còn chỗ ở tường Tây. Trong panel nhìn cửa đôi, cầu thang nằm ở mép phải, nên C42 4–7 Raven ngửa nhìn được cả đèn chùm lẫn cầu thang.
6. **Phòng ăn** (bảng riêng): cửa vòm ở Nam; lối vào bếp ở Bắc ("cuối phòng ăn"); buffet và tủ bát kính ở tường Đông ("tường bên"); cửa sổ ở Tây. Lúc 17:30 ngày 26/9 ở Maryland, mặt trời ở hướng tây – tây nam, cao khoảng 15°, nên nắng thấp vào qua cửa sổ Tây và "chiếu xiên qua phòng". Nhìn cửa vòm thì nắng đến từ phải; nhìn về bếp thì nắng đến từ trái.

**Số bảng — chọn 2:**
- *Không chọn 3 bảng* (sảnh, phòng khách có góc làm việc, phòng ăn). Phương án phụ cũng thoả mọi trái/phải: bàn quay Bắc, lưng tựa tường mặt tiền, "phòng khách" là phòng riêng ở phía Đông. Nhưng phương án đó cần thêm một bảng chỉ để phục vụ 3 cú ngược của C66 (2–5, 7–10, 15–19 s). Phương án đã chọn là một phòng làm việc nhỏ mở thẳng ra sảnh qua khoảng mở rộng. "Phòng khách" khi nhìn từ bàn ra chính là phía sảnh đối diện: cầu thang cùng đôi ghế kem và bàn tròn. Một bảng phủ cả sảnh lẫn góc làm việc mà vẫn đúng mọi chiều.
- *Không gộp thành 1 bảng*: phòng ăn có đủ 4 hướng được dùng (cửa vòm, buffet, bếp, cửa sổ đón nắng) và có trạng thái ánh sáng riêng là nắng thấp cuối chiều.
- Cửa đôi lắp **kính vân mờ**; cửa sổ vòm chỉ thấy trời; cửa sổ phòng làm việc và phòng ăn có **rèm voan**. Nhờ vậy bảng trong nhà không khoá mùa và dùng được cho cả tháng 10, tháng 1 và tháng 9. Cảnh trời ngoài cửa mở lấy từ bảng ngoài nhà đúng mùa (mục 3).

### 2.4 Bảng ánh xạ

| Câu kịch bản | Cụm · giây | Panel |
|---|---|---|
| "Máy đặt giữa sảnh nhìn về cửa đôi" / "Cùng hướng" | C42 0–2, 4–16, 25–30; C43 0–5, 8–16 | LOT7_FOYER_DOORS (+ LOT7_EXT_OCT khi cửa mở) |
| "Máy đặt trong ngưỡng cửa nhìn vào phòng ăn" / "Máy nhìn vào phòng ăn" | C42 2–4, 16–25; C43 5–8 | LOT7_FOYER_ARCH |
| "Máy đặt trong sảnh, chếch về phía góc làm việc, nhìn về cửa đôi" | C49 0–2 | LOT7_FOYER_DOORS + LOT7_EXT_OCT |
| "Máy đặt sau vai phải bà trong sảnh nhìn ra cửa" / "Máy trong sảnh nhìn ra cửa" | C49 2–8, 11–16 | LOT7_FOYER_DOORS + LOT7_EXT_OCT |
| "Máy đặt ngoài ngưỡng … nhìn vào trong" / "Máy ngoài ngưỡng nhìn vào" | C49 8–11, 16–21 | LOT7_FOYER_ARCH (khung cửa + bậc thềm: LOT7_EXT_OCT_HOUSE) |
| "Máy đặt thấp ngang ngực bà, chếch bên, nhìn lên" | C49 21–24 | LOT7_FOYER_ARCH (nền trần, đèn chùm) |
| "Máy trong sảnh nhìn về cửa đôi" / "máy chếch bên" | C49 24–30 | LOT7_FOYER_DOORS |
| "máy nhìn về góc làm việc nhà Lot 7" | C51 21–30 | LOT7_WORK |
| "Máy đặt phía phòng khách nhìn về góc làm việc" / "Máy nhìn về góc làm việc" | C66 0–2, 5–7, 10–15, 23–30 | LOT7_WORK |
| "Máy đặt sau bàn nhìn về phòng khách" / "Máy nhìn về phòng khách" | C66 2–5, 7–10, 15–19 | LOT7_STAIRS |
| "Máy đặt ở phía sảnh nhìn về phòng ăn" | C66 19–23 | LOT7_FOYER_ARCH |
| "Máy đặt trong sảnh, chếch về phía phòng khách, nhìn về cửa đôi" / "Máy trong sảnh nhìn ra cửa" | C68 0–6, 11–14, 17–21, 24–27 (chèn 9–11 nhấc nắp nồi: nền LOT7_EXT_SEP) | LOT7_FOYER_DOORS + LOT7_EXT_SEP |
| "Máy đặt ngoài ngưỡng nhìn vào" | C68 6–9, 14–17, 21–24 | LOT7_FOYER_ARCH (+ LOT7_EXT_SEP_HOUSE) |
| "Máy đặt giữa sảnh, xoay chậm … về phía cửa vòm phòng ăn" | C68 27–30 | LOT7_FOYER_ARCH → phòng ăn: LOT7_DINING_ARCH |
| "Máy đặt ở góc phòng ăn nhìn về cửa vòm" / "Máy nhìn về cửa vòm" | C69 0–3, 15–27; C70 23–26 | LOT7_DINING_ARCH |
| "Máy đặt sau đầu bàn nhìn về tủ buffet" / "Máy nhìn về tủ buffet" | C69 5–15 | LOT7_DINING_BUFFET |
| "Máy đặt sau đầu bàn, trượt ngang … lối vào bếp ở cuối phòng ăn" | C69 27–30 | LOT7_DINING_KITCHEN |
| "Máy đặt ở lối vào bếp nhìn về bàn ăn" / "Máy nhìn về bàn ăn" / "Máy đặt sau vai Devin nhìn về bà" | C70 0–14 | LOT7_DINING_ARCH |
| "Máy đặt ở góc phòng ăn nhìn về đầu bàn" (lấy bát từ tủ bát kính) | C70 14–20 | LOT7_DINING_ARCH + LOT7_DINING_BUFFET |
| "Máy đặt ở góc phòng ăn cạnh cửa vòm, nhìn dọc bàn về phía bếp" | C70 26–30 | LOT7_DINING_KITCHEN |
| KẾT "LOT7_IN" | C66 / C68–C70 | lần lượt LOT7_WORK / LOT7_DINING_* |

### 2.5 Bảy câu đời thực
1. **Của ai:** bà Marguerite Batiste, 66 tuổi. Bà là cựu phiên dịch tiếng Pháp, 20 năm làm ở toà án và bệnh viện (trong đó 12 năm dịch cho bác sĩ ung thư), gốc Creole Louisiana. Nhà do Inès sang tên, bà trả dần; ở từ 10/10/2026, tới C70 là gần một năm. Theo căn nhà thì đây là **tầng 3 (giàu thật)**, nhưng gu bà là "chất lượng, không phô": gỗ óc chó, kem, lanh. Nội thất nền là đồ Inès để lại (quiet luxury màu kem – lạc đà), thêm đồ riêng của bà. Tháng 9/2027 góc làm việc đã thành văn phòng phiên dịch có tuyển người.
2. **Ở đâu thật:** khu có cổng ở Mitchellville, Prince George's County, Maryland (mục 3.2: khu giàu của quận da đen giàu nhất nước). Nhà colonial gạch mới xây, có sảnh hai tầng và cầu thang cong, đúng mẫu tầng 3 ở mục 4.3.
3. **Dấu hiệu người trong cuộc:**
   - Sảnh: ảnh gia đình nhỏ đóng khung leo tường cầu thang; tranh trừu tượng lớn màu xanh rêu – đất son – nâu ("giàu nhưng có gốc": nghệ thuật thật thay cho vàng chói); ảnh căn nhà gỗ vàng ở Louisiana trên góc bàn; kệ từ điển và sách tiếng Pháp.
   - Phòng ăn: Kinh Thánh gia đình bìa da cũ kẹp chương trình tang lễ (mục 4.2); tủ bát kính đựng "bát đĩa đẹp" sứ trắng viền xanh; nồi gang, hũ bột filé và chai tương ớt trong bếp (dấu Creole, món gumbo); bát cam satsuma (Louisiana).
4. **Đồ sinh hoạt:** bát gốm đựng chìa khoá và giỏ mây trên băng ghế; xấp tài liệu dịch và đèn bàn chao lanh; bát satsuma; bình cúc vàng; một bộ bát đĩa ở đầu bàn (bà ăn một mình).
5. **Nguồn sáng:**
   - Sảnh: cửa sổ vòm trên cửa đôi, kính vân của cửa, rèm voan phòng làm việc, đèn bàn chao lanh. Đèn chùm tắt ban ngày.
   - Phòng ăn: nắng thấp cuối chiều qua cửa sổ Tây có rèm voan; hai đèn tường đồng ở cửa vòm bật. Không có ám cam toàn khung.
6. **Người nền:** không ai. Bảo vệ khu (C42–43), người xin việc và Inès (C66) đều là nhân vật.
7. **Tiếng nền:** yên. Điều hoà rì nhẹ, chim ngoài vườn, xe chạy xa. C66 có tiếng lật hồ sơ. C69–70 có tiếng muôi chạm bát sứ và máy cắt cỏ xa. Không nhạc.

**Điều sai ở nơi này:**
- Kiểu nhà phông bạt: vàng chói, nhung chần nút, gương, đèn LED dải.
- Đồ Công giáo (thánh giá có tượng, tượng thánh, chuỗi hạt, nến khấn), dù nhiều người Creole Louisiana theo Công giáo. Phim chốt Tin Lành; bà đeo thánh giá trơn nhỏ.
- Bàn console với gương tròn: đó là dấu riêng của sảnh Bowie, không lặp lại ở đây.
- Chữ đọc được trên gáy sách và tài liệu.
- Tuyết hoặc lá vàng nhìn qua cửa sổ của bảng trong nhà.
- Ám vàng toàn khung trong cảnh nắng chiều. "Nắng xiên vàng" là vệt nắng, không phải màu toàn ảnh.

### 2.6 Mâu thuẫn trong nhà
- **"Phòng khách" ở C66.** Kịch bản gọi hướng nhìn ngược từ bàn là "phòng khách". Trong bố cục đã chọn, hướng đó là phía sảnh đối diện (cầu thang và đôi ghế kem). Mọi trái/phải vẫn đúng. Nếu muốn có một phòng khách thật, chuyển sang phương án 3 bảng ở mục 2.3.
- **C68 lúc 17:30 dùng bảng sảnh vẽ ánh ngày trung tính.** Nắng thấp tả bằng chữ trong prompt và có thêm panel ngoài nhà tháng 9. Nếu render thiếu nắng, vẽ biến thể `LOT7_FOYER_CHIEU_BANG` từ bảng sảnh, chỉ đổi ánh sáng.
- **"Nắng chiều sau lưng anh" (C68).** Devin đứng ngoài cửa quay mặt về Bắc; mặt trời lúc 17:30 ở tây – tây nam, tức sau lưng chếch trái. Chấp nhận được, không cần sửa.

---

## 3. LOT 7 — NGOÀI NHÀ (`LOT7_EXT_BANG` + biến thể `_THU_`, `_CHIEU_`)

### 3.1 Bằng chứng
| Cụm · giây | Câu kịch bản | Ghi nhận |
|---|---|---|
| C57 0–2 | "Máy đặt trên lối xe, phía trong cổng, nhìn ra cổng: trời trong, lạnh, tuyết cũ đọng dọc mép cỏ; ngoài cổng sắt đang đóng, trên vỉa hè — phóng viên … ở mép trái khung …; Raven … giữa khung sát cổng …; Charlene … ở mép phải khung …; khoảng năm người hàng xóm … ở mép vỉa hè …; bà Marguerite ngoài khung, ở bậc thềm sau lưng máy" | nhìn ra: trái = phóng viên |
| C57 8–10 | "Máy đặt ngoài cổng sau vai phải Raven nhìn vào lối xe về phía nhà: … xa cuối lối xe lát đá, bà … đứng một mình ở bậc thềm đá trước cửa đôi gỗ" | nhìn vào nhà |
| C57 27–30 | "bước xuống bậc thềm đá, rồi đi thẳng xuống lối xe về phía cổng" | lối xe thẳng |
| C58 3–6 | "Máy phía trong cổng nhìn ra, đặt cạnh trụ cổng bên phải lối xe" | trụ cổng gạch |
| C58 6–9 | "Máy đặt phía trong hàng rào, bên hông cổng, nhìn ngang dọc song sắt: bà … ở mép trái khung; phía ngoài, Devin … ở mép phải khung" | **nhìn dọc rào: trong = trái** |
| C58 26–30 | "Máy phía trong cổng nhìn ra, sau vai trái bà: vai … ở mép phải tiền cảnh" | |
| C59 13–16 | "Máy đặt ngoài cổng sau vai phải Devin nhìn vào: … xa sau lưng bà là lối xe lát đá và cửa đôi gỗ" | |
| C60 26–30, KẾT | "tiếng bộ đàm rè rè vang lên từ vỉa hè bên phải; … cùng quay đầu về mép phải khung; phóng viên lùi ra ngoài khung bên trái" | **nhìn ra: phải = phía cảnh sát** |
| C61 0–3 | "xe tuần tra … đã đỗ sát lề đường sau lưng đám hàng xóm; viên cảnh sát … bước vào khung từ mép phải theo vỉa hè" | |
| C61 6–9 | "Máy đặt trên vỉa hè, ngoài hàng rào, nhìn dọc song sắt về phía cổng: viên cảnh sát … đi dọc hàng rào sắt, ngang qua chỗ bà …" | nhìn dọc rào về cổng |
| C62 17–20 | "dẫn Raven … đi về phía xe tuần tra ở mép phải khung" | |
| C62 27–30 | "xa cuối lối xe, bà đã lên tới bậc thềm đá, bước qua cửa đôi gỗ vào nhà rồi khép hai cánh cửa lại" | |
| C42 0–2 · C43 11–16 · C49 0–2 | (tháng 10) "bậc thềm đá và cây lá vàng tháng Mười" · "dưới hàng cây lá vàng tháng Mười" · "lối xe vòng lát đá …, cổng sắt đen để mở ở cuối lối xe, hàng cây sồi lá vàng tháng Mười, nắng trưa" | cần bảng mùa thu |
| C68 0–2 | (tháng 9) "lối xe lát đá, hàng cây sồi xanh đậm và nắng chiều thấp vàng" | nên có bảng tháng 9 |

### 3.2 Đồ cố định
Nhà colonial gạch đỏ hai tầng. Bậc thềm đá rộng, cửa đôi gỗ có ô kính, cửa sổ vòm phía trên. Lối xe lát đá: chạy thẳng từ cổng, kết bằng vòng quay đầu trước bậc thềm. Cổng sắt rèn đen nằm giữa hai trụ gạch. Hàng rào sắt chạy dọc vỉa hè. Hàng sồi trồng dọc phía trong hàng rào. Ngoài cổng là vỉa hè, bó vỉa và phố yên; bên kia phố là các nhà gạch lớn.

### 3.3 Suy bố cục
Đặt mặt tiền nhìn về Nam (cùng hướng với trong nhà).
- Tường 1 = Bắc: mặt tiền nhà, nhìn từ cổng vào.
- Tường 2 = Đông: bãi cỏ hông, hàng rào chạy về đông, hàng cây xanh ranh giới, nhà kế bên.
- Tường 3 = Nam: cổng và phố. Panel này mang mã `LOT7_EXT`, vì đa số cú là "phía trong cổng nhìn ra".
- Tường 4 = Tây: phố cong đi, cột đèn; phía cảnh sát và xe tuần tra tới.

Kiểm:
- Nhìn từ trong cổng ra (Nam): trái là Đông, nơi phóng viên đứng (C57 KẾT); phải là Tây, nơi có bộ đàm, cảnh sát và xe tuần tra (C60, C61, C62). Đúng.
- Nhìn dọc song sắt với bà (bên trong) ở trái và Devin (bên ngoài) ở phải: máy phải nhìn về Đông, vì khi đó trái là Bắc (trong rào), phải là Nam (vỉa hè). Đúng với C58 6–9.
- C61 6–9: máy trên vỉa hè phía tây cổng nhìn về Đông, viên cảnh sát đi từ tây tới. Cùng hướng với panel Đông.
- "Lối xe vòng" (C49) và "đi thẳng xuống lối xe" (C57, C62) được gộp thành lối xe thẳng kết bằng vòng quay đầu.
- "Dưới hàng cây lá vàng" (C43) và "hàng cây sồi" thấy qua cổng (C49) được gộp thành hàng sồi dọc phía trong rào.

**Có cần bảng ngoài nhà mùa thu không? CÓ.**
- C42 (0–2 s), C43 (11–16 s, toàn cảnh) và C49 (0–16 s, 24–27 s) đều nhìn qua cửa đôi mở ra bậc thềm, lối xe, cổng và hàng sồi lá vàng. C49 0–2 s là cú toàn cảnh.
- Nếu không có bảng, Seedance tự bịa lối xe, cổng và hàng cây, sẽ lệch với bảng tháng Giêng. Bảng tháng Giêng có tuyết và cây trụi nên cũng không dùng thay được.
- Bảng thu vẽ **từ** `LOT7_EXT_BANG`, chỉ đổi mùa và nắng.
- Tương tự, **bảng tháng 9 (`LOT7_EXT_CHIEU_BANG`) là khuyến nghị**: ở C68 lối xe và hàng sồi xanh đậm nằm sau lưng Devin khoảng 14 giây. Nếu muốn tiết kiệm có thể bỏ, nhưng sẽ có rủi ro lệch.

### 3.4 Bảng ánh xạ
| Câu kịch bản | Cụm · giây | Panel |
|---|---|---|
| "Máy đặt trên lối xe, phía trong cổng, nhìn ra cổng" / "Máy phía trong cổng nhìn ra" / "Cùng hướng" | C57 0–8, 10–18, 20–27; C58 3–6, 9–12, 20–23, 26–30; C59 0–13, 16–30; C60 0–8, 10–26; C61 0–6, 9–24, 26–30; C62 0–8, 10–20 (các chèn màn hình điện thoại / còng tay ở giữa dùng cùng nền) | LOT7_EXT |
| "Máy đặt ngoài cổng sau vai phải Raven / Devin nhìn vào lối xe về phía nhà" / "Cùng hướng" | C57 8–10, 27–30; C58 0–3, 12–20; C59 13–16; C62 8–10, 20–30 | LOT7_EXT_HOUSE |
| "Máy đặt phía trong hàng rào, bên hông cổng, nhìn ngang dọc song sắt" | C58 6–9 | LOT7_EXT_EAST |
| "Máy đặt trên vỉa hè, ngoài hàng rào, nhìn dọc song sắt về phía cổng" | C61 6–9 | LOT7_EXT_EAST (+ LOT7_EXT cho rào, cổng) |
| "máy lia chậm sang phải theo ánh nhìn của họ" | C60 26–30 | LOT7_EXT → LOT7_EXT_WEST |
| tháng 10 — qua cửa mở / từ ngoài ngưỡng nhìn vào | C42, C43, C49 | LOT7_EXT_OCT / LOT7_EXT_OCT_HOUSE |
| tháng 9 — qua cửa mở / từ ngoài ngưỡng nhìn vào | C68 | LOT7_EXT_SEP / LOT7_EXT_SEP_HOUSE |

### 3.5 Bảy câu đời thực
1. **Của ai:** như căn nhà ở mục 2. Mặt tiền thuộc khu có cổng có văn phòng bán hàng. Tầng 3.
2. **Ở đâu thật:** Mitchellville, PG County. Nhà colonial mặt gạch, lối vào hai tầng ốp đá, cổng sắt giữa hai trụ gạch, lối xe dài (mục 4.3, tầng 3).
3. **Dấu hiệu người trong cuộc:** colonial "brick-front" có lối vào hai tầng, dấu của ngoại ô da đen giàu ở PG County; trụ gạch và cổng sắt; bãi cỏ cắt tỉa; hàng cây thường xanh ranh giới; phố toàn nhà gạch lớn sân rộng.
4. **Đồ sinh hoạt:** đèn lồng treo, chậu boxwood, luống cẩm tú cầu đã tỉa (tháng 1) hoặc còn hoa khô (tháng 10). Tháng 1 lối xe và bậc thềm đã dọn tuyết, cho thấy có người ở.
5. **Nguồn sáng:** chỉ mặt trời.
   - Tháng 1, 11:00: trời trong, nắng thấp từ phía đường, mặt tiền sáng, nhìn ra cổng là ngược sáng.
   - Tháng 10, 11:20–11:40: nắng trưa cao.
   - Tháng 9, 17:30: nắng thấp từ tây.
   - Đèn lồng tắt.
6. **Người nền:**
   - Tháng 1: khoảng 5 hàng xóm mặc áo khoác mùa đông đứng ở mép vỉa hè (2 người giơ điện thoại quay); phóng viên; 2 cảnh sát quận và xe tuần tra trắng sọc navy không chữ đỗ sát lề phía tây.
   - Tháng 10: bảo vệ khu (C42–43). Sedan xám của Devin là đạo cụ C49.
   - Tháng 9: không ai.
7. **Tiếng nền:**
   - Tháng 1: gió lạnh, bộ đàm rè, giày lạo xạo trên tuyết cũ, chó sủa xa.
   - Tháng 10: lá xào xạc, máy thổi lá xa.
   - Tháng 9: chim, máy cắt cỏ xa.

**Điều sai:**
- Chữ đọc được: số nhà, biển tên khu, chữ "POLICE" hay logo trên xe, logo hãng trên sedan.
- Trang trí Giáng sinh còn sót, người tuyết, tuyết dày trắng xoá (chỉ có tuyết cũ dọc mép).
- Lẫn mùa: lá vàng trong bảng tháng 1, cây xanh trong bảng tháng 10.
- Cổng mở trong bảng: bảng vẽ cổng ĐÓNG. C49 cổng mở, ghi bằng chữ trong prompt.

---

## 4. CĂN HỘ CỦA CHARLENE (`CHARLENE_APT_BANG` ngày · `CHARLENE_APT_DEM_BANG` đêm)

### 4.1 Bằng chứng
| Cụm · giây | Câu kịch bản | Ghi nhận |
|---|---|---|
| C50 13–16 | "máy đặt cạnh bàn tròn bếp nhỏ nhìn ra cửa: cửa mở, Charlene … bước vào … căn hộ chật: sofa giường kê sát tường, cửa phòng ngủ sơn trắng cạnh đó, bếp nhỏ có bàn tròn hai ghế" | bàn tròn ↔ cửa căn hộ |
| C50 20–23 | "Máy đặt cạnh cửa sổ nhìn về sofa giường" | cửa sổ ↔ sofa |
| C50 25–30 | "Máy đặt cạnh cửa căn hộ nhìn về bếp nhỏ" | |
| C51 0–2 | "Máy đặt cạnh cửa căn hộ nhìn vào bếp nhỏ: Raven … ở bàn tròn …; Charlene … ngồi mép sofa giường ở mép trái khung; Devin … đứng cạnh cửa sổ ở mép phải khung" | **từ cửa nhìn bếp: sofa TRÁI, cửa sổ PHẢI** |
| C51 6–8, 10–13, 16–21 | "Máy đặt cạnh sofa giường nhìn về cửa sổ" / "Máy nhìn về cửa sổ" | |
| C51 13–16 | "Máy đặt cạnh cửa sổ nhìn về sofa giường" | |
| C56 0–2 | "Máy đặt trong phòng ngủ tối, sau cánh cửa khép hờ, nhìn qua khe cửa ra phòng khách: tiền cảnh mép trái là mép cánh cửa …; giữa khung, Charlene … ngồi trên sofa giường đã kéo ra …; xa ở góc bếp nhỏ, Raven … tựa quầy bếp …; cây đèn bàn vàng là nguồn sáng duy nhất, cửa sổ tối có tuyết bám mép kính" | đêm |
| C56 2–5, 10–14, 19–23 | "Máy đặt cạnh sofa giường nhìn về góc bếp" — "bàn tròn hai ghế bên cạnh, xấp hoá đơn trên bàn" | |
| C56 8–10 | "Máy đặt ở góc bếp nhìn về sofa giường: … sau lưng bà ta, cửa phòng ngủ sơn trắng khép hờ, khe cửa tối" | cửa phòng ngủ ở sau sofa khi nhìn từ bếp |
| C56 16–19 | "Máy đặt cạnh cửa sổ nhìn về sofa giường và cửa phòng ngủ" | |
| C56 14–16, 23–30 | "Máy đặt trong phòng ngủ tối, sát khe cửa" — "vệt đèn vàng từ khe cửa" | phòng ngủ: không có trong bảng |

### 4.2 Suy bố cục
- Tường 1 = Bắc: bếp nhỏ (quầy, bếp, tủ lạnh) và bàn tròn hai ghế.
- Tường 2 = Đông: cửa sổ và TV.
- Tường 3 = Nam: cửa căn hộ.
- Tường 4 = Tây: sofa giường, đèn bàn, cửa phòng ngủ.

Kiểm:
- Từ cửa căn hộ nhìn về bếp (Bắc): trái là Tây (sofa), phải là Đông (cửa sổ). Đúng C51 0–2.
- Từ bàn tròn nhìn ra cửa (Nam): bên phải là Tây, nên thấy sofa và cửa phòng ngủ. Đúng C50 13–16.
- Sofa (Tây) đối diện cửa sổ (Đông). Đúng.
- Cửa phòng ngủ đặt **phía nam sofa**, gần góc cửa căn hộ. Từ góc bếp nhìn về sofa thì cửa phòng ngủ ở sau lưng Charlene (C56 8–10). Từ khe cửa phòng ngủ nhìn chéo đông bắc thì thấy sofa giường đã kéo ra ở giữa và góc bếp ở xa (C56 0–2).
- Đèn bàn chao xếp nếp vàng đặt giữa sofa và cửa phòng ngủ, nên đêm C56 nó hắt vệt sáng qua khe cửa lên mặt Devin.
- Biến thể đêm chỉ đổi ánh sáng.

### 4.3 Bảng ánh xạ
| Câu kịch bản | Cụm · giây | Panel |
|---|---|---|
| "máy đặt cạnh bàn tròn bếp nhỏ nhìn ra cửa" / "Cùng hướng" | C50 13–20 | CHARLENE_DOOR |
| "Máy đặt cạnh cửa sổ nhìn về sofa giường" | C50 20–23; C51 13–16 | CHARLENE_SOFA |
| Chèn "Cận mặt bàn ăn tròn hai ghế" | C50 23–25 | CHARLENE_KITCHEN |
| "Máy đặt cạnh cửa căn hộ nhìn về bếp nhỏ" / "Máy nhìn về bếp nhỏ" | C50 25–30; C51 0–6, 8–10 | CHARLENE_KITCHEN |
| "Máy đặt cạnh sofa giường nhìn về cửa sổ" / "Máy nhìn về cửa sổ" | C51 6–8, 10–13, 16–21 | CHARLENE_WINDOW |
| "Máy đặt trong phòng ngủ tối, … nhìn qua khe cửa ra phòng khách" | C56 0–2 | CHARLENE_KITCHEN_NIGHT (gần nhất; tiền cảnh là mép cửa và bóng tối) |
| "Máy đặt cạnh sofa giường nhìn về góc bếp" | C56 2–8, 10–14, 19–23 | CHARLENE_KITCHEN_NIGHT |
| "Máy đặt ở góc bếp nhìn về sofa giường" | C56 8–10 | CHARLENE_SOFA_NIGHT |
| "Máy đặt cạnh cửa sổ nhìn về sofa giường và cửa phòng ngủ" | C56 16–19 | CHARLENE_SOFA_NIGHT |
| "Máy … trong phòng ngủ tối, sát khe cửa" | C56 14–16, 23–30 | không có panel; nền tối, dùng vệt đèn và mép cửa của CHARLENE_SOFA_NIGHT |

### 4.4 Bảy câu đời thực
1. **Của ai:** Charlene Lyles, 64 tuổi, nhận là giáo viên về hưu ("Thirty years I taught school"), người đi nhà thờ tích cực, nay sa sút về căn hộ thuê một phòng ngủ. **Tầng 1** (lao động / trung lưu thấp). Từ tháng Giêng có vợ chồng Devin dọn tới ở nhờ.
2. **Ở đâu thật:** khu căn hộ gạch ba tầng kiểu garden-style ở District Heights, PG County (mục 4.3, tầng 1). *Kịch bản không ghi thành phố; Claude chọn, có thể sửa.*
3. **Dấu hiệu người trong cuộc:** hộp mũ tròn màu tím trên nóc tủ lạnh (mũ "church crown"); bình quạt giấy nhà thờ cán gỗ; Kinh Thánh cũ trên bàn đầu sofa; chăn móc len vắt sofa; đĩa kẹo bạc hà (đồ nhà thế hệ boomer); giấy khen đóng khung (để trống chữ).
4. **Đồ sinh hoạt:** xấp hoá đơn trên bàn tròn; dây sạc điện thoại; điều khiển TV; máy sưởi điện nhỏ; giá úp bát; móc treo với ô gấp; bát gốm đựng chìa khoá; lịch treo tường để trống.
5. **Nguồn sáng:**
   - Ngày: ánh ngày tháng Giêng đục qua rèm lá trắng kéo nửa, đèn bàn chao xếp nếp vàng bật.
   - Đêm: chỉ có đèn bàn đó.
6. **Người nền:** không có (chỉ ba nhân vật).
7. **Tiếng nền:**
   - Ngày: máy sưởi tích tích, xe ngoài phố, cửa nhà bên đóng.
   - Đêm: tủ lạnh rì, TV nhà bên lọt qua tường, gió rít ở cửa sổ.

**Điều sai:**
- Vẻ sang hoặc phông bạt.
- Tím tràn khắp phòng: chỉ điểm vài chỗ.
- Bọc nhựa sofa và băng VHS: bà 64 tuổi, không phải cụ trên 80.
- Rác, bẩn hoặc tả kiểu "the projects": nhà tầng 1 thì cũ nhưng sạch.
- Chữ trên hoá đơn và lịch.

### 4.5 Mâu thuẫn
- **C56: "sofa giường đã kéo ra"**, trong khi luật biến thể yêu cầu giữ y bố cục và chỉ đổi ánh sáng. Bảng đêm vẫn để sofa **gập**; prompt video ghi "sofa giường đã kéo ra, chăn trắng". Nếu Seedance cứ giữ sofa gập, sửa riêng panel `CHARLENE_SOFA_NIGHT` bằng `sua_panel`.
- **Cú trong phòng ngủ tối** (C56 0–2, 14–16, 23–30 s) không có panel. Nền là bóng tối, mép cửa trắng và vệt đèn vàng, Seedance tự dựng được.

---

## 5. PHÒNG BỆNH (`HOSP_BANG`)

### 5.1 Bằng chứng
| Cụm · giây | Câu kịch bản | Ghi nhận |
|---|---|---|
| C52 0–4 | "Máy đặt cạnh cửa hành lang nhìn về giường …: Raven … đứng bên giường phía cửa sổ ở mép phải khung …; Devin … bên giường phía ghế khách ở mép trái khung …; áo dạ tím sẫm … vắt trên lưng ghế khách; ở đầu giường, dây bấm gọi y tá màu trắng móc trên thành giường phía ghế khách; bà … bước vào khung từ mép trái" | **từ cửa nhìn giường: cửa sổ PHẢI, ghế TRÁI** |
| C52 27–30 | "Máy đặt cạnh đầu giường nhìn về chân giường" | |
| C53 0–2 | "Máy đặt ở chân giường phía cửa nhìn về giường: … Devin … phía ghế khách ở mép trái khung; Raven … phía cửa sổ ở mép phải khung" | khớp |
| C53 2–5 | "Máy đặt cạnh đầu giường nhìn về cửa" | |
| C53 23–26 | "Máy đặt cạnh cửa sổ nhìn về ghế khách" | cửa sổ ↔ ghế khách |
| C53 28–30 | "Máy đặt cạnh cửa sổ nhìn về cửa hành lang: tiền cảnh mép trái là Charlene nằm trên giường …; ngọn đèn báo nhỏ trên khung cửa hành lang bật sáng; qua ô kính dọc của cánh cửa …" | **sai trái/phải** (xem 5.4) |
| C54 0–2 | "Máy đặt cạnh đầu giường nhìn về cửa: … Charlene nằm … ở tiền cảnh mép phải" | |
| C54 13–17, KẾT | "bà Marguerite đứng cạnh ông ở mép trái khung" (máy nhìn về cửa) · "đứng cạnh ông ở chân giường, phía cửa sổ" | **nhìn ra cửa: cửa sổ TRÁI** |
| C55 0–2 | "Máy đặt cạnh đầu giường nhìn về cửa: … bà … đứng cạnh ông phía cửa sổ ở mép trái khung" | khớp |
| C55 21–24 | "quay chậm sang con trai (ngoài khung bên phải, cạnh đầu giường phía ghế khách)" | **nhìn ra cửa: ghế PHẢI** |
| C55 27–30 | "bà … đứng ở chân giường phía cửa sổ, mép phải khung" (máy sát cửa nhìn giường) | khớp |

### 5.2 Suy bố cục
- Tường 1 = Tây: đầu giường áp tường.
- Tường 2 = Bắc: cửa sổ.
- Tường 3 = Đông: cửa hành lang ở phía chân giường.
- Tường 4 = Nam: ghế khách.

Kiểm: từ cửa nhìn giường (Tây) thì phải là Bắc (cửa sổ), trái là Nam (ghế). Từ đầu giường nhìn cửa (Đông) thì trái là Bắc (cửa sổ), phải là Nam (ghế). Đúng mọi câu, trừ C53 28–30 s.

Dây gọi màu trắng móc ở thành giường phía ghế (Nam), gần đầu giường. Cửa hành lang có ô kính dọc hẹp và đèn báo nhỏ trên khung.

### 5.3 Bảng ánh xạ
| Câu kịch bản | Cụm · giây | Panel |
|---|---|---|
| "Máy đặt cạnh cửa hành lang nhìn về giường" / "Máy nhìn về giường" / "Máy đặt ở chân giường phía cửa nhìn về giường" / "sau vai phải bà ở chân giường nhìn về giường" / "Máy đặt cạnh cửa nhìn về giường" / "Máy (đặt) sát cửa … nhìn vào phòng / nhìn về giường" / "sau vai trái Dr. Okonjo nhìn vào phòng" | C52 0–13, 15–21; C53 0–2, 5–8, 12–15, 21–23; C54 2–5, 10–13, 17–21, 24–27; C55 2–5, 8–11, 14–16, 24–30 | HOSP_BED |
| "Máy nhìn về cửa" / "Máy đặt cạnh đầu giường nhìn về cửa" / "… nhìn về chân giường" | C52 21–25, 27–30; C53 2–5, 8–12, 17–21; C54 0–2, 5–8, 13–17, 21–24, 27–30; C55 0–2, 5–8, 11–14, 16–24 | HOSP_DOOR |
| "Máy đặt cạnh cửa sổ nhìn về ghế khách" | C53 23–26 | HOSP_CHAIR |
| "Máy đặt cạnh cửa sổ nhìn về cửa hành lang" | C53 28–30 | HOSP_DOOR (sửa trái/phải, xem 5.4) |
| Chèn dây gọi trên thành giường | C53 26–28 | HOSP_BED |
| — (phía cửa sổ, nơi Raven đứng) | | HOSP_WINDOW |

### 5.4 Mâu thuẫn
**C53 28–30 s.** Câu "Máy đặt cạnh cửa sổ nhìn về cửa hành lang: tiền cảnh mép trái là Charlene nằm trên giường" sai hình học. Đứng phía cửa sổ (Bắc) nhìn ra cửa hành lang (Đông) thì giường nằm ở **bên phải** máy. Hai cách sửa:
- **(a)** Giữ vị trí máy, đổi thành "tiền cảnh mép **phải** là Charlene…". Raven cũng ở phải, bám thành giường phía cửa sổ. Ít sửa nhất.
- **(b)** Giữ "mép trái", đổi máy thành "Máy đặt cạnh đầu giường **phía ghế khách** nhìn về cửa hành lang". Khi đó giường ở trái, còn Raven ở phía bên kia giường bám thành giường.

Khuyến nghị (a).

### 5.5 Bảy câu đời thực
1. **Của ai:** phòng đơn của một bệnh viện khu vực công lập ở PG County (không nêu tên thật). Nơi công, sạch, rõ là đang dùng.
2. **Ở đâu thật:** Prince George's County, Maryland, đúng kịch bản. Bệnh viện mới, tường xanh xám nhạt.
3. **Dấu hiệu người trong cuộc:** ghế ngả bằng vinyl cho người nhà ngủ lại; bảng trắng chăm sóc (để trống); tường đầu giường có ổ oxy; TV treo cao. Đây là phòng phụ của cộng đồng nên chỉ cần 1–2 dấu hiệu.
4. **Đồ sinh hoạt:** bình nước nhựa trên bàn ăn gác ngang giường, hộp khăn giấy, lọ cẩm chướng vàng (ai đó mang tới), bình xịt sát khuẩn, bồn rửa nhỏ.
5. **Nguồn sáng:** đèn tấm trần trắng lạnh phẳng; ánh ngày đục mùa đông qua rèm dọc; một chi tiết ấm là lọ cẩm chướng vàng. Theo look: `benh_vien`.
6. **Người nền:** qua ô kính cửa có y tá mặc scrubs xanh teal bưng khay và bảo vệ bệnh viện đồng phục xanh than (C54–55), vài người đi qua hành lang. Đều im lặng, chỉ trong prompt.
7. **Tiếng nền:** chuông gọi trên hành lang, bánh xe đẩy, bước chân; máy theo dõi tắt nên không có tiếng bíp.

**Điều sai:**
- Thánh giá có tượng trên tường (kiểu bệnh viện Công giáo).
- Chữ hoặc số trên bảng trắng, màn hình, vòng tay.
- Logo bệnh viện thật.
- Túi truyền đang nối vào người: Charlene giả bệnh.
- Ám xanh lục u ám, hoặc phòng tối như phim kinh dị.

---

## 6. HÀNH LANG TOÀ ÁN Ở UPPER MARLBORO (`COURT_HALL_BANG`)

### 6.1 Bằng chứng
- C63 0–3 s, "Máy đặt giữa hành lang nhìn về cửa phòng xử". Kịch bản tả: "sàn đá cẩm thạch màu be, tường ốp gỗ sồi sáng màu, cửa sổ cao hắt ánh sáng ban ngày trắng; dãy ghế băng gỗ dài dọc tường, khoảng sáu người chờ …; một nhân viên an ninh toà … ở cuối hành lang; cửa gỗ đôi phòng xử có ô kính mờ …; Devin … đứng ở **mép phải khung cạnh cột ốp gỗ**".
- C63 3–9 s: "Máy lùi theo" / "Cùng hướng".
- C63 12–16 s, "Máy đặt sát dãy ghế băng nhìn ngang hành lang". Kịch bản tả: "người chờ trên ghế băng quay sang nhìn …; nhân viên an ninh toà ở cuối hành lang bước lên một bước; Devin … rời cột ốp gỗ".
- C63 9–12, 19–28 s: các cú qua vai (Charlene / Raven / Devin).
- C63 28–30 s, "Máy đặt giữa hành lang nhìn về cửa phòng xử: Devin quay lưng đi về phía máy, **ra khỏi khung bên trái**".

### 6.2 Suy bố cục
Hành lang chạy theo trục đông – tây.
- Tường 1 = Bắc: cửa đôi phòng xử, ghế băng hai bên cửa (người chờ thấy được trong cú nhìn cửa), cột ốp gỗ ngay **bên phải** cửa.
- Tường 2 = Đông: cuối hành lang, cửa ra cầu thang bộ.
- Tường 3 = Nam: cửa sổ cao, hắt sáng trắng về phía cửa phòng xử.
- Tường 4 = Tây: chốt an ninh (cổng dò kim loại) và lối ra thang máy.

Kiểm:
- 12–16 s: "nhìn ngang hành lang" từ dãy ghế băng là nhìn dọc về Tây. An ninh ở cuối hành lang bước lên; ghế băng chạy ở bên phải panel (tường 1 = phải của panel 4). Đúng.
- 28–30 s: Devin ra mép trái của panel 1, tức đi về Tây, phía lối ra. Đúng.

### 6.3 Bảng ánh xạ
| Câu kịch bản | Giây | Panel |
|---|---|---|
| "Máy đặt giữa hành lang nhìn về cửa phòng xử" / "Máy lùi theo" / "Cùng hướng" | 0–9, 28–30 | COURT_DOORS |
| "Máy đặt sau vai Charlene nhìn Raven" | 9–12 | COURT_DOORS (Raven ở phía cửa phòng xử) |
| "Máy đặt sát dãy ghế băng nhìn ngang hành lang" | 12–16 | COURT_HALL_WEST |
| "Máy đặt sau vai Raven nhìn Devin" | 19–22, 25–28 | COURT_WINDOWS (ngược 180°) |
| "Máy đặt sau vai Devin nhìn Raven" | 22–25 | COURT_DOORS |

### 6.4 Bảy câu đời thực
1. **Của ai:** toà án vòng quận (circuit court) của Prince George's County. Nhà công, cũ nhưng giữ gìn.
2. **Ở đâu thật:** Upper Marlboro, quận lỵ của PG County, đúng kịch bản. Không ghi tên toà nhà.
3. **Dấu hiệu:** chốt an ninh có cổng dò kim loại và băng chuyền X-quang (mục 6, "toà án gia đình"); ghế băng gỗ dài ngoài cửa phòng xử; tủ kính dán thông báo (để trống).
4. **Đồ sinh hoạt:** vòi nước uống, thùng rác thép, đồng hồ treo tường không số.
5. **Nguồn sáng:** cửa sổ cao phía Nam cho ánh ngày trắng; đèn trần âm phẳng. Không có đèn ấm.
6. **Người nền:** khoảng 6 người ngồi chờ trên ghế băng, im lặng, mặc áo khoác hoặc đồ công sở giản dị, đa số người da đen PG County, trộn tuổi. 1 nhân viên an ninh toà đồng phục xanh than đứng xa ở đầu Tây.
7. **Tiếng nền:** bước chân vang trên đá cẩm thạch, tiếng thì thầm, tiếng cửa phòng xử đóng, tiếng bíp cổng dò ở xa.

**Điều sai:**
- Chữ trên cửa, số phòng, con dấu của quận.
- Thẩm phán đứng ở hành lang.
- Hành lang tối kiểu phim hình sự.
- Cờ có chữ.

---

## 7. HỘI TRƯỜNG HẦM NHÀ THỜ BAPTIST (`CHURCH_HALL_BANG`)

### 7.1 Bằng chứng
- C64 0–3 s, "Máy đặt ở cuối hàng người xếp hàng nhìn về quầy phát đồ ăn". Kịch bản tả: "hội trường dưới hầm nhà thờ — sàn linoleum lốm đốm, trần thả đèn tuýp, tường gạch block sơn kem, dãy bàn gấp dài phủ khăn nhựa trắng, ghế gấp kim loại, cây đàn piano đứng cạnh cửa ra, bảng tin dán tờ rơi trắng không chữ; sau quầy phát đồ ăn bằng thép, Charlene … múc gumbo từ nồi thép lớn …; phía sau bà ta, Raven … ở bồn rửa thép đôi …; khoảng mười lăm người lớn tuổi xếp hàng".
- C64 5–8 s: "Máy đặt sau quầy, sau vai trái Charlene, nhìn ra hàng người"; vai Charlene ở "tiền cảnh mép phải".
- C64 8–16 s và 23–26 s: "Máy đặt trước quầy nhìn vào"; Raven ở bồn rửa phía sau.
- C64 16–23 s: "Máy đặt sau quầy nhìn ra hàng người".
- C64 26–30 s: "Máy đặt ở đầu quầy, lùi chậm dọc hàng người". Sister Bernice và Sister Pearl "đi về dãy bàn gấp"; "hàng người dài tới cửa ra".

### 7.2 Suy bố cục
- Tường 1 = Bắc: quầy thép trước cửa thông sang bếp nhà thờ, bồn rửa thép đôi phía sau. Mã `CHURCH_HALL`.
- Tường 2 = Đông: dãy bàn gấp, cửa sổ hầm cao.
- Tường 3 = Nam: thánh giá gỗ trơn, băng rôn không chữ, xe đẩy chồng ghế gấp. Đây là hướng "sau quầy nhìn ra".
- Tường 4 = Tây: cửa thép đôi ra cầu thang, piano đứng, bảng tin, kệ đồ hộp của kho thực phẩm.

Hàng người chạy dọc phía Tây, từ quầy tới cửa ra.

Kiểm:
- 0–3 s, từ cuối hàng nhìn quầy: piano và cửa ra ở mép trái (tường 4 = trái của panel 1), bàn gấp ở phải. Như vậy piano, cửa ra và bảng tin đều nằm trong khung như kịch bản liệt kê.
- Từ sau quầy nhìn ra: hàng người kéo về cửa ra ở bên phải (tường 4 = phải của panel 3); hai Sister cầm bát đi về dãy bàn ở bên trái.

### 7.3 Bảng ánh xạ
| Câu kịch bản | Giây | Panel |
|---|---|---|
| "Máy đặt ở cuối hàng người xếp hàng nhìn về quầy phát đồ ăn" | 0–3 | CHURCH_HALL |
| Chèn muôi gumbo | 3–5 | CHURCH_HALL |
| "Máy đặt sau quầy, sau vai trái Charlene, nhìn ra hàng người" / "Máy đặt sau quầy nhìn ra hàng người" | 5–8, 16–23 | CHURCH_HALL_OUT |
| "Máy đặt trước quầy nhìn vào" / "Cùng hướng" | 8–16, 23–26 | CHURCH_HALL |
| "Máy đặt ở đầu quầy, lùi chậm dọc hàng người" | 26–30 | CHURCH_HALL + CHURCH_HALL_EXIT |

### 7.4 Bảy câu đời thực
1. **Của ai:** một hội thánh Baptist người da đen cỡ vừa, gạch đỏ. Đây chính là nhà thờ của Charlene (Sister Bernice và Sister Pearl là bạn nhà thờ của bà ta). Bữa trưa miễn phí thứ Bảy; hội thánh tầng lao động – trung lưu.
2. **Ở đâu thật:** hội trường dưới hầm (fellowship hall) của nhà thờ ở District Heights, PG County. *Claude chọn District Heights, cùng khu với căn hộ Charlene.* Tin Lành, không phải Công giáo.
3. **Dấu hiệu Tin Lành da đen (≥3):** thánh giá gỗ trơn không tượng; băng rôn tím – vàng của hội thánh không chữ; piano đứng cạnh cửa ra; bảng tin tờ rơi; bình cà phê lớn và khay nhôm; kệ đồ hộp của kho thực phẩm (mục 5.1: 29% từng nhờ nhà thờ giúp đồ ăn); chai tương ớt trên mỗi bàn.
4. **Đồ sinh hoạt:** xe đẩy chồng ghế gấp, hộp đựng giấy ăn, lọ muối tiêu, chồng bát giấy, khay nhôm.
5. **Nguồn sáng:** đèn tuýp trần thả phẳng; chút ánh ngày qua cửa sổ hầm cao kính mờ; hơi nóng bốc từ nồi.
6. **Người nền:** khoảng 15 người lớn tuổi xếp hàng, mặc áo khoác xuân hoặc đồ đi nhà thờ giản dị, trộn nam nữ, im lặng, cầm bát giấy. Tình nguyện viên đeo tạp dề xanh và lưới tóc. Không có mục sư mặc áo lễ.
7. **Tiếng nền:** muôi gõ nồi, ghế gấp cào sàn, tiếng nói khẽ, tiếng cọ nồi ở bồn rửa. Không nhạc (`无音乐`).

**Điều sai:**
- Đồ Công giáo. Theo mục 5.6, không liệt kê sẵn trong bài; chỉ chặn khi render đã lỡ ra.
- Kính màu dưới hầm.
- Chữ trên tờ rơi, băng rôn, nhãn hộp.
- Nhãn hãng thật trên đồ hộp.
- Chữ "soup kitchen" hoặc "food stamps".
- Biếm hoạ người nghèo.
- Sảnh sang trọng.

---

## 8. KHO PHÂN PHỐI (`WAREHOUSE_BANG`)

### 8.1 Bằng chứng
- C65 0–3 s, "Máy đặt ở góc nghỉ của kho nhìn về dãy giá kệ". Kịch bản tả: "góc nghỉ có bàn gấp, ghế nhựa, tủ lạnh nhỏ …; sau lưng họ là dãy giá kệ thép cao và xe nâng vàng; vài công nhân kho đi qua".
- C65 5–9 s: "Máy đặt sau vai đồng nghiệp nhìn về Devin".
- C65 11–14 s: "Máy đặt ở góc nghỉ nhìn về lối đi giữa giá kệ"; Devin "đứng bật dậy ở mép phải khung".
- C65 17–24 s: "Máy đặt ở lối đi, sau vai quản lý kho, nhìn về góc nghỉ"; đồng nghiệp "ở bàn gấp mép trái khung".
- C65 24–27 s: "Máy nhìn về lối đi giữa giá kệ".
- C65 27–30 s, "Máy đặt cạnh băng chuyền, lùi chậm theo Devin … đi dọc dãy giá kệ thép cao". KẾT ghi `WAREHOUSE`.

### 8.2 Suy bố cục và ánh xạ
- Tường 1 = Đông: lối đi giữa giá kệ, xe nâng. Mã `WAREHOUSE`.
- Tường 2 = Nam: cửa bốc dỡ hàng.
- Tường 3 = Tây: góc nghỉ.
- Tường 4 = Bắc: băng chuyền chạy dọc giá kệ.

Hai hướng chính "góc nghỉ → giá kệ" và "lối đi → góc nghỉ" là cặp ngược 180°. Ở cú cuối, băng chuyền nằm bên trái máy (tường 4 = trái của panel 1).

| Câu kịch bản | Giây | Panel |
|---|---|---|
| "Máy đặt ở góc nghỉ của kho nhìn về dãy giá kệ" / "Cùng hướng" | 0–5 | WAREHOUSE |
| "Máy đặt sau vai đồng nghiệp nhìn về Devin" | 5–9 | WAREHOUSE (giá kệ sau lưng Devin, như 0–3 s) |
| Chèn tay nhét phong bì | 9–11 | WAREHOUSE_BREAK |
| "Máy đặt ở góc nghỉ nhìn về lối đi giữa giá kệ" / "Máy nhìn về lối đi giữa giá kệ" | 11–17, 24–27 | WAREHOUSE |
| "Máy đặt ở lối đi, sau vai quản lý kho, nhìn về góc nghỉ" / "Cùng hướng" | 17–24 | WAREHOUSE_BREAK |
| "Máy đặt cạnh băng chuyền, lùi chậm theo Devin" | 27–30 | WAREHOUSE (+ WAREHOUSE_CONVEYOR) |

### 8.3 Bảy câu đời thực
1. **Của ai:** một công ty hậu cần (không tên, không logo). Nơi làm của công nhân tầng 1. Devin làm ở đây 8 tháng, nay lên tổ trưởng ca.
2. **Ở đâu thật:** kho phân phối ở Prince George's County, đúng kịch bản. Quận có nhiều trung tâm logistics dọc các xa lộ.
3. **Dấu hiệu:** góc nghỉ với lò vi sóng trên xe đẩy và bàn gấp; dãy tủ khoá; bảng tin an toàn (để trống); giá kệ pallet và xe nâng vàng; pallet bọc màng co.
4. **Đồ sinh hoạt:** tủ lạnh nhỏ, bình nước, ghế nhựa, cuộn băng dính, thùng carton trơn.
5. **Nguồn sáng:** đèn LED high-bay trắng lạnh đều; ánh ngày lọt qua cửa bốc dỡ mở nửa. Không đèn ấm.
6. **Người nền:** 4–6 công nhân mặc gi-lê phản quang cam đi qua, 1 tài xế xe nâng. Trộn nam nữ, đa số người da đen.
7. **Tiếng nền:** tiếng bíp lùi của xe nâng, băng chuyền rì, tiếng bíp máy quét.

**Điều sai:**
- Logo hoặc chữ trên thùng, gi-lê, biển lối đi.
- Biển an toàn có chữ.
- Kho tối bẩn kiểu xưởng bóc lột.

---

## 9. PHÒNG STUDIO THUÊ CỦA DEVIN (`DEVIN_STUDIO_BANG`, đêm)

### 9.1 Bằng chứng
- C67 0–3 s, "Máy đặt ở cửa ra vào nhìn vào phòng". Kịch bản tả: "phòng studio nhỏ — giường đơn trải chăn xám, bàn gấp với một ghế, góc bếp nhỏ có bếp điện hai lò và tủ lạnh thấp, đèn bàn chao vải vàng; gi-lê phản quang cam và thẻ đeo dây cam treo trên móc cạnh cửa, **ở mép trái tiền cảnh**; Devin … đứng ở góc bếp, khuấy nồi gang".
- C67 3–5 s, chèn: "tờ công thức viết tay giấy ngả vàng … dựng vào hũ muối; … thớt gỗ với hành, cần tây, ớt chuông xanh thái hạt lựu".
- C67 5–8, 10–17 s: "Máy đặt cạnh bếp nhìn về Devin".
- C67 19–26 s: "Máy đặt ở bàn gấp nhìn về góc bếp".
- C67 26–30 s: "Máy đặt ở cửa ra vào, đẩy chậm vào". Kịch bản tả: "trên bàn gấp sau lưng anh là chiếc áo len cổ tròn xanh navy gấp phẳng và một chiếc khăn bếp trắng gấp vuông".

### 9.2 Suy bố cục và ánh xạ
- Tường 1 = Bắc: góc bếp. Mã `DEVIN_STUDIO`.
- Tường 2 = Đông: giường đơn và cửa sổ.
- Tường 3 = Nam: cửa ra vào.
- Tường 4 = Tây: bàn gấp, một ghế, đèn bàn chao vải vàng, móc treo ở góc gần cửa.

Kiểm:
- Từ cửa nhìn vào (Bắc): móc treo ở trái (tường 4 = trái của panel 1), giường ở phải.
- Bàn gấp nằm giữa Devin và cửa, nên là "sau lưng anh" khi nhìn từ cửa.

| Câu kịch bản | Giây | Panel |
|---|---|---|
| "Máy đặt ở cửa ra vào nhìn vào phòng" / "… đẩy chậm vào" | 0–3, 26–30 | DEVIN_STUDIO |
| Chèn công thức, thớt, điện thoại | 3–5, 8–10, 17–19 | DEVIN_STUDIO |
| "Máy đặt cạnh bếp nhìn về Devin" | 5–8, 10–17 | DEVIN_STUDIO_TABLE (nền sau Devin là bàn, đèn vàng và móc; chọn vì kịch bản không nói máy ở bên nào bếp) |
| "Máy đặt ở bàn gấp nhìn về góc bếp" | 19–26 | DEVIN_STUDIO |

### 9.3 Bảy câu đời thực
1. **Của ai:** Devin Batiste, khoảng 40 tuổi. Từng là giám đốc, bị đuổi việc, mất nhà, ly hôn; nay là công nhân kho thuê phòng studio. Tầng 1, khiêm tốn mà sạch. Đây là chỗ anh tự làm lại đời.
2. **Ở đâu thật:** tầng hai một khu chung cư gạch thấp tầng kiểu garden-style ở Capitol Heights, PG County, đúng kịch bản.
3. **Dấu hiệu:** "bộ ba" hành – cần tây – ớt chuông thái hạt lựu (gốc gumbo Creole/Cajun); nồi gang; chai tương ớt; tờ công thức viết tay ngả vàng của mẹ.
4. **Đồ sinh hoạt:** dây sạc trên tủ đầu giường, giỏ khăn gấp, móc treo với thẻ dây cam, khăn bếp trắng gấp vuông, thảm chùi chân.
5. **Nguồn sáng:** đèn bàn chao vải vàng và đèn dưới máy hút mùi, ngoài ra không còn nguồn sáng nào khác; cửa sổ tối, rèm lá đóng.
6. **Người nền:** không ai.
7. **Tiếng nền:** nồi sôi lục bục, thìa gỗ chạm gang, tủ lạnh rì, một chiếc xe chạy qua ngoài phố, TV nhà bên lọt qua tường.

**Điều sai:** đồ sang, đèn LED dải, ring light, vàng; bừa bộn, rác, hộp đồ ăn ngoài chất đống; chữ đọc được trên tờ công thức.

Gi-lê phản quang và áo len navy là đồ mặc, không tả trong bảng (luật cấm chữ quần áo); thêm bằng prompt video.

---

## 10. Tổng hợp mâu thuẫn và việc nên làm

| # | Chỗ | Mâu thuẫn | Cách giải |
|---|---|---|---|
| 1 | Mã `FOYER_STAIRS` | Brief gợi ý mã này cho Lot 7, nhưng kịch bản dùng nó cho sảnh **nhà Devin ở Bowie** (KẾT C1–C3) | Không dùng lại. Panel Lot 7 đặt tên `LOT7_FOYER_DOORS` / `LOT7_STAIRS`… Tránh cả bàn console và gương tròn của sảnh Bowie |
| 2 | Mã `LOT7_IN` | Dùng chung cho góc làm việc (C66) và phòng ăn (C68–70) | Tách thành `LOT7_WORK`, `LOT7_DINING_*` |
| 3 | C53 28–30 s | "Máy đặt cạnh cửa sổ nhìn về cửa hành lang: tiền cảnh mép **trái** là Charlene nằm trên giường": đứng phía cửa sổ thì giường phải ở **phải** | Sửa (a) "mép phải" (khuyến nghị) hoặc (b) "máy cạnh đầu giường phía ghế khách" |
| 4 | C56 | "sofa giường đã kéo ra", trái luật biến thể chỉ đổi ánh sáng | Bảng đêm giữ sofa gập; prompt ghi đã kéo ra; nếu cần thì `sua_panel` riêng CHARLENE_SOFA_NIGHT |
| 5 | C56 0–2, 14–16, 23–30 s | Cú trong phòng ngủ tối, không thuộc bảng phòng khách | Nền tối, mép cửa trắng, vệt đèn vàng; 0–2 s dùng CHARLENE_KITCHEN_NIGHT |
| 6 | C66 "phòng khách" | Hướng nhìn ngược từ bàn bị gọi là "phòng khách" | Phương án 2 bảng: đó là phía sảnh với cầu thang và đôi ghế kem. Trái/phải đều đúng. Phương án 3 bảng để dự phòng |
| 7 | C49 "lối xe vòng" vs C57/C62 "đi thẳng xuống lối xe" | Hai cách tả lối xe | Lối xe thẳng từ cổng, kết bằng vòng quay đầu trước bậc thềm |
| 8 | C49 cổng mở vs C57–62 cổng đóng | Trạng thái đạo cụ | Mọi bảng vẽ cổng đóng; C49 mở cổng bằng prompt |
| 9 | C68 dùng bảng sảnh ánh ngày | Cảnh 17:30 nắng thấp | Nắng tả bằng prompt, có thêm LOT7_EXT_SEP; nếu render thiếu thì làm biến thể LOT7_FOYER_CHIEU_BANG |
| 10 | "nắng xiên vàng", "nắng chiều thấp vàng" (C68–70) | Look phim cấm ám cam toàn khung | Câu ánh sáng ghi rõ vệt nắng thấp, phần còn lại ánh ngày trung tính, "no global orange or amber cast" |
| 11 | Charlene, nhà thờ | Kịch bản không ghi thành phố | Claude chọn District Heights cho cả hai, sửa được |

Không thấy mâu thuẫn trái/phải nào khác ở các cụm đã đọc: C42, C43, C49, C50–C52, C54–C70.
