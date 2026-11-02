> Claude soạn ngày 02/11/2026 khi đọc trọn 70 cụm để dựng ảnh. Số dòng dạng (L123) hay "dòng 123" tính từ dòng `## KỊCH BẢN CHI TIẾT 70 CỤM` của `03_kich-ban-chinh-sua.md` (dòng 490 của file đó là L1); cộng 489 để ra số dòng trong 03.

# Bible bối cảnh A — Nhà Devin & Raven ở Bowie (EAT IN THE KITCHEN)

Nguồn: `kb.txt` (kịch bản chi tiết 70 cụm, bản 02/11/2026), đọc trọn C1–C11, C18–C21, C33, C44, C48, C50. Máy đọc: `boi_canh_A.json` (cùng thư mục). Tool: `bang_4_goc.py` — panel k nhìn thẳng tường k, tường k+1 ở BÊN PHẢI máy, k−1 bên trái, k+2 sau lưng máy.

## 0. Tóm tắt

| Bảng | Panel 1 / 2 / 3 / 4 | Trạng thái | Vẽ từ | Cụm |
|---|---|---|---|---|
| `BOWIE_HOUSE_DAY_BANG` | BOWIE_KITCHEN_DAY / BOWIE_DINING_DAY / **FOYER_STAIRS** / BOWIE_SOFA_DAY | ngày, gọn (bà còn ở) | — (gốc) | C1–C3 |
| `BOWIE_HOUSE_MESSY_BANG` | BOWIE_KITCHEN_MESSY / BOWIE_DINING_MESSY / BOWIE_FOYER_MESSY / BOWIE_SOFA_MESSY | ngày, bừa (bà đã đi) | DAY | C18–C20, C48 |
| `BOWIE_HOUSE_NIGHT_BANG` | BOWIE_KITCHEN_NIGHT / BOWIE_DINING_NIGHT / BOWIE_FOYER_NIGHT / BOWIE_SOFA_NIGHT | đêm thường, bừa | MESSY | C21, C33, C44 (0–22 s) |
| `BOWIE_PARTY_NIGHT_BANG` | **NIGHT_KITCHEN** / **NIGHT_DINING** / BOWIE_PARTY_FOYER / BOWIE_PARTY_SOFA | đêm tiệc, gọn | DAY | C4–C10 (0–25 s) |
| `BOWIE_FRONT_DAY_BANG` | BOWIE_FRONT_DAY / BOWIE_DRIVEWAY_DAY / BOWIE_STREET_DAY / BOWIE_SIDEYARD_DAY | mặt tiền ngày đầu thu | — (gốc) | nền ngoài cửa mở: C3, C18, C20, C48 |
| `BOWIE_FRONT_NIGHT_BANG` | **PORCH_NIGHT** / BOWIE_DRIVEWAY_NIGHT / BOWIE_STREET_NIGHT / BOWIE_SIDEYARD_NIGHT | đêm tiệc ngoài hiên | FRONT_DAY | C10 (25–30 s), C11 |
| `BOWIE_FRONT_SNOW_BANG` | BOWIE_FRONT_SNOW / BOWIE_DRIVEWAY_SNOW / BOWIE_STREET_SNOW / BOWIE_SIDEYARD_SNOW | tuyết tháng Giêng, ngày | FRONT_DAY | C50 (0–13 s) |

Mã in đậm là mã kịch bản đã dùng (FOYER_STAIRS, NIGHT_KITCHEN, NIGHT_DINING, PORCH_NIGHT). HALL_DOOR và FRONT_NIGHT **không có** trong kịch bản nên không dùng. Mọi mã khác có tiền tố BOWIE_ để khỏi trùng bảng B/C. 28 panel, không trùng tên.

**Thứ tự tạo ảnh** (đúng thứ tự khoá trong JSON — `dung_bang_4_goc.py` duyệt theo thứ tự này): DAY → MESSY → NIGHT → PARTY; FRONT_DAY → FRONT_NIGHT → FRONT_SNOW. NIGHT vẽ từ MESSY nên MESSY phải có ảnh trước.

## 1. Bằng chứng từ kịch bản

### 1.1 Trong nhà — các hướng máy

| Hướng (câu kịch bản) | Cụm · giây | Thấy gì / trái–phải |
|---|---|---|
| "Máy đặt phía đảo bếp nhìn về cửa chính" | C1 0–2, 16–30; C2 0–8, 26–30; C3 0–8, 15–19 | Bàn console + gương tròn **nửa trái**; chân cầu thang, lan can trắng **nửa phải** ("Raven bước sang chân cầu thang ở nửa phải khung" C1 20–24; "Devin bước xuống mấy bậc cuối cầu thang ở nửa phải khung, một tay vịn lan can trắng" C2 0–2); cửa chính ô kính mờ ở giữa ("sau ô kính mờ của cửa chính hiện bóng mờ một người cầm chùm bóng bay" C2 26–30) |
| "Máy nhìn về cửa chính" (cận bà ở console) | C1 6–9, 13–16; C2 11–14, 20–23; C3 19–22, 25–30 | "gương tròn trên console mờ sau lưng" (C1 6–9); "sau lưng bà là cửa chính sơn trắng ô kính mờ" (C2 20–23) → console sát bên trái cửa |
| "Máy đặt sau vai trái Marguerite nhìn về bếp" | C1 2–6; C2 8–11; C3 8–13 | vai bà ở tiền cảnh **mép phải**; "đảo bếp đá trắng sau lưng họ" (C2 14–18) |
| "Máy nhìn về bếp" → cửa phòng giặt | C3 22–25 | "cửa gỗ hẹp phòng giặt ở đầu bếp sau lưng mình" |
| "Máy đặt phía bàn ăn nhìn về bếp" | C4 0–3; C9 0–7; C10 0–4 | bà ở đảo bếp, bát ở "góc đảo bếp"; "bồn rửa đôi dưới cửa sổ tối" (C9 5–7); "cửa gỗ hẹp phòng giặt ở **đầu phải** bếp" (C9 27–30, C10 0–4); "Raven đứng cạnh bồn rửa ở **nửa trái** khung" (C9 19–24); "khăn lau sage treo tay lò" (C9 14–17); "đèn thả vàng" trên đảo (C8 25–27, C44 28–30) |
| "Máy đặt ở dãy ghế phía sofa nhìn về tủ buffet" | C4 3–8; C5 0–11; C6 12–15; C9 24–27; C10 12–15 | đầu bàn phía bếp ở **mép trái** (bà bê nồi "đi vào khung từ mép trái"), "Devin ngồi ghế đầu bàn phía cửa chính, xa ở **mép phải**"; dãy ghế phía buffet: Raven ghế 1, Charlene ghế 2, Bernice 3, Pearl 4 tính từ đầu bếp; "bóng bay vàng kim buộc lưng ghế Charlene"; Charlene lấy "quạt giấy nhà thờ cán gỗ vừa lấy từ tủ buffet sau lưng" (C10 12–15) |
| "Máy đặt ở đầu bàn phía cửa chính nhìn dọc bàn về bếp" | C4 8–11; C5 19–24; C6 0–10; C7 0–2; C8 0–9; C10 19–22 | "Raven và Charlene ngồi ở **nửa phải** khung ngay cạnh bà" (C6 0–2) → dãy buffet ở bên phải khi nhìn về bếp |
| "Máy đặt sau lưng bà ở đầu bàn phía bếp nhìn dọc bàn về cửa chính" | C4 11–15; C5 11–13; C6 10–12; C7 12–14; C8 9–13; C10 6–9 | "vành mũ tím của Charlene mờ ở tiền cảnh **mép trái**" → dãy buffet ở bên trái khi nhìn về cửa chính |
| "Máy đặt cạnh bồn rửa nhìn ra phòng" | C9 9–14, 17–19 | nhìn từ bếp ra phía cửa chính |
| "Máy đặt ngoài hiên nhìn qua cửa chính đang mở vào phòng" | C10 22–25 | "bàn tiệc và mười vị khách mờ phía sau bà" → từ cửa nhìn thẳng thấy bàn ăn |
| "Máy đặt ở mép phòng ăn nhìn về cửa chính" | C18 0–4; C20 21–30 | "ở **mép phải** khung, trên sofa chữ L xám than, Raven… và Charlene" |
| "Máy đặt cạnh cửa chính nhìn vào bếp" | C18 4–6 | "đảo bếp bừa hộp đồ ăn…, bát đĩa chưa rửa chất cao trong bồn, rổ quần áo chưa giặt dưới chân cầu thang" |
| "Máy đặt cạnh sofa nhìn về phía bàn ăn" | C18 6–9, 12–14, 22–27; C19 8–11, 17–25; C20 9–21; C33 10–13 | "tủ buffet gỗ mờ sau lưng" bà; Devin "đi ngang qua **mép phải** khung về phía đầu sofa phía cửa chính"; Raven "đi vòng tới tủ buffet gỗ, kéo ngăn kéo" (C19 19–22) |
| "Máy đặt sau vai phải bà nhìn về sofa" | C18 9–12, 14–22, 27–30; C19 0–8, 11–17, 25–30; C20 0–9 | vai bà tiền cảnh **mép trái**; "Devin đứng ở đầu sofa phía cửa chính, **mép trái**"; "Charlene ngồi ở đầu sofa phía bếp, **mép phải**"; bàn trà kính |
| "Máy đặt ở mép phòng khách nhìn về bàn ăn" | C21 0–13, 26–30 | Raven trái, Charlene phải, laptop "nắp quay về máy"; "đèn chùm trên bàn ăn"; "bàn gỗ sẫm" (C21 5–7) |
| "Máy đặt ở mép phòng ăn nhìn về phòng khách" | C21 18–23 | Raven "ngồi phịch xuống sofa chữ L xám than" |
| "Máy đặt ở góc sofa nhìn về cửa chính" | C33 0–8 | "ở **mép phải** khung, Raven và Charlene ngồi trên sofa quay đầu lại nhìn ra cửa" |
| "Máy đặt giữa phòng khách / giữa phòng nhìn về sofa" | C33 8–10, 13–24, 27–30; C44 0–17 | "rèm voan kéo kín, đèn bàn chao vải sáng vàng" (C33 KẾT); Charlene "ngồi ở đầu sofa gần cửa sổ"; Devin "ngồi trên tay sofa phía bếp (**mép phải** khung)" (C44 0–2) |
| "Máy đặt gần cửa chính, lia theo Devin về phía bếp" | C44 17–22 | Raven, Charlene "ở **mép trái** khung" (sofa) khi nhìn về bếp |
| "Máy đặt cạnh đảo bếp nhìn về cửa chính" / "trước bàn console nhìn về bếp" | C48 0–5 | "cửa chính vừa mở, nắng trưa tràn vào"; "khay chìa khoá" trên console (C48 5–9, 23–25); "Raven đứng nghiêng ở **nửa trái** khung" trước cửa (C48 25–28) |

**Đồ cố định & vật liệu nêu trong kịch bản:** đảo bếp "đá trắng vân xám" (C9 19–24); "đèn thả vàng" trên đảo; "bồn rửa đôi dưới cửa sổ"; lò có tay cầm treo khăn sage; "cửa gỗ hẹp phòng giặt ở đầu phải bếp", bên trong "bóng đèn nhỏ… giường gấp hẹp kê sát máy giặt" (C10 0–4); bàn console + "gương tròn"; "cửa chính sơn trắng ô kính mờ"; cầu thang "lan can trắng", lên "lầu"; "sofa chữ L xám than"; "bàn trà kính"; "tủ buffet gỗ" có ngăn kéo; bàn ăn "gỗ sẫm" + "đèn chùm"; "rèm voan"; "đèn bàn chao vải"; sàn gỗ ("ghế cào sàn gỗ" C6, "gót giày gõ trên sàn gỗ" C8, "bánh vali lăn lạch cạch trên sàn gỗ" C10); khăn bàn trắng, đĩa trắng, ly trà ngọt (tiệc).

### 1.2 Ngoài nhà — hiên đêm (C10 25–30, C11) và tuyết (C50 0–13)

| Hướng | Cụm · giây | Thấy gì |
|---|---|---|
| "Máy đặt dưới lối đi trước nhà nhìn về mặt tiền" | C10 25–30; C11 0–5 | "bậc hiên trên cùng dưới đèn hiên vàng", "cửa chính sơn trắng khép lại… ô kính mờ sáng ánh đèn trong nhà", "cửa sổ phòng ăn sáng đèn sau rèm voan" |
| "Máy đặt ở bậc thềm dưới nhìn lên cửa chính" | C11 7–14 | Raven/Devin trong khung cửa, "ánh đèn trong nhà sau lưng" |
| "Máy đặt dưới lối đi nhìn về bậc thềm" | C11 14–17 | túi rác "đập xuống mặt bê tông", "bậc bê tông" |
| "Máy đặt ngang tầm mặt bà" | C11 17–24 | cận, nền bậc thềm |
| "Máy đặt ở mép hiên nhìn chéo qua bà về phía cửa sổ phòng ăn" | C11 24–27 | bà ngồi bậc dưới cùng **nửa trái**, cửa sổ phòng ăn sáng đèn **nửa phải**, sau rèm voan bóng khách quanh bánh kem |
| "Máy đặt cuối lối đi nhìn về mặt tiền" | C11 27–30 | toàn mặt tiền, máy lùi |
| "Máy đặt trên lối đi trước nhà nhìn về hiên" | C50 0–8 | "giữa cánh cửa trắng dán một tờ thông báo siết nhà khổ lớn màu trắng viền cam, dán bốn góc bằng băng keo trong"; "bậc tuyết"; "trời xám, tuyết lất phất" |
| "Máy đặt trên hiên nhìn ra đường" | C50 8–13 | Devin ở chân bậc, Charlene trên lối đi, "vali đen bóng của Devin ở mép trái khung" |

## 2. Suy ra bố cục

### 2.1 Nhà trong — một khối mở, 4 tường

Từ "nhìn về tủ buffet: đầu bếp mép trái, đầu cửa chính mép phải" (C4 3–5) → nhìn tường buffet thì bếp ở trái, cửa chính ở phải. Từ "nhìn về bếp: dãy buffet nửa phải" (C6 0–2) và "nhìn về cửa chính: dãy buffet tiền cảnh mép trái" (C4 11–15) → chiều kim đồng hồ: **BẾP → BUFFET → CỬA CHÍNH → SOFA**. Đặt la bàn: bếp Bắc, buffet Đông, cửa chính Nam (mặt tiền), sofa Tây.

```
                         BẮC — tường 1: BẾP (NIGHT_KITCHEN / BOWIE_KITCHEN_*)
   [cửa sổ + bồn rửa đôi] [bếp ga, lò + khăn sage] [tủ lạnh] [cửa gỗ hẹp → phòng giặt]
            [============ ĐẢO BẾP đá trắng vân xám, 2 đèn thả đồng ============]
                                                  ┌──────────────────┐
 TÂY — tường 4:   ┌─ đầu quặt L (phía bếp)        │ BÀN ĂN gỗ sẫm    │  ĐÔNG — tường 2:
 SOFA             │                               │ trục Bắc–Nam,    │  TỦ BUFFET gỗ
 2 cửa sổ cao     │ sofa L xám than   [bàn trà    │ đèn chùm hạt kính │  (tường đặc, sau
 rèm voan +       │ dựa tường Tây      kính]      │ dãy ghế phía sofa│  là garage),
 rèm nhung đỏ rượu│                               │ | dãy phía buffet │  tranh trừu tượng,
 đèn bàn chao vải └─ đầu phía cửa chính           └──────────────────┘  2 đèn bàn, lọ quạt
   [cầu thang gỗ sồi lan can trắng, lên dần về Tây ←] [CỬA CHÍNH trắng ô kính mờ] [console + gương tròn] [cửa sổ phòng ăn]
                         NAM — tường 3: CỬA CHÍNH (FOYER_STAIRS / BOWIE_*_FOYER)
                         → hiên có mái, 4 bậc bê tông, lối đi thẳng ra đường
```

Kiểm từng ràng buộc (panel k: phải = k+1, trái = k−1):

| Ràng buộc kịch bản | Bố cục cho ra | Đạt |
|---|---|---|
| Nhìn về cửa chính: console nửa trái, chân cầu thang nửa phải (C1, C2) | tường 3: console bên trái cửa, cầu thang bên phải cửa leo về phải | ✓ |
| Nhìn về cửa chính: sofa ở mép phải (C18 0–2, C33 0–2) | phải của tường 3 = tường 4 (sofa) | ✓ |
| Nhìn về cửa chính: dãy buffet tiền cảnh mép trái (C4 11–15) | trái của tường 3 = tường 2 (buffet + bàn) | ✓ |
| Nhìn về bếp: dãy buffet nửa phải (C4 24–27, C6 0–2) | phải của tường 1 = tường 2 | ✓ |
| Nhìn về bếp: sofa ở mép trái (C44 17–22, KẾT C44) | trái của tường 1 = tường 4 | ✓ |
| Nhìn về bếp: bồn rửa nửa trái, cửa phòng giặt đầu phải (C9) | tường 1 trái→phải: cửa sổ+bồn … cửa gỗ hẹp | ✓ |
| Nhìn về buffet: đầu bếp mép trái, đầu cửa chính mép phải (C4, C9 24–27) | trái tường 2 = tường 1, phải = tường 3 | ✓ |
| Nhìn về sofa: đầu sofa phía cửa chính mép trái, phía bếp mép phải (C18 9–12, C44 0–2) | trái tường 4 = tường 3, phải = tường 1 | ✓ |
| Cạnh sofa nhìn về bàn ăn thấy buffet sau lưng bà (C18 12–14, C19 19–22) | tường 2 đối diện tường 4 | ✓ |
| Từ hiên nhìn qua cửa mở thấy bàn tiệc (C10 22–25) | bàn ăn chạy dọc trục bếp–cửa chính, đầu Nam gần cửa | ✓ |
| Bóng sau kính mờ cửa chính (C2 26–30, C10 25–30) | cửa trắng có ô kính mờ cao | ✓ |
| "nắng trưa tràn vào" khi mở cửa (C48 0–2) | mặt tiền quay hướng Nam | ✓ |

Vì sao tường buffet không có cửa sổ: phía Đông là garage đôi gắn liền (đúng kiểu colonial mới ở PG County), phòng giặt ở góc Đông Bắc giữa bếp và garage — đúng vị trí "đầu phải bếp". Cầu thang chạy dọc mặt trong tường mặt tiền, lên về phía Tây tới chiếu nghỉ tầng hai (Raven "ngửa mặt lên lầu gọi").

### 2.2 Ngoài nhà — 4 hướng

Tường 1 = mặt tiền (máy trên lối đi nhìn Bắc), 2 = phía lối xe + garage (Đông), 3 = nhìn ra đường (Nam), 4 = sân bên (Tây). Cửa sổ phòng ăn ở bên PHẢI cửa chính nhìn từ đường (vì phòng ăn ở phía Đông trong nhà), dưới cùng mái hiên; garage trắng ở mép phải xa. C50 "Máy đặt trên hiên nhìn ra đường" = panel 3; trái của nó là lối xe (vali ở mép trái hợp lý).

## 3. Bảng ánh xạ câu kịch bản → panel

| Câu trong kịch bản | Cụm · giây | Panel |
|---|---|---|
| "Máy đặt phía đảo bếp nhìn về cửa chính", "Máy nhìn về cửa chính", "Cùng hướng" | C1 0–2, 6–9, 13–30; C2 0–8, 11–14, 20–23, 26–30; C3 0–8, 15–22, 25–30 | FOYER_STAIRS |
| "Máy đặt sau vai trái Marguerite nhìn về bếp", "Máy nhìn về bếp" | C1 2–6, 9–11; C2 8–11, 14–20, 23–26; C3 8–15, 22–25 | BOWIE_KITCHEN_DAY |
| Cửa chính mở, nền ngoài khung cửa (sáng) | C3 0–8 | BOWIE_STREET_DAY (ngoài cửa) |
| "Máy đặt phía bàn ăn nhìn về bếp", "Máy nhìn về bếp", "Máy đặt ở đầu bàn phía cửa chính nhìn dọc bàn về bếp", "Máy đặt ở dãy ghế phía sofa nhìn về bếp", "Máy đặt phía cửa chính nhìn về bếp" | C4 0–3, 8–11, 15–17, 24–27; C5 19–24, 27–30; C6 0–10, 15–18, 26–30; C7 0–6, 9–12, 26–30; C8 0–9, 19–22, 25–30; C9 0–7, 14–17, 19–24, 27–30; C10 0–6, 9–12, 19–22 | NIGHT_KITCHEN |
| "Máy đặt ngoài hiên nhìn qua cửa chính đang mở vào phòng"; "bậc thềm dưới nhìn lên cửa chính" (nền trong nhà sau khung cửa) | C10 22–25; C11 7–14 | NIGHT_KITCHEN (trong khung cửa) |
| "Máy đặt ở dãy ghế phía sofa nhìn về tủ buffet", "Máy nhìn về tủ buffet" | C4 3–8, 17–24, 27–30; C5 0–11, 13–16, 24–27; C6 12–15, 21–26; C7 6–9, 14–20, 22–26; C8 13–19, 22–25; C9 24–27; C10 12–15, 17–19 | NIGHT_DINING |
| "Máy đặt sau lưng bà ở đầu bàn phía bếp nhìn dọc bàn về cửa chính", "Máy nhìn dọc bàn về cửa chính", "Máy đặt cạnh bồn rửa nhìn ra phòng", "Máy nhìn ra phòng", "Máy nhìn về cửa chính" | C4 11–15; C5 11–13, 16–19; C6 10–12, 18–21; C7 12–14, 20–22; C8 9–13; C9 9–14, 17–19; C10 6–9, 15–17 | BOWIE_PARTY_FOYER |
| "Máy đặt dưới lối đi trước nhà nhìn về mặt tiền", "bậc thềm dưới nhìn lên cửa chính", "dưới lối đi nhìn về bậc thềm", "ngang tầm mặt bà", "mép hiên nhìn chéo qua bà về phía cửa sổ phòng ăn", "cuối lối đi nhìn về mặt tiền" | C10 25–30; C11 0–5, 7–30 | PORCH_NIGHT |
| "Máy đặt ở mép phòng ăn nhìn về cửa chính" | C18 0–4; C20 21–30 | BOWIE_FOYER_MESSY (+ BOWIE_STREET_DAY ngoài cửa mở) |
| "Máy đặt cạnh cửa chính nhìn vào bếp" | C18 4–6 | BOWIE_KITCHEN_MESSY (rổ đồ giặt ở tiền cảnh trái — ghi trong prompt) |
| "Máy đặt cạnh sofa nhìn về phía bàn ăn", "Cùng hướng" | C18 6–9, 12–14, 22–27; C19 8–11, 17–25; C20 9–13, 15–21 | BOWIE_DINING_MESSY |
| "Máy đặt sau vai phải bà nhìn về sofa", "Cùng hướng" | C18 9–12, 14–22, 27–30; C19 0–8, 11–17, 25–30; C20 0–9 | BOWIE_SOFA_MESSY |
| "Máy đặt ở mép phòng khách nhìn về bàn ăn", "Máy nhìn về bàn ăn" | C21 0–5, 7–13, 26–30 | BOWIE_DINING_NIGHT |
| "Máy đặt sau lưng ghế Raven nhìn sang Charlene" (hai người ngồi dãy phía buffet, Raven phía bếp) | C21 13–16 | BOWIE_FOYER_NIGHT |
| "Máy đặt ở mép phòng ăn nhìn về phòng khách" | C21 18–23 | BOWIE_SOFA_NIGHT |
| "Máy đặt ở góc sofa nhìn về cửa chính", "Cùng hướng" | C33 0–8 | BOWIE_FOYER_NIGHT |
| "Máy đặt giữa phòng khách / giữa phòng nhìn về sofa", "Máy nhìn về sofa" | C33 8–10, 13–24, 27–30; C44 0–9, 11–17 | BOWIE_SOFA_NIGHT |
| "Máy đặt cạnh sofa nhìn về phía bàn ăn", "Máy nhìn về phía bàn ăn" | C33 10–13, 24–27 | BOWIE_DINING_NIGHT |
| "Máy đặt gần cửa chính, lia theo Devin về phía bếp", "Máy nhìn về bếp" | C44 17–22, 28–30 | BOWIE_KITCHEN_NIGHT |
| "Máy đặt cạnh đảo bếp nhìn về cửa chính", "Máy nhìn về cửa chính", "Cùng hướng" | C48 0–2, 5–9, 13–16, 23–30 | BOWIE_FOYER_MESSY (+ BOWIE_STREET_DAY ngoài cửa mở, nắng trưa) |
| "Máy đặt trước bàn console nhìn về bếp", "Máy nhìn về bếp" | C48 2–5, 9–13, 16–23 | BOWIE_KITCHEN_MESSY |
| "Máy đặt trên lối đi trước nhà nhìn về hiên" | C50 0–8 | BOWIE_FRONT_SNOW |
| "Máy đặt trên hiên nhìn ra đường", "Cùng hướng" | C50 8–13 | BOWIE_STREET_SNOW |
| INSERT (C1 11–13, C9 7–9, C11 5–7, C20 13–15, C21 5–7/16–18/23–26, C44 9–11) | — | không cần panel (cận đồ vật / tay) |

Panel không cụm nào dùng trực tiếp (vẫn vẽ vì bảng luôn đủ 4 hướng, giữ không gian chung): BOWIE_DINING_DAY, BOWIE_SOFA_DAY (C1–C3 không nhìn về buffet hay sofa), BOWIE_PARTY_SOFA, BOWIE_FRONT_DAY (chỉ là gốc), BOWIE_STREET_NIGHT (chỉ khi C33 mở cửa lúc trời đã tối — nhưng bảng này có xe khách tiệc đỗ dọc lề, nên với C33 bỏ xe trong prompt), mọi panel lối xe / sân bên.

## 4. Khác biệt giữa các bảng (đồ cố định GIỐNG HỆT nhau)

- **DAY (gốc):** gọn — bà lau dọn mỗi ngày. Ánh sáng ngày qua rèm voan, đèn thả và đèn chùm tắt, một đèn bàn bật.
- **MESSY = DAY +** hộp đồ ăn đặt ngoài + túi giấy trên đảo, bát đĩa chưa rửa chất cao trong bồn, rổ khăn chưa giặt dưới chân cầu thang, thư chất đống trên console, giày dép vương quanh thảm, xấp thư + túi mua sắm trơn ở một đầu bàn ăn, hộp đồ ăn trên bàn trà, chăn nhàu + mũ satin đỏ rượu trên sofa, hai túi mua sắm bóng trơn dưới sàn. Không dời món nào.
- **NIGHT = MESSY +** đêm: cửa sổ xanh đen sau rèm voan, ô kính cửa tối; bật đèn chùm, 2 đèn thả đảo, 2 đèn buffet, đèn bàn sofa. Không đổi đồ.
- **PARTY = DAY +** đêm (như NIGHT) + bày tiệc: bàn nối bàn gấp dưới một khăn trắng dài từ gần đảo tới gần cửa, 14 chỗ (8 ghế kem + 6 ghế gấp trắng), đĩa trắng, khăn ăn trắng, ly trà đá, bình hoa thấp tím–trắng + nến ngắn; chùm bóng bay vàng kim–trắng không chữ buộc lưng ghế thứ 2 dãy phía buffet tính từ đầu bếp (ghế Charlene); trên buffet: bánh kem hai tầng trắng viền tím–vàng không chữ + bình thuỷ tinh trà đá có lát chanh; đảo bếp đầy khay giấy bạc và nồi đậy nắp. KHÔNG có đồ bừa.
- **FRONT_DAY (gốc ngoài):** đầu thu, cỏ xanh, cây non lá bắt đầu vàng, chậu cúc đỏ rượu trên bậc, sedan xám trong lối xe.
- **FRONT_NIGHT = FRONT_DAY +** đêm: đèn hiên bật, ô kính cửa + cửa sổ phòng ăn sáng đèn sau rèm voan, 2 cửa sổ lầu sáng, đèn đường, nhà đối diện có đèn hiên; thêm sedan/SUV đỗ dọc hai bên lề (xe khách dự tiệc).
- **FRONT_SNOW = FRONT_DAY +** sáng tháng Giêng xám, tuyết lất phất, lớp tuyết mỏng trên cỏ, mái, hàng rào, bậc, lối đi, sedan; vài dấu chân; cây trơ; bỏ chậu cúc; đèn hiên tắt, cửa sổ tối; tờ thông báo trắng viền cam không chữ đọc được dán bốn góc giữa cửa.

## 5. Bảy câu đời thực

### 5.1 Trong nhà — trạng thái "bà còn ở" (DAY, PARTY)

1. **Của ai:** Devin (38, nhân viên cấp trung Keystone Grid Systems ở Largo) và Raven (35, thích phô trương); mua bằng tiền cọc từ căn nhà Louisiana bà Marguerite bán. Tầng 2 (trung lưu) gồng lên trông như tầng 3, có nét tầng 4 phông bạt (bóng, vàng, túi mua sắm). Ở chưa lâu (vài năm). Bà Marguerite là người giúp việc không lương, ngủ giường gấp trong phòng giặt.
2. **Ở đâu thật:** Bowie, Prince George's County, Maryland (quận đa số da đen giàu nhất nước) — khu nhà mới xây 2000–2010 kiểu dọc Route 450 / Fairwood (tên đường hư cấu); colonial hai tầng mặt gạch, sườn ốp vinyl, garage đôi, hiên có mái, tầng trệt mở bếp–ăn–khách, cầu thang ngay lối vào.
3. **Dấu hiệu người trong cuộc (≥3):** chảo gang đã lên nước + chai tương ớt đỏ cạnh bếp (bếp của người nấu gốc Louisiana); lọ quạt giấy nhà thờ trên buffet; lưới ảnh gia đình khung đen dọc tường cầu thang; giày dép cởi ở thảm cửa. Tiệc: bình trà ngọt đá có chanh, nồi đậy nắp + khay giấy bạc trên đảo, bánh kem màu tím của Charlene (màu chữ ký), bàn nối bàn gấp + ghế gấp trắng cho khách nhà thờ.
4. **Đồ sinh hoạt (≥3):** khay chìa khoá + thư trên console (kịch bản C48), dây sạc điện thoại trên bàn trà, khăn lau sage trên cửa lò (C9), giày dép ở thảm.
5. **Nguồn sáng:** ngày — cửa sổ phòng khách rèm voan (Tây), cửa sổ trên bồn rửa, ô kính mờ cửa chính (Nam), một đèn bàn chao vải; đêm tiệc — đèn chùm hạt kính trên bàn, 2 đèn thả đồng trên đảo, 2 đèn bàn buffet chao kem, đèn bàn sofa, nến thấp. Cân trắng trung tính, ấm chỉ ở quanh đèn.
6. **Người nền:** ngày C1–C3 — không ai (chỉ nhân vật chính; Charlene là nhân vật). Tiệc C4–C10 — khoảng 10 khách bạn nhà thờ của Charlene, 60–75 tuổi, phần lớn là các bà đội mũ nhà thờ rộng vành, vest váy màu đậm (tím, xanh ngọc, đỏ mận, kem), vài ông vest tối, ngồi kín hai dãy, không thoại, chưa ai ăn; Sister Bernice (xanh ngọc) và Sister Pearl (đỏ mận) có tạo hình riêng.
7. **Tiếng nền:** ngày — tủ lạnh rì rì, xa xa máy thổi lá/xe chạy ngoài phố cuối tuần; tiệc — tiếng xì xào, đá chạm ly, dao nĩa, ghế cào sàn gỗ. Không nhạc (bài tiếng Trung luôn 无音乐).
- **Không được xuất hiện:** đồ Công giáo (thánh giá có tượng, chuỗi hạt, tượng Đức Mẹ), tranh Bữa Tiệc Ly có người, tiệm lưu niệm châu Phi, vàng chói kiểu biệt thự, bọc nhựa sofa / VHS, TV có chữ, chữ đọc được trên thư, túi, bánh, bóng bay; logo hãng; phòng như nhà mẫu (sạch như chưa ai ở); ánh vàng cam phủ cả khung.

### 5.2 Trong nhà — trạng thái "vắng bà" (MESSY, NIGHT)

1. **Của ai:** như trên, sau khi bà bị đuổi (26/09) — không còn ai dọn.
2. **Ở đâu thật:** như trên.
3. **Dấu hiệu người trong cuộc:** như trên + mũ satin đỏ rượu bỏ trên sofa (Raven tóc bob vuốt bóng — đời thật đội mũ satin khi ở nhà), túi mua sắm bóng không chữ (tầng 4 phông bạt).
4. **Đồ sinh hoạt:** hộp đồ ăn đặt ngoài, bát đĩa chưa rửa, rổ khăn chưa giặt, thư chưa mở chất đống, giày dép vương, dây sạc — bừa vừa phải, không bẩn (luật 4.1).
5. **Nguồn sáng:** ngày — như DAY (C18 14:00, C48 nắng trưa qua cửa mở); đêm — đèn chùm, đèn thả đảo, đèn buffet, đèn bàn sofa; cửa sổ tối.
6. **Người nền:** không ai.
7. **Tiếng nền:** tủ lạnh rì rì, điện thoại rung (C44), xe chạy xa ngoài phố; đêm có thể có TV dưới tầng hầm rất nhỏ — không cần.
- **Không được xuất hiện:** rác bẩn, chuột gián, đồ hỏng (đây là nhà khá giả thiếu người dọn, không phải nhà nghèo); chữ đọc được trên thư, hoá đơn, túi.

### 5.3 Ngoài nhà — mặt tiền (FRONT_DAY, PORCH_NIGHT, SNOW)

1. **Của ai:** nhà Devin–Raven (như trên); tháng Giêng 2027 ngân hàng siết nhà.
2. **Ở đâu thật:** đường cong trong khu nhà mới ở Bowie, hai bên là colonial mặt gạch gần như giống nhau (đúng kiểu subdivision PG County), cây đường còn non.
3. **Dấu hiệu người trong cuộc:** chuông cửa có camera (nguồn "receipts" quen thuộc của khán giả), chậu cúc đỏ rượu mùa thu trên bậc, xe khách nhà thờ đỗ kín hai bên lề đêm tiệc, khung bóng rổ di động ở lối xe nhà bên.
4. **Đồ sinh hoạt:** hai thùng rác có bánh xe cạnh garage, sedan xám trong lối xe, thảm chùi chân, dấu chân trên tuyết.
5. **Nguồn sáng:** ngày — nắng cao đầu thu trên mặt tiền hướng Nam; đêm — đèn lồng hiên đen bóng ấm, ánh đèn trong nhà qua ô kính mờ và rèm voan cửa sổ phòng ăn, một đèn đường trung tính lạnh; tuyết — trời xám phẳng, đèn hiên tắt.
6. **Người nền:** đêm — không ai ngoài sân; sau rèm cửa sổ phòng ăn là bóng ~10 khách đứng vỗ tay quanh bánh kem (C11 24–30, prompt thêm, im lặng). Tuyết — không ai (phố vắng).
7. **Tiếng nền:** đêm cuối tháng 9 — dế và châu chấu kêu, tiếng tiệc vọng ra nghèn nghẹt, xe xa trên đường lớn; tuyết — im phăng phắc, tiếng xẻng xúc tuyết đâu đó, bánh vali lộc cộc trên bậc tuyết.
- **Không được xuất hiện:** cột kiểu dinh thự miền Nam, cọ, hàng rào cọc trắng kiểu bưu thiếp, cờ hay biển có chữ, số nhà đọc được, tuyết xanh lam / kiểu thiệp Giáng sinh, đèn trang trí Giáng sinh rực rỡ, chữ trên tờ thông báo.

## 6. Mâu thuẫn và điểm cần quyết

1. **Giờ tiệc và "đêm" (C4–C11).** Kịch bản ghi 19:00–19:07 ngày 26/09/2026; ở Bowie mặt trời lặn khoảng 18:57 EDT, hoàng hôn dân dụng hết khoảng 19:22 — lúc 19:00–19:07 trời còn sáng xanh, trong khi kịch bản tả "bồn rửa đôi dưới cửa sổ tối" (C9 5–7) và "đêm" ở hiên (C10 25–30, C11). Bảng vẽ ĐÊM HẲN theo lời tả. Đề xuất: lùi giờ tiệc sang 19:30 (C4) → 19:37 (C11), hoặc chấp nhận "đêm" như ước lệ.
2. **C33 "tối" lúc 18:00 ngày 09/10.** Mặt trời lặn khoảng 18:37 → 18:00 còn nắng, mà C33 có "cửa chính mở" và "rèm voan kéo kín, đèn bàn chao vải sáng vàng". Đã xếp vào bảng NIGHT. Đề xuất đổi giờ thành ~19:30 (vẫn kịp "Tonight, Maison Bayou"), hoặc dùng bảng MESSY ngày + bật đèn.
3. **Rổ đồ giặt "dưới chân cầu thang" thấy từ "Máy đặt cạnh cửa chính nhìn vào bếp" (C18 4–6).** Chân cầu thang sát cửa chính (bắt buộc bởi C1–C2), nên rổ nằm sát máy, không nằm trong panel bếp. Giải: rổ đặt ở chân cầu thang trong bảng MESSY/NIGHT (panel cửa chính); prompt C18 4–6 ghi rổ ở tiền cảnh mép trái.
4. **Góc máy C11 24–27 "ở mép hiên nhìn chéo qua bà về phía cửa sổ phòng ăn".** Cửa sổ phòng ăn phải ở bên phải cửa chính nhìn từ đường (phòng ăn nằm phía Đông, tường buffet). Để bà ở nửa trái và cửa sổ ở nửa phải, máy phải đứng trên cỏ ở góc trước-trái hiên nhìn chéo lên phải; nếu đặt máy trên sàn hiên phía trái, bà sẽ rơi sang nửa phải. Ghi rõ chỗ đứng máy trong prompt.
5. **Phòng giặt bên trong (C10 0–4):** bóng đèn nhỏ, giường gấp hẹp sát máy giặt, vali vải nâu — sau cánh cửa đóng trong mọi bảng; cần ảnh đạo cụ / ảnh chèn riêng (đề xuất LAUNDRY_COT), không đưa vào bảng để cửa không bị vẽ mở ở C3–C9.
6. **Trạng thái bừa cho đêm và C48 là suy luận** từ câu C18 "Nhà bừa bộn từ ngày bà đi"; C21, C33, C44, C48 không tả bừa nhưng cũng không tả gọn. Nếu muốn đêm gọn: đặt `ve_tu` của BOWIE_HOUSE_NIGHT_BANG = BOWIE_HOUSE_DAY_BANG và bỏ câu clutter; nếu muốn C48 gọn: chuyển C48 sang bảng DAY.
7. **Đời thực — siết nhà sau 3 tháng (C50).** Ở Maryland, từ lúc ngừng trả góp tới khi ngân hàng lấy nhà thường mất nhiều tháng tới hơn một năm (thông báo trước khi khởi kiện, hoà giải…). Tờ dán cửa sau 3 tháng hơi nhanh — vẫn giữ (kịch bản cần), coi như thông báo của ngân hàng; tờ giấy không chữ đọc được nên không lộ chi tiết pháp lý. Chỉ ghi để người dùng biết, không sửa.
8. Không có mâu thuẫn trái–phải nào không giải được: mọi câu "mép trái / mép phải / nửa trái / nửa phải" trong 15 cụm khớp với một bố cục 4 tường duy nhất (mục 2.1).

## 7. Ghi chú kỹ thuật

- Mọi chuỗi tiếng Anh đã chạy regex `TU_CHI_NGUOI` của tool (`doc_kich_ban.py`) — 0 trúng; không có chữ người / thân thể / quần áo, không hãng, không chữ đọc được ("no lettering", "blank"), không đồ Công giáo, không immaculate/pristine/minimalist/showroom, không cinematic/golden hour/moody/warm tones/vintage film. Tránh cả "handle", "arm" (sofa arm), "crowd" vì regex cắt cả mệnh đề.
- `dung_bang_4_goc.py` (bản hiện tại) chỉ lấy **vế đầu** của mỗi tường (tới dấu `;`/`,` đầu tiên) để nhắc ở mép trái/phải — nên mọi `tuong` được viết "mốc chính trước, chi tiết sau dấu phẩy": vế đầu của tường buffet có cả bàn ăn + đèn chùm (để bàn hiện ở mép phải panel bếp và mép trái panel cửa chính như C4, C6 cần), vế đầu tường cửa chính có đủ console–cửa–chân cầu thang, vế đầu tường sofa có sofa L + cửa sổ rèm voan + bàn trà kính, vế đầu tường bếp có đảo đá + đèn thả.
- Độ dài `tuong` bảng gốc: trong nhà 59–68 từ (mỗi tường mang 5–6 món bắt buộc từ kịch bản), ngoài nhà 36–81 từ (mặt tiền dài nhất). Hơi quá mức ~45 từ, nhưng prompt bảng gốc dựng thử bằng `prompt_goc` = 5.930 ký tự (nhà trong) và 5.214 ký tự (mặt tiền), trong ngưỡng ~4.000–5.900 đã qua. Bảng biến thể chỉ gửi `khac_ban_goc` (3.000–3.700 ký tự); `tuong` của biến thể chỉ để lưu tham khảo.
