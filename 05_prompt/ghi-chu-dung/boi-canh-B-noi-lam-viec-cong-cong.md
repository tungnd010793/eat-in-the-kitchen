> Claude soạn ngày 02/11/2026 khi đọc trọn 70 cụm để dựng ảnh. Số dòng dạng (L123) hay "dòng 123" tính từ dòng `## KỊCH BẢN CHI TIẾT 70 CỤM` của `03_kich-ban-chinh-sua.md` (dòng 490 của file đó là L1); cộng 489 để ra số dòng trong 03.

# BỐI CẢNH NHÓM B — BẢNG 4 GÓC (EAT IN THE KITCHEN)

Nguồn: `kb.txt` (kịch bản chi tiết 70 cụm, bản 1 — 02/11/2026), đọc trọn các cụm C12–C17, C22–C32, C34–C41, C43–C47.
Dữ liệu máy đọc: `boi_canh_B.json` (cùng thư mục). File này là bằng chứng + lập luận + bảng ánh xạ + 7 câu đời thực.

## 0. Tóm tắt

| Bảng | Panel 1 · 2 · 3 · 4 (tường 1→4 theo chiều kim đồng hồ) | Trạng thái | Cụm |
|---|---|---|---|
| `GROCERY_BANG` | REGISTERS · MARKET · GROCERY_AISLES · GROCERY_DELI | ngày | 12–17, 26 (từ 15 s) |
| `KEYSTONE_CONF_BANG` | KEYSTONE_CONF_HEAD · KEYSTONE_CONF_WINDOWS · KEYSTONE_CONF_DOOR · KEYSTONE_CONF_CREDENZA | ngày | 22–26 (26 tới 15 s), 30–31, 45–47 (47 tới 13 s) |
| `KEYSTONE_CONF_NIGHT_BANG` | …_HEAD_NIGHT · …_WINDOWS_NIGHT · …_DOOR_NIGHT · …_CREDENZA_NIGHT | đêm, vẽ từ `KEYSTONE_CONF_BANG` | 44 (từ 22 s) |
| `KEYSTONE_FLOOR_BANG` | KEYSTONE_ELEVATOR · KEYSTONE_FLOOR_WINDOWS · KEYSTONE_FLOOR · KEYSTONE_CONF_GLASS | ngày | 27–29, 47 (từ 13 s) |
| `BASEMENT_BANG` | BASEMENT_BED · BASEMENT_DRESSER · BASEMENT_DOOR · BASEMENT_TABLE | chiều tối | 32 |
| `MAISON_BANG` | MAISON_RIVER · MAISON_BAR · MAISON_ENTRANCE · MAISON_BANQUETTE | đêm | 34–38 |
| `SALES_OFFICE_BANG` | SALES_ENTRANCE · SALES_SOFA · SALES_DESK · SALES_LAKE | ngày | 39–41, 43 (từ 16 s) |

Panel không có cú nào nhìn thẳng (chỉ hiện ở cạnh trái/phải của panel khác): GROCERY_DELI, BASEMENT_DRESSER, MAISON_BANQUETTE; ba panel đêm WINDOWS/DOOR/CREDENZA_NIGHT để sẵn.

Mâu thuẫn còn lại: không có mâu thuẫn cứng về mặt bằng. Có 5 chỗ lệch nhẹ đã xử lý (mục 1.4, 2.4, 3.4): vị trí cửa kính phòng họp so với "ghế thứ ba gần cửa kính"; "dãy bàn nhân viên" khi máy nhìn về thang máy; kệ đồ hộp và "dãy quầy ở mép trái" khi nhìn về cửa kính tiệm tạp hoá; hai "vách kính" khác nhau ở C45; nhóm Raven–Devin–Charlene đổi chỗ giữa C27 và C28 (dàn cảnh, không phải mặt bằng).

### Luật đọc trái/phải (tool `bang_4_goc.py`)

`tuong` = 4 tường theo chiều kim đồng hồ nhìn từ trên xuống. Panel k nhìn thẳng vào tường k; tường k+1 ở bên PHẢI khung, tường k−1 ở bên TRÁI, tường k+2 sau lưng máy. Sơ đồ dưới đây vẽ tường 1 ở trên, 2 bên phải, 3 ở dưới, 4 bên trái (đúng chiều kim đồng hồ).

Chuỗi `tuong` chỉ tả đồ vật, không tả ánh sáng (ánh sáng nằm ở `anh_sang`), để bảng đêm chép nguyên 4 tường của bảng ngày. Vị trí trong một tường được viết theo mốc ("the end nearest the entrance doors", "near the credenza corner"), không viết "left/right", vì cùng một chuỗi còn hiện ở cạnh trái/phải của hai panel khác.

---

## 1. TIỆM TẠP HOÁ FAIRWOOD, ROUTE 450, BOWIE (ngày) — `GROCERY_BANG`

### 1.1 Bằng chứng

**Vị trí máy và hướng nhìn**

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt phía khách nhìn về quầy thu ngân" / "phía khách nhìn về quầy" | C12 0–3, 14–17, 21–24, 27–30 · C13 0–2, 5–9, 12–14, 18–20, 24–30 · C14 0–6, 12–15, 23–30 · C15 0–2, 13–15, 24–27 · C16 7–11, 18–25 · C17 5–9, 13–16, 18–21 |
| "Máy đặt ở chỗ khách xếp hàng nhìn về dãy quầy" / "Máy nhìn về dãy quầy" | C26 15–24, 26–30 |
| "Máy đặt sau quầy 1 nhìn về cửa kính" | C12 3–14 · C14 19–23 · C16 15–18 · C17 9–13 |
| "Máy đặt sau vai phải bà nhìn về cửa kính" (KẾT ghi MARKET) | C17 26–30 |
| "Máy đặt sau quầy 1 nhìn ra cửa hàng" | C12 17–21, 24–27 · C13 2–5, 9–12, 14–18, 20–24 · C14 6–12, 15–19 · C17 23–26 |
| "Máy đặt sau quầy 2 nhìn ra cửa hàng" (KẾT ghi GROCERY_AISLES) | C15 2–12, 15–24, 27–30 · C16 0–7, 11–15, 28–30 · C17 0–5 |
| Chèn trên mặt quầy (tiền, hoá đơn, điện thoại nắp gập) | C16 25–28 · C17 16–18, 21–23 · C26 24–26 |

**Vật cố định**: quầy 1 và quầy 2 cạnh nhau (băng chuyền, máy quét bíp, máy quẹt thẻ, máy tính tiền, túi ni lông); cửa kính trượt tự động ra vỉa hè và bãi đỗ xe nắng; mặt kính nhìn ra vỉa hè (Charlene đứng ngoài, C17); đầu dãy kệ đồ hộp (C14 19–23); giỏ nhựa đỏ (Charlene); túi giấy đựng hàng (Inès).

**Trái / phải trong khung**

- C12 0–3: nhìn từ phía khách, "Marguerite đứng sau quầy 1 ở nửa phải khung … ở nửa trái khung, quầy 2 bên cạnh". Tương tự C15 0–2, C16 7–11.
- C14 26–30: "từ quầy 2 ngay sát tay phải bà (ngoài mép trái khung)" — bà quay mặt về máy, tay phải bà là bên trái khung → quầy 2 bên trái. Khớp.
- C26 15–18: "sau quầy thu ngân số 1 ở đầu phải dãy quầy (gần cửa kính tự động)"; C26 26–30: "đi về phía cửa kính tự động ở mép phải khung" → nhìn về dãy quầy thì cửa ở bên PHẢI.
- C12 6–8 (nhìn về cửa kính): "hất cằm về phía dãy quầy thu ngân (mép trái khung)".
- C14 19–23 (nhìn về cửa kính): "ở đầu dãy kệ đồ hộp mép trái khung, Charlene … quay lưng về dãy quầy".
- C16 15–18 (nhìn về cửa kính): "ở mép phải khung, vài khách xếp hàng".
- C15 2–5, C16 0–2 (sau quầy 2 nhìn ra): "vai gi-lê xanh lá của Marguerite ở mép trái khung (sau quầy 1)" → nhìn ra cửa hàng thì quầy 1 bên TRÁI quầy 2 (đúng phép lật 180°).
- C17 9–13: Inès "đứng ở đầu quầy 1", phía sau cô qua mặt kính cửa tự động là Charlene → đầu quầy 1 nằm giữa máy và cửa.

### 1.2 Mặt bằng suy ra

```
                    TƯỜNG 1 — REGISTERS (tường sau lưng thu ngân)
          ┌──────────────────────────────────────────────────────┐
          │      [quầy 2]          [quầy 1]                      │
          │   thu ngân đứng phía tường 1, khách đứng phía dưới   │
 TƯỜNG 4  │                         hàng khách xếp  →            │  TƯỜNG 2 — MARKET
 GROCERY_ │                                              kệ đồ   │  mặt tiền kính,
 DELI     │                                              hộp ◢   │  cửa trượt tự động
 (đồ nóng,│                                                      │  (ra vỉa hè, bãi xe)
 bánh,    │     ║ dãy kệ ║   ║ dãy kệ ║   ║ dãy kệ ║             │
 hải sản) └──────────────────────────────────────────────────────┘
                    TƯỜNG 3 — GROCERY_AISLES (lòng tiệm)
```

- Nhìn về tường 1 (REGISTERS): phải = tường 2 (cửa kính) → quầy 1 ở đầu gần cửa, bên phải ✓ C12, C26.
- Nhìn về tường 2 (MARKET): trái = tường 1 (dãy quầy) ✓ C12 6–8; phải = tường 3 (lòng tiệm, chỗ hàng khách xếp lan ra) ✓ C16 15–18.
- Nhìn về tường 3 (GROCERY_AISLES, từ sau quầy nhìn ra): trái = tường 2 → quầy 1 (gần cửa) bên trái quầy 2 ✓ C15, C16.
- Kịch bản chỉ có hai quầy → bảng vẽ đúng hai quầy, khỏi lẫn "quầy 2" với quầy thứ ba.

### 1.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "phía khách nhìn về quầy (thu ngân)", "chỗ khách xếp hàng nhìn về dãy quầy", "Máy nhìn về dãy quầy", chèn trên mặt quầy | `REGISTERS` |
| "sau quầy 1 nhìn về cửa kính", "sau vai phải bà nhìn về cửa kính" | `MARKET` |
| "sau quầy 1 nhìn ra cửa hàng", "sau quầy 2 nhìn ra cửa hàng" | `GROCERY_AISLES` |
| (không cú nào nhìn thẳng — cạnh trái REGISTERS, cạnh phải GROCERY_AISLES) | `GROCERY_DELI` |

### 1.4 Chỗ lệch và cách xử lý

1. C12 6–8 "dãy quầy thu ngân (mép trái khung)" trong khi máy đặt "sau quầy 1": máy đứng sát quầy thì dãy quầy phải ở sát máy chứ không ở xa. Xử lý: panel MARKET nhìn tường 2, cạnh trái là tường 1 → dãy quầy chạy dọc mép trái khung đúng như câu. "Sau quầy 1" hiểu là máy ở khu thu ngân, lùi về phía trong.
2. C14 19–23 "đầu dãy kệ đồ hộp mép trái khung", Charlene "quay lưng về dãy quầy": dãy kệ chính ở tường 3, không thể ở mép trái panel MARKET. Xử lý: đặt một kệ đầu dãy đồ hộp thấp ở góc tường 2 sát dãy quầy ("a low end display of canned goods in the corner beside the checkout counters"). Charlene đứng quay mặt vào kệ thì lưng quay về dãy quầy.
3. Cần kiểm (đời thực, không phải mặt bằng): kịch bản dùng "túi ni lông" ở quầy. Nếu luật túi mang về của Maryland / PG County năm 2026 đã cấm túi ni lông mỏng thì đổi thành túi giấy hoặc túi ni lông dày dùng lại. Tôi chưa kiểm chứng; bảng vẫn giữ "plastic bag carousels" theo kịch bản.

### 1.5 Bảy câu đời thực

1. **Của ai:** siêu thị khu phố do chủ địa phương làm (không phải chuỗi thật), trong dãy cửa hàng mặt tiền dọc Route 450. Khách là các gia đình trung lưu người da đen ở Bowie (tầng 1–2). Marguerite làm thu ngân lương tối thiểu được một tuần.
2. **Ở đâu thật:** Route 450 (Annapolis Road) qua Bowie, PG County. Dọc đường có các trung tâm mua sắm dải (siêu thị, tiệm giặt, tiệm tóc, quán carryout). Fairwood là khu nhà mới cạnh Route 450. Quận đa số người da đen, phần lớn trung lưu; gần Bowie có một HBCU (không nêu tên trên hình).
3. **Dấu hiệu người trong cuộc:** (a) quầy đồ nóng có mac and cheese, rau hầm, kệ bánh sweet potato pie và pound cake; (b) quầy hải sản có cua xanh hấp — dấu hiệu Maryland; (c) đầu dãy là khoai lang đóng hộp, bột ngô, bao gạo hạt dài; quầy rau có bó collard greens, đậu bắp, khoai lang (kịch bản: bà quét một hộp đậu bắp); (d) bảng ghim tờ rơi trống ở cửa (nhà thờ, thợ tết tóc, gia sư); (e) hũ quyên góp nhãn trống trên quầy 1.
4. **Đồ sinh hoạt:** giỏ nhựa đỏ chồng ở cửa, túi ni lông trên giá xoay, xô lau nhà vàng ở đầu một dãy kệ, xe đẩy trong bãi, thẻ giá trống.
5. **Nguồn sáng thật:** đèn LED trần trắng trung tính, nắng trưa qua mặt kính tiền sảnh, tủ mát và tủ đồ nóng sáng từ trong, hai đèn sưởi ấm trên tủ đồ nóng (nguồn ấm duy nhất).
6. **Người nền (không vẽ vào bảng):** sáng thứ Bảy 11h có 6–10 người, đa số người Mỹ gốc Phi, đủ tuổi:
   - bà cụ quấn khăn đầu in hoa (kịch bản), áo khoác mỏng;
   - cậu thanh niên đeo tai nghe (kịch bản C15), hoodie trường không chữ, jogger, sneaker trắng;
   - ông cụ đội mũ lưỡi trai cựu binh không chữ, áo khoác gió;
   - mẹ trẻ tóc tết knotless, áo nỉ + legging, đẩy xe hàng có bé ngồi;
   - cặp trung niên mặc áo thun đồng phục nhà thờ / hội không chữ;
   - nữ thu ngân trẻ ở quầy 2 (kịch bản): gi-lê xanh lá giống Marguerite, tóc locs buộc;
   - quản lý ca: polo xanh lá, thẻ tên trống.

   Họ xếp hàng, xem điện thoại, đổi giỏ sang tay kia (C15), che miệng cười không ra tiếng (C16). Không ai nhìn máy.
7. **Tiếng nền:** máy quét bíp, băng chuyền rì rì, túi ni lông sột soạt, cửa tự động trượt, bánh xe đẩy lạch cạch, loa gọi nhân viên xa nghe không rõ chữ. Không nhạc.

**Điều sai ở nơi này:** tên hoặc logo chuỗi thật; chữ trên biển giá, biển dãy kệ, biển "lane"; kính chống đạn ở quầy, song sắt, bảo vệ canh cửa (đây là ngoại ô trung lưu, không phải khu ổ chuột); kệ trống, đồ hỏng; dưa hấu hay gà rán bày làm trò; tuyết; Halloween bày lố (đầu tháng 10 chỉ vài quả bí ngô là đủ).

---

## 2. KEYSTONE GRID SYSTEMS — PHÒNG HỌP KÍNH (ngày + đêm) — `KEYSTONE_CONF_BANG`, `KEYSTONE_CONF_NIGHT_BANG`

### 2.1 Bằng chứng

**Vị trí máy và hướng nhìn**

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt ở cuối bàn (phía cửa kính) nhìn về đầu bàn", "Máy nhìn về đầu bàn" | C22 0–5, 9–12, 14–17, 27–30 · C24 9–11 · C25 8–11, 17–20 · C30 24–27 |
| "Máy đặt sau vai Devin nhìn về đầu bàn" | C45 5–9, 11–14, 17–26 · C46 0–6, 8–12, 17–27 · C47 7–10 |
| "Máy đặt giữa bàn họp nhìn về đầu bàn" (đêm) | C44 22–28 |
| "Máy đặt phía tủ thấp nhìn về dãy cửa sổ", "Máy nhìn về dãy cửa sổ" | C22 5–9, 12–14, 17–27 · C23 7–15, 20–23, 26–30 · C24 0–5, 11–16, 21–28 · C25 5–8, 24–30 · C26 0–8 · C30 2–4, 7–22 · C31 10–22, 26–30 |
| "phía tủ thấp nhìn về cuối dãy ghế gần cửa kính" | C25 11–17 |
| "Máy đặt giữa phòng nhìn về góc cửa sổ phía cửa kính" | C26 11–15 |
| "Máy đặt ở đầu bàn (cạnh ghế chủ toạ) nhìn về cửa kính" | C23 0–7 · C30 0–2 · C31 22–26 |
| "Máy đặt sau ghế chủ toạ nhìn về cửa kính" | C45 0–5, 14–17, 26–30 · C46 6–8, 12–15, 27–30 · C47 0–7, 10–13 |
| "sau dãy ghế phía cửa sổ / phía cửa sổ / sau góc đầu bàn phía cửa sổ nhìn về tủ thấp", "Máy nhìn về tủ thấp" | C23 15–20, 23–26 · C24 5–9, 16–21, 28–30 · C25 0–5, 20–24 · C26 8–11 · C30 4–7, 27–30 · C31 0–10 |

**Vật cố định**:

- bàn họp dài, mặt gỗ sáng (C22 9–12, C30 22–24); ghế chủ toạ ở đầu bàn;
- 3 ghế mỗi cạnh dài: Devin ở "ghế thứ ba gần cửa kính"; C30 "hai ghế ở giữa bỏ trống"; Inès "ghế giữa dãy phía tủ thấp";
- dãy cửa sổ kính ngoài trời nắng (C26 11–15 "nền cửa sổ kính nắng sáng");
- tủ thấp;
- cửa kính ở cuối bàn; bàn phụ cạnh cửa kính (Ashanti);
- vách kính nhìn ra dãy bàn nhân viên (C45–C47);
- đoàn đối tác ngồi sau lưng Inès (cần hàng ghế phụ dọc tủ thấp);
- đêm: "đèn trần chỉ bật một dãy" (C44).

**Trái / phải trong khung**

- C22 0–2 (nhìn đầu bàn): "dọc cạnh bàn phía cửa sổ ở mép phải khung … dãy ghế phía tủ thấp ở mép trái". Ashanti ở bàn phụ cạnh cửa kính "sau lưng máy".
- C22 5–9 (nhìn cửa sổ): "ở mép phải khung, gần cửa kính, Ashanti … vai vest xám than của Prentice ở mép trái".
- C23 0–3 (nhìn cửa kính): "Ashanti giữ cánh cửa kính mở ở mép phải khung … ở tiền cảnh mép trái … Charlene, Raven và Devin ngồi" (phía cửa sổ). C23 3–5: "Prentice vào khung từ mép phải, đi dọc cạnh bàn phía tủ thấp". C23 5–7: "Ashanti khép cửa kính ở mép phải".
- C23 15–20, C24 28–30, C25 0–2, C25 20–24, C31 0–2 (nhìn tủ thấp): "Prentice … ở mép phải khung".
- C23 26–30, C24 0–2, C26 0–2 (nhìn cửa sổ): Prentice mép trái, "Ashanti đứng ở bàn phụ cạnh cửa kính, mép phải xa".
- C25 11–14: "chỉ thẳng tay về phía bàn phụ cạnh cửa kính ở mép phải khung".
- C30 0–2 (nhìn cửa kính): "Devin … ghế thứ ba phía cửa sổ ở nửa trái khung; ở nửa phải khung, phía tủ thấp, Inès".
- C31 22–26 (nhìn cửa kính): "Prentice ở tiền cảnh mép trái … Devin … nửa trái khung, gần cửa".
- C45 0–2 (nhìn cửa kính): "Ashanti đứng cạnh bên trái ghế chủ toạ, sát vách kính hông, … tiền cảnh mép trái … sau vách kính, mờ: nhân viên văn phòng ở dãy bàn". C45 17–19 (nhìn đầu bàn): "Ashanti đứng cạnh bên trái ghế chủ toạ (mép phải khung)".
- C26 11–15: "bàn họp và mọi người ngoài khung bên trái".

### 2.2 Mặt bằng suy ra

```
                     TƯỜNG 1 — KEYSTONE_CONF_HEAD
                     màn hình tắt, ảnh trên không bãi container pin
          ┌──────────────────────────────────────────────┐
          │                [ghế chủ toạ]                  │
 TƯỜNG 4  │   ghế phụ      ┌──────────┐   Charlene        │  TƯỜNG 2
 CREDENZA │   (đoàn Pháp)  │  bàn họp │   Raven           │  WINDOWS
 tủ thấp  │   Inès (giữa)  │ gỗ sáng  │   Devin (ghế 3)   │  cửa sổ ngoài
          │                └──────────┘                   │
          │  ▯cửa kính       bàn phụ                       │
          └──────────────────────────────────────────────┘
                     TƯỜNG 3 — KEYSTONE_CONF_DOOR
                     vách kính trong + cửa (ra tầng văn phòng)
```

- Nhìn về đầu bàn (tường 1): phải = tường 2 (cửa sổ) ✓, trái = tường 4 (tủ thấp) ✓, sau lưng = tường 3 (cửa kính, tiếng gõ "sau lưng máy" C22 27–30) ✓.
- Nhìn về cửa kính (tường 3): trái = tường 2 (dãy ghế phía cửa sổ ở tiền cảnh trái) ✓, phải = tường 4 → cửa nằm ở góc phía tủ thấp ✓ C23.
- Nhìn về tủ thấp (tường 4): phải = tường 1 (Prentice ở ghế chủ toạ, mép phải) ✓.
- Nhìn về cửa sổ (tường 2): trái = tường 1 (Prentice mép trái) ✓, phải = tường 3. Bàn phụ dựa vách kính ở phía cửa sổ của cửa → ở mép phải và xa máy ✓ "mép phải xa".
- C45: Ashanti ở bên trái ghế chủ toạ (bên trái của Prentice khi ông nhìn xuống cuối bàn = phía cửa sổ) → nhìn cửa kính thì mép trái, nhìn đầu bàn thì mép phải ✓.

**Một bảng hay hai bảng với tầng điều hành?** Hai bảng riêng. Phòng họp là hộp kính khép kín, có bốn tường của chính nó; cú trong phòng nhìn đủ bốn phía. Tầng là khoảng mở, cũng được nhìn đủ bốn phía (thang máy, cửa sổ, dãy bàn, vách kính phòng họp). Hai nơi chỉ chung một vách kính có cửa; thứ thấy qua kính ở hai bên chỉ là nền mờ. Gộp lại thì một lưới 2×2 không chứa nổi tám hướng. Để hai bảng khớp nhau, tôi tả vật liệu giống hệt: thảm than, kính trong có dải mờ ngang giữa, tay nắm thép dài, bàn gỗ sồi sáng, ghế lưới đen. Hướng cũng khớp: tường 3 của phòng họp = tường 4 của tầng; cửa ở góc tủ thấp nhìn từ trong = đầu phía dãy bàn nhìn từ tầng (C47 21–25 "dãy bàn nhân viên ở mép trái khung") ✓.

**Bảng đêm** (`KEYSTONE_CONF_NIGHT_BANG`, `ve_tu` = bảng ngày): 4 tường chép nguyên, chỉ đổi ánh sáng. Cửa sổ tối có vài đèn bãi xe xa; chỉ dãy đèn trần trên đầu bàn bật; tầng văn phòng sau kính tối. Chỉ panel `KEYSTONE_CONF_HEAD_NIGHT` được dùng (C44 22–28).

### 2.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "cuối bàn (phía cửa kính) nhìn về đầu bàn", "Máy nhìn về đầu bàn", "sau vai Devin nhìn về đầu bàn" | `KEYSTONE_CONF_HEAD` |
| "giữa bàn họp nhìn về đầu bàn" (C44, đêm) | `KEYSTONE_CONF_HEAD_NIGHT` |
| "phía tủ thấp nhìn về dãy cửa sổ", "Máy nhìn về dãy cửa sổ", "phía tủ thấp nhìn về cuối dãy ghế gần cửa kính", "giữa phòng nhìn về góc cửa sổ phía cửa kính" (nửa phải panel) | `KEYSTONE_CONF_WINDOWS` |
| "đầu bàn (cạnh ghế chủ toạ) nhìn về cửa kính", "sau ghế chủ toạ nhìn về cửa kính" | `KEYSTONE_CONF_DOOR` |
| "sau dãy ghế phía cửa sổ / phía cửa sổ / sau góc đầu bàn phía cửa sổ nhìn về tủ thấp", "Máy nhìn về tủ thấp" | `KEYSTONE_CONF_CREDENZA` |

### 2.4 Chỗ lệch và cách xử lý

1. **Cửa kính ở đầu nào của tường 3.** C23 0–3 và 5–7 nói rõ cửa ở mép PHẢI khi nhìn từ đầu bàn, tức góc phía tủ thấp. Nhưng C22 0–2 "Devin … ghế thứ ba gần cửa kính" (Devin ngồi phía cửa sổ) và "Ashanti ở bàn phụ cạnh cửa kính … mép phải xa" khi nhìn về cửa sổ (C23 26–30, C24 0–2) lại gợi ý cửa ở phía cửa sổ. Xử lý: theo câu rõ nhất (C23) đặt cửa ở góc tủ thấp. Bàn phụ dựa vách kính ở phía cửa sổ của cửa, nên vẫn "cạnh cửa kính" và vẫn "mép phải xa". "Ghế thứ ba gần cửa kính" hiểu là ghế cuối bàn, gần vách kính.
2. **C45 0–2 có hai "vách kính".** "Sát vách kính hông" là tường 2 (cửa sổ ngoài, bên trái ghế chủ toạ). "Sau vách kính … nhân viên ở dãy bàn" là tường 3. Không mâu thuẫn, nhưng người viết prompt phải tách đúng.
3. **C26 11–15** "giữa phòng nhìn về góc cửa sổ phía cửa kính … bàn họp ngoài khung bên trái": máy ở khoảng trống cuối bàn nhìn về góc tường 2–3, bàn ở phía đầu bàn nên nằm bên trái ✓. Dùng nửa phải panel WINDOWS.
4. Tường 1 (màn hình tắt, ảnh trên không bãi container pin, chậu lưỡi hổ) kịch bản không tả; tôi thêm cho đúng ngành của công ty.

### 2.5 Bảy câu đời thực (phòng họp + tầng điều hành)

1. **Của ai:** Keystone Grid Systems, công ty kỹ thuật lưu trữ năng lượng pin cỡ vừa (hư cấu), thuê tầng trên của một toà văn phòng thấp tầng. Prentice là sếp. Nhân viên là dân văn phòng chuyên môn trung lưu (tầng 2–3). Phòng họp kính dùng tiếp đối tác.
2. **Ở đâu thật:** Largo, PG County — trung tâm hành chính của quận, quanh ga Metro Downtown Largo, nhiều office park thấp tầng, bãi xe rộng, cây lá đổi màu tháng 10. Không có skyline.
3. **Dấu hiệu người trong cuộc:**
   - phòng họp: tranh vải ghép kiểu quilt màu chàm – gỉ sắt (nghệ thuật Mỹ gốc Phi ở công sở); bát kẹo bạc hà gói trên tủ thấp; ảnh trên không bãi container pin (dấu hiệu ngành, để người trong nghề nhận ra);
   - tầng: trên bàn có ảnh gia đình, cờ nỉ hai màu không chữ (HBCU), quạt giấy nhà thờ cán gỗ cắm trong cốc bút, chậu xương rồng nhỏ (bàn Devin, C47).
4. **Đồ sinh hoạt:** bình nước, cốc, phích cà phê, xấp bìa hồ sơ trên bàn phụ, rèm cuốn kéo nửa chừng; ở tầng thêm cốc, xấp giấy, máy in chung.
5. **Nguồn sáng thật:** ngày là nắng qua cửa sổ + đèn âm trần trắng trung tính, ở tầng thêm đèn bàn đồng ở quầy lễ tân; đêm là một dãy đèn trần trên đầu bàn, cửa sổ tối, đèn bãi xe xa.
6. **Người nền:**
   - nhân viên ở dãy bàn: 8–12 người, đa số người Mỹ gốc Phi, xen vài người da trắng, Latino, châu Á, tuổi 25–60. Họ mặc business casual: sơ mi oxford, áo len mỏng, blazer, váy liền, quần tây, thẻ nhân viên dây xanh (cùng loại với Devin). Họ gõ phím, đeo tai nghe họp; ở C45–C47 thì ngẩng lên rồi đứng dậy nhìn;
   - đoàn đối tác Pháp (kịch bản): 2 nam vest xám sơ mi trắng, 1 nữ tóc búi gọn vest đen;
   - bảo vệ toà nhà (kịch bản): polo xanh than, bộ đàm;
   - lễ tân: kịch bản không có. Đề xuất để quầy trống (lễ tân đi vắng) để các cú C27–C28 khỏi có thêm một người nền đứng ngay sau lưng nhóm Raven. Nếu muốn đúng đời hơn thì thêm một nữ lễ tân 40 tuổi, blazer xanh than, tai nghe điện thoại, cúi nhìn màn hình;
   - đêm (C44): không ai ngoài Prentice.
7. **Tiếng nền:** điều hoà ù nhẹ, gõ phím xa qua kính, ghế xoay kẽo kẹt, máy in, chuông thang máy "ding" (ở tầng). Đêm chỉ còn tiếng điều hoà. Không nhạc.

**Điều sai:** tên hoặc logo công ty trên kính, tường, màn hình, thẻ nhân viên; màn hình bật có chữ; skyline cao tầng kiểu Manhattan; toàn nhân viên da trắng ở nền (PG County đa số da đen); nội thất vàng chói; nắng ở cảnh đêm.

---

## 3. KEYSTONE — TẦNG ĐIỀU HÀNH (sảnh, thang máy, lễ tân, dãy bàn) — `KEYSTONE_FLOOR_BANG`

### 3.1 Bằng chứng

**Vị trí máy và hướng nhìn**

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt giữa sảnh nhìn về thang máy", "sau lưng Raven nhìn về thang máy", "Máy nhìn về thang máy", "giữa sàn nhìn về thang máy" | C27 0–2, 10–13, 20–25 · C28 17–21 · C47 25–30 |
| "Máy đặt sau vai phải bà nhìn ra giữa sảnh" | C27 2–10, 13–20, 25–28 |
| "Máy đặt gần thang máy nhìn về dãy bàn nhân viên" | C47 13–21 |
| "Máy đặt phía dãy cửa sổ nhìn về phòng họp kính", "sau vai phải bà nhìn về phòng họp kính", "Máy nhìn về phòng họp kính", "giữa sàn nhìn về phòng họp kính" | C27 28–30 · C28 0–8, 14–17 · C29 8–13, 17–22, 25–30 · C47 21–25 |
| "Máy đặt trước cửa phòng họp nhìn về dãy cửa sổ", "giữa sàn nhìn về dãy cửa sổ", "Máy nhìn về dãy cửa sổ" | C28 8–14, 21–30 · C29 0–8, 13–17, 22–25 |

**Vật cố định:** thang máy cửa thép; quầy lễ tân; dãy bàn nhân viên; dãy cửa sổ kính với "một bàn trống sát cửa sổ"; phòng họp kính có cửa kính; sàn thảm (C28 24–27).

**Trái / phải trong khung**

- C27 0–2 (nhìn thang máy): "ở nửa phải khung, cạnh quầy lễ tân, Raven, Devin và Charlene".
- C27 2–6, 16–20, 25–28 (nhìn ra giữa sảnh): "sau lưng họ: nhân viên văn phòng ở dãy bàn". C27 25–28: "Devin liếc nhanh về mép phải khung, phía phòng họp kính (ngoài khung)".
- C27 28–30 (từ phía cửa sổ nhìn phòng họp): "ở mép phải khung, bà, Raven, Devin, Charlene".
- C28 0–2 (nhìn phòng họp): "Devin, Raven, Charlene ngoài khung bên trái". C28 14–17: "nhìn Devin một nhịp dài (ngoài khung bên trái)".
- C28 8–11 (nhìn cửa sổ): "ở mép phải khung Devin". C28 21–24: "Devin đứng một mình ở mép phải khung".
- C47 13–15 (nhìn dãy bàn): "vách kính phòng họp ở mép phải khung". C47 18–21: "phòng họp kính (mép phải khung, xa)".
- C47 21–25 (nhìn phòng họp): "dãy bàn nhân viên ở mép trái khung".
- C28 17–19 (nhìn thang máy): "Raven và Charlene đi qua trước dãy bàn nhân viên về phía thang máy".

### 3.2 Mặt bằng suy ra

```
                    TƯỜNG 1 — KEYSTONE_ELEVATOR
                    [thang máy][thang máy]   [quầy lễ tân]
          ┌──────────────────────────────────────────────┐
          │                                               │
 TƯỜNG 4  │             sảnh mở (nhóm Raven chặn bà)      │  TƯỜNG 2
 KEYSTONE │                                     ▭ bàn sát │  KEYSTONE_FLOOR_WINDOWS
 _CONF_   │  ▯cửa                               ▭ cửa sổ  │  dãy cửa sổ,
 GLASS    │  vách kính                          ▭ (bàn    │  hàng bàn sát kính
 phòng họp│                                       trống)  │
          │   ▭▭▭  ▭▭▭  ▭▭▭  dãy bàn nhân viên            │
          └──────────────────────────────────────────────┘
                    TƯỜNG 3 — KEYSTONE_FLOOR
```

- Nhìn thang máy (tường 1): phải = tường 2 → lễ tân ở nửa phía cửa sổ ✓ C27 0–2.
- Nhìn ra giữa sảnh = tường 3 (dãy bàn) ✓; phải = tường 4 (phòng họp) ✓ C27 25–28, C47 13–21.
- Nhìn phòng họp (tường 4): trái = tường 3 (dãy bàn) ✓ C47 21–25; phải = tường 1 (thang máy) ✓ C27 28–30.
- Nhìn cửa sổ (tường 2): phải = tường 3 (Devin đứng phía dãy bàn) ✓ C28 8–11, 21–24; sau lưng = tường 4 (Prentice trước cửa phòng họp "sau lưng máy") ✓ C28 KẾT, C29 KẾT.

### 3.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "giữa sảnh / giữa sàn nhìn về thang máy", "sau lưng Raven nhìn về thang máy", "Máy nhìn về thang máy" | `KEYSTONE_ELEVATOR` |
| "trước cửa phòng họp nhìn về dãy cửa sổ", "giữa sàn nhìn về dãy cửa sổ", "Máy nhìn về dãy cửa sổ" | `KEYSTONE_FLOOR_WINDOWS` |
| "sau vai phải bà nhìn ra giữa sảnh", "gần thang máy nhìn về dãy bàn nhân viên" | `KEYSTONE_FLOOR` |
| "phía dãy cửa sổ nhìn về phòng họp kính", "sau vai phải bà nhìn về phòng họp kính", "(giữa sàn) nhìn về phòng họp kính" | `KEYSTONE_CONF_GLASS` |

Mã `KEYSTONE_FLOOR` của bản nháp `02` gắn ở KẾT C47, đó là khung cửa thang máy khép. Bây giờ khung đó thuộc `KEYSTONE_ELEVATOR`. Tên `KEYSTONE_FLOOR` giữ cho hướng dãy bàn, là phần "tầng" chính của C47 13–25.

### 3.4 Chỗ lệch và cách xử lý

1. C28 17–19: máy nhìn về thang máy mà Raven và Charlene "đi qua trước dãy bàn nhân viên". Dãy bàn chính ở tường 3, sau lưng máy. Xử lý: thêm một hàng bàn sát cửa sổ ở tường 2. Hàng này hiện ở cạnh phải panel ELEVATOR, và cũng chính là chỗ có "bàn trống sát cửa sổ" của C28–C29.
2. Nhóm Raven–Devin–Charlene: ở C27 28–30 họ đứng mép phải (phía thang máy); ở C28 0–2 và 8–11 họ ở phía dãy bàn. Đây là dàn cảnh (họ dịch chỗ khi Prentice bước ra), không phải mặt bằng. Giữ nguyên.
3. Kiến trúc: cửa sổ ngoài của phòng họp nằm cùng phía với tường thang máy của tầng. Nghĩa là phòng họp ở góc toà nhà, nhô ra sau tường thang máy. Hai bảng không bao giờ thấy cùng lúc nên không ảnh hưởng.

---

## 4. PHÒNG HẦM THUÊ Ở LANDOVER (chiều tối) — `BASEMENT_BANG`

### 4.1 Bằng chứng

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt cạnh giường sắt nhìn về cửa", "Máy nhìn về cửa" | C32 0–4, 11–14, 18–30 |
| "Máy đặt ở cửa nhìn vào phòng", "Máy nhìn vào phòng" | C32 4–9, 14–18 |
| "Chèn — Máy nhìn về bàn gấp" | C32 9–11 |

**Vật cố định**:

- cửa gỗ mở vào; công tắc cạnh cửa ("với tay bật công tắc"); bóng đèn trần trơ;
- cầu thang bê tông ngoài trời đi lên, "khoảng trời tối ở đầu cầu thang";
- trần thấp, tường bê tông;
- giường sắt; vali vải nâu da bò có dây buộc dựng ở chân giường;
- bàn gấp: bếp điện một họng nguội, nồi nhỏ, ấm nước, đúng hai cái bát úp, khung ảnh gỗ kính nứt;
- cửa sổ hầm tối mờ (sau lưng bà khi máy nhìn vào phòng).

**Trái / phải trong khung**: C32 2–4 (nhìn về cửa) "bà bước sâu vào phòng ở nửa trái khung"; C32 14–18 (nhìn vào phòng) "cửa sổ hầm tối mờ sau lưng"; C32 4–6 "bà đi tới chân giường sắt … rồi quay lại, mặt về máy".

### 4.2 Mặt bằng suy ra

```
                    TƯỜNG 1 — BASEMENT_BED
                    cửa sổ hầm nhỏ trên cao
          ┌──────────────────────────────┐
          │        [giường sắt]          │
 TƯỜNG 4  │        [  chăn ghép ]         │  TƯỜNG 2
 BASEMENT │ bàn    [vali ở cuối giường]   │  BASEMENT_DRESSER
 _TABLE   │ gấp                           │  tủ nhựa, Kinh Thánh,
          │                               │  thánh giá gỗ, sưởi
          └────────────▯ cửa gỗ ──────────┘
                    TƯỜNG 3 — BASEMENT_DOOR (cầu thang bê tông đi lên)
```

- Nhìn về cửa (tường 3) từ cạnh giường: trái = tường 2 → bà bước sâu vào phòng ở nửa trái ✓.
- Nhìn vào phòng (tường 1): cửa sổ hầm sau lưng bà khi bà đứng ở cuối giường ✓; vali ở cuối giường ✓.
- Bàn gấp ở tường 4 (cú chèn).

### 4.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "ở cửa nhìn vào phòng", "Máy nhìn vào phòng" | `BASEMENT_BED` |
| (không cú nào nhìn thẳng) | `BASEMENT_DRESSER` |
| "cạnh giường sắt nhìn về cửa", "Máy nhìn về cửa" | `BASEMENT_DOOR` |
| "Chèn — Máy nhìn về bàn gấp" | `BASEMENT_TABLE` |

### 4.4 Chỗ lệch

Không có mâu thuẫn. Khung ảnh căn nhà vàng nhạt là đạo cụ chính; nếu có ảnh đạo cụ thì ảnh đạo cụ thắng chi tiết vẽ trong bảng.

### 4.5 Bảy câu đời thực

1. **Của ai:** phòng hầm của một chủ nhà người da đen lớn tuổi, cho thuê theo tháng 400 đô (rẻ, kiểu chỗ quen giới thiệu, không có hợp đồng công ty). Marguerite mới ở 9 ngày (bị đuổi 26/09, cảnh ngày 05/10), nên đồ của bà rất ít: một vali, túi cardigan, khung ảnh. Giường sắt, bàn gấp, tủ nhựa là đồ cũ của chủ nhà. Tầng 0–1.
2. **Ở đâu thật:** Landover, PG County, trong vành đai Beltway — khu garden apartment gạch thập niên 1960 và nhà gạch nhỏ (ranch, duplex). Có lối xuống hầm riêng bằng cầu thang bê tông ngoài trời ("English basement").
3. **Dấu hiệu người trong cuộc:** Kinh Thánh bìa da sờn trên tủ; thánh giá gỗ trơn treo tường (khớp dây chuyền thánh giá vàng của bà); chăn ghép mảnh tự khâu; vỏ gối lụa màu champagne (phụ nữ da đen giữ tóc khi ngủ). Đủ 3 nhóm theo `kiem_doi_thuc.py`.
4. **Đồ sinh hoạt:** sạc điện thoại nắp gập cắm ổ điện, kính đọc sách, máy sưởi nhỏ (tháng 10), rổ khăn gấp, bao gạo, chổi, thảm chùi chân.
5. **Nguồn sáng thật:** một bóng đèn trần trơ (nguồn ấm duy nhất), ánh chạng vạng xanh qua cửa sổ hầm và lối cầu thang.
6. **Người nền:** không ai trong hình. Chủ nhà ở tầng trên chỉ có mặt bằng tiếng.
7. **Tiếng nền:** TV nhỏ vọng từ tầng trên, bước chân trên sàn gỗ trên đầu, tủ lạnh mini ù, xe chạy xa ngoài đường. Không nhạc.

**Điều sai:** rác, chuột, gián, tường mốc tróc nặng, song sắt cửa sổ (nghèo nhưng sạch — mục 4.1); tối quá không thấy mặt; đèn LED dây, đồ của người trẻ; tượng thánh hay chuỗi tràng hạt (giữ thánh giá gỗ trơn, không làm đậm yếu tố Công giáo khi phim chưa xác lập); chữ "the projects", "section 8" trong mô tả.

---

## 5. NHÀ HÀNG MAISON BAYOU (đêm) — `MAISON_BANG`

### 5.1 Bằng chứng

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt giữa lối đi nhìn về vách kính", "Máy nhìn về vách kính" | C34 0–2, 5–7, 16–19, 25–28 · C35 6–9, 19–21 · C36 7–14, 19–21, 27–30 |
| "Máy đặt giữa lối, sau lưng ba người, nhìn về vách kính" | C36 0–2 |
| "Máy đặt sau lưng Inès nhìn về vách kính" | C37 0–2 · C38 6–8 (+ "Máy nhìn về vách kính" C37 8–11, 20–26 · C38 11–18, 27–30) |
| "Máy đặt cạnh bàn bà nhìn về cửa vào", "Máy nhìn về cửa vào" | C34 2–5, 7–16, 19–25, 28–30 · C35 0–6, 9–19, 21–25, 28–30 · C36 2–7, 14–19, 21–27 |
| "Máy đặt sau lưng bà nhìn về phía cửa vào", "Máy nhìn về phía cửa vào" | C37 2–8, 11–20, 26–30 · C38 0–6, 8–11, 18–21, 24–27 |
| "Máy đặt giữa phòng nhìn về quầy bar" | C35 25–28 |
| "Máy đặt ngang bàn nhìn về quầy bar" | C38 21–24 |

**Vật cố định**:

- vách kính sông ("sông đêm lấp lánh mờ sau lưng"); bàn hai người của bà (lưng bà về vách kính);
- lối đi giữa các bàn; khách ăn tối ở các bàn;
- quầy bar (Inès ở "đầu kia quầy bar");
- bục tiếp tân (quản lý đứng ở đó, C35 0–2); cửa gỗ đôi (C36 24–27);
- nến giữa bàn (C37 13–17 "chân nến", C38 21–24 "ánh nến lay"); khăn bàn trắng.

**Trái / phải trong khung**

- C34 2–5 (nhìn cửa vào): Devin ở mép trái ("bên phải cô"), Charlene mép phải. Sau lưng họ: khách ở các bàn.
- C35 28–30 (nhìn cửa vào): "cùng quay đầu về phía quầy bar (mép trái khung)".
- C36 0–2 (nhìn vách kính): "Inès … cạnh bàn bà ở mép phải khung (phía quầy bar)".
- C36 2–4, 14–19 (nhìn cửa vào): Inès / quầy bar "ngoài khung bên trái".
- C38 21–24 (nhìn quầy bar): "Marguerite ở mép trái khung … Inès ở mép phải khung".

### 5.2 Mặt bằng suy ra

```
                    TƯỜNG 1 — MAISON_RIVER (vách kính sông)
          ┌──────────────────────────────────────────────┐
          │  ▭ ▭ [bàn bà] ▭ ▭   bàn đôi sát kính         │
 TƯỜNG 4  │                                               │  TƯỜNG 2
 MAISON_  │      ○   ○   ○   bàn khách khăn trắng         │  MAISON_BAR
 BANQUETTE│      ○   ○   ○      (lối đi giữa)            │  quầy bar dài,
 gạch,    │                                               │  Inès ở đầu kia
 băng ghế │                                               │
          └──────────── [bục tiếp tân] ▯▯ cửa gỗ đôi ──────┘
                    TƯỜNG 3 — MAISON_ENTRANCE
```

- Nhìn vách kính (tường 1): phải = tường 2 (quầy bar) ✓ C36 0–2.
- Nhìn cửa vào (tường 3): trái = tường 2 (quầy bar) ✓ C35 28–30, C36 2–4, 14–19.
- Nhìn quầy bar (tường 2): trái = tường 1 → bà (lưng về kính) ở mép trái ✓; phải = tường 3 → Inès (lưng về phía cửa vào) ở mép phải ✓ C38 21–24.

### 5.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "nhìn về vách kính (sông)", "giữa lối (sau lưng ba người) nhìn về vách kính", "sau lưng Inès nhìn về vách kính" | `MAISON_RIVER` |
| "giữa phòng / ngang bàn nhìn về quầy bar" | `MAISON_BAR` |
| "cạnh bàn bà nhìn về cửa vào", "Máy nhìn về cửa vào", "sau lưng bà nhìn về phía cửa vào" | `MAISON_ENTRANCE` |
| (không cú nào nhìn thẳng) | `MAISON_BANQUETTE` |

### 5.4 Chỗ lệch

Không có. Mọi câu trái/phải về quầy bar đều khớp khi quầy bar ở tường 2.

### 5.5 Bảy câu đời thực

1. **Của ai:** Inès Diallo (giàu thật, tầng 3) làm chủ một nhà hàng Creole Louisiana sang. Quản lý vest đen ria mảnh, bảo vệ vest đen tai nghe (kịch bản).
2. **Ở đâu thật:** bờ sông Potomac phía PG County (khu ăn uống ven sông ở Oxon Hill). Ăn tối thứ Sáu ở nhà hàng sang của chủ người da đen là sinh hoạt quen của tầng trung – thượng lưu PG County.
3. **Dấu hiệu người trong cuộc:**
   - ảnh đen trắng đầm lầy cây bách và nhà gỗ Creole (gốc Louisiana của món ăn và của chính Marguerite);
   - đèn kiểu đèn khí New Orleans, sắt rèn, gạch cũ;
   - góc sân khấu nhỏ có contrabass và bộ trống đang nghỉ — tối thứ Sáu thường có ban nhạc jazz / R&B;
   - bàn đầy khách da đen ăn mặc chỉn chu, đi tiệc sinh nhật, kỷ niệm (ở người nền).
4. **Đồ sinh hoạt:** chồng thực đơn bìa da ở bục tiếp tân, ly úp trên giá bar, khăn ăn gấp, nến cháy dở, bình lắc cocktail.
5. **Nguồn sáng thật:** nến thuỷ tinh thấp trên từng bàn, đèn tường đồng, ba đèn thả và kệ chai chiếu hậu ở bar. Kính sông tối, phản chiếu đèn bờ bên kia.
6. **Người nền:** tối thứ Sáu 20h có khoảng 25–35 thực khách, đa số người Mỹ gốc Phi trung – thượng lưu:
   - cặp hẹn hò: váy liền màu jewel tone, blazer, sơ mi lụa;
   - nhóm bạn gái mừng sinh nhật: đầm satin;
   - cặp trung niên kỷ niệm cưới;
   - phục vụ: sơ mi trắng, gi-lê đen, tạp dề dài đen kiểu bistro (kịch bản: "phục vụ dừng lại nhìn", "đứng dọc lối nhìn theo");
   - một bartender, quản lý, bảo vệ.

   Họ ăn, nâng ly, nói khẽ. Khi Raven to tiếng thì vài bàn quay lại (kịch bản).
7. **Tiếng nền:** dao nĩa chạm đĩa, rì rầm nói chuyện, đá lắc trong bình ở bar, ly chạm. Không nhạc — ban nhạc đang nghỉ, khớp luật `无音乐`.

**Điều sai:** tên "Maison Bayou" trên tường, cửa, thực đơn; mặt nạ voodoo, phù thuỷ, cá sấu nhồi bông, hạt Mardi Gras khắp nơi (biếm hoạ Louisiana); đèn chùm vàng chói; khách toàn da trắng; skyline cao tầng bên kia sông; dưa hấu, gà rán.

---

## 6. VĂN PHÒNG BÁN HÀNG KHU CÓ CỔNG, MITCHELLVILLE (ngày) — `SALES_OFFICE_BANG`

### 6.1 Bằng chứng

| Câu kịch bản | Cụm · giây |
|---|---|
| "Máy đặt cạnh bàn tiếp khách nhìn về cửa vào", "Máy nhìn về cửa vào" | C39 0–2, 7–9 |
| "Máy đặt sau bàn (tiếp khách) nhìn về cửa vào" | C39 12–15, 21–30 · C40 0–8, 18–21, 25–30 · C41 28–30 · C43 16–18, 21–28 |
| "Máy đặt giữa phòng nhìn về sofa chờ", "Máy nhìn về sofa chờ", "sau vai bà nhìn về sofa chờ" | C39 2–7, 15–18 · C41 0–11, 25–28 |
| "Máy đặt trước bàn nhìn về bàn tiếp khách", "Máy nhìn về bàn tiếp khách" | C39 9–12, 18–21 · C40 8–18, 21–25 · C43 18–21 (+ chèn C43 28–30) |
| "Máy đặt sau vai Devin nhìn về cửa kính ra hồ", "Máy nhìn về cửa kính ra hồ" | C41 11–25 |

**Vật cố định**:

- cửa kính ra vỉa hè; thảm chùi chân;
- sofa chờ màu kem;
- bàn tiếp khách trắng: màn hình máy tính quay nghiêng, bàn phím, chuột, ngăn kéo (chìa khoá), điện thoại bàn;
- mô hình khu nhà dưới hộp kính "sau lưng cô";
- cửa kính ra hồ; vỉa hè nắng, "con đường của khu".

**Trái / phải trong khung**

- C39 0–2 (nhìn cửa vào): "ở mép phải khung, trên sofa chờ màu kem, Raven và Devin".
- C39 2–4 (nhìn sofa): "hất cằm về phía cửa (mép trái khung)". C39 15–18: "nhân viên nhà đất … ngồi sau bàn ở mép phải khung".
- C39 7–9, 21–30, C40 0–2 (nhìn cửa vào): Raven "ở mép phải khung (phía sofa)".
- C41 0–2, 25–28 (nhìn sofa): bàn tiếp khách / nhân viên ở mép phải, cửa ở mép trái.
- C41 21–25 (nhìn cửa kính ra hồ): "đi khỏi khung về phía cửa vào (mép phải khung)".

### 6.2 Mặt bằng suy ra

```
                    TƯỜNG 1 — SALES_ENTRANCE (cửa kính, thảm, vỉa hè)
          ┌──────────────────▯▯──────────────────────┐
          │                                           │
 TƯỜNG 4  │                                           │  TƯỜNG 2
 SALES_   │                                           │  SALES_SOFA
 LAKE     │                                           │  sofa chờ kem,
 cửa kính │                                           │  bàn trà
 ra hồ    │         [bàn tiếp khách trắng]            │
          │         [hộp kính mô hình khu nhà]        │
          └───────────────────────────────────────────┘
                    TƯỜNG 3 — SALES_DESK
```

- Nhìn cửa vào (tường 1): phải = tường 2 (sofa) ✓; sau lưng = tường 3 (bàn tiếp khách, nhân viên "ngoài khung, sau lưng máy") ✓.
- Nhìn sofa (tường 2): trái = tường 1 (cửa) ✓, phải = tường 3 (bàn) ✓.
- Nhìn bàn (tường 3): mô hình trong hộp kính sau lưng nhân viên ✓.
- Nhìn cửa kính ra hồ (tường 4): phải = tường 1 (cửa vào) ✓ C41 21–25. Tường 4 là phía ngược của cú nhìn sofa qua vai bà (C41 0–2 ↔ 11–15) ✓.

### 6.3 Bảng ánh xạ

| Câu kịch bản | Panel |
|---|---|
| "cạnh bàn tiếp khách / sau bàn (tiếp khách) nhìn về cửa vào", "Máy nhìn về cửa vào" | `SALES_ENTRANCE` |
| "giữa phòng / sau vai bà nhìn về sofa chờ", "Máy nhìn về sofa chờ" | `SALES_SOFA` |
| "trước bàn nhìn về bàn tiếp khách", "Máy nhìn về bàn tiếp khách", chèn ký hợp đồng trên bàn | `SALES_DESK` |
| "sau vai Devin nhìn về cửa kính ra hồ", "Máy nhìn về cửa kính ra hồ" | `SALES_LAKE` |

### 6.4 Chỗ lệch

Không có. "Cửa kính ra hồ" chỉ xuất hiện ở C41; tôi đặt nó ở tường 4 (đối diện sofa), khớp mọi câu trái/phải. Số lô (Lot 7, Lot 12) trên mô hình và sơ đồ trên màn hình ghép lúc dựng, không vẽ. Trong `tuong`, mô hình viết là "tabletop miniature" vì tool `bo_nguoi()` cắt chữ "model".

### 6.5 Bảy câu đời thực

1. **Của ai:** văn phòng bán hàng của chủ đầu tư khu có cổng mới (hư cấu) gồm nhà colonial gạch lớn — nơi bán nhà cho tầng 3. Nhân viên nhà đất là nữ da đen khoảng 30 tuổi, blazer xanh dương nhạt (kịch bản), chuyên nghiệp, không biếm hoạ.
2. **Ở đâu thật:** Mitchellville, PG County — giàu, đa số người da đen, nhiều khu có cổng, sân golf, hồ, nhà colonial gạch mặt tiền, sảnh hai tầng (khớp biệt thự Lot 7: đèn chùm lớn, cầu thang cong). Văn phòng bán hàng đặt gần cổng khu.
3. **Dấu hiệu người trong cuộc:** tranh trừu tượng chàm – vàng kim của nghệ sĩ da đen trên sofa; bát kẹo bạc hà gói trên bàn trà; chậu cúc cam tháng 10 trước cửa (trang trí thu kiểu Maryland); ảnh trên không hồ và mái nhà; nhà gạch mặt tiền ngoài phố (đúng kiểu nhà giàu PG County, không phải nhà Địa Trung Hải).
4. **Đồ sinh hoạt:** điện thoại bàn, cốc bút, ngăn kéo chìa khoá, bàn nước có chai nước và đĩa bánh quy, giá brochure.
5. **Nguồn sáng thật:** nắng cuối buổi sáng qua cửa kính trước và mặt kính ra hồ, đèn âm trần trắng trung tính, một đèn cây đồng cạnh sofa (nguồn ấm duy nhất).
6. **Người nền:** trong phòng chỉ có nhân viên nhà đất (AG1), đúng kịch bản. Ngoài kính có thể có một người chạy bộ hoặc dắt chó đi xa trên vỉa hè. Bảo vệ khu ở chốt cổng ngoài hình (C41–C42): áo khoác gió xám bạc, bộ đàm.
7. **Tiếng nền:** chuông cửa khi mở, điều hoà nhẹ, gõ phím, máy cắt cỏ xa, tiếng đài phun nước ngoài hồ. Không nhạc.

**Điều sai:** tên khu, logo chủ đầu tư, bảng giá có số; chữ "showroom", "model home" trong mô tả; cây cọ ngoài trời (sai vùng Maryland); nhà kiểu California / Địa Trung Hải; vàng chói, nhung chần nút (giàu thật không phải phông bạt).

---

## 7. Soát chữ đã chạy (02/11/2026)

- Regex `TU_CHI_NGUOI` của tool (nạp từ `xuong_anh/doc_kich_ban.py`) + danh sách cấm của đề bài + các từ chỉ thân thể / đồ mặc (head, foot, waist, host, vest, coat…) trên mọi `tuong`, `the_gioi`, `anh_sang`, `khac_ban_goc`: **0 chỗ**. Đã thay: "two-person tables" → "tables for two", "host stand" → "reservation podium", "foot rail" → "brass rail along its base", "head of the table" → "top end", "waist height" → "across its middle", "model" → "tabletop miniature", "handmade" → "homemade".
- `banned_words.json` (mọi nhóm, kể cả WEAPON — đã bỏ "shotgun cottage" — và MODEL_UNSAFE "hold/holding", "bedroom"): **0 chỗ**. Không tên hãng, không tên chuỗi, không chữ showroom, không "cinematic / golden hour / moody / warm tones / vintage".
- `kiem_doi_thuc.soat()` chạy trong bộ nhớ: 7 bảng "ổn"; `BASEMENT_BANG` (loại nhà ở) có 3 nhóm dấu hiệu (Kinh Thánh + thánh giá gỗ, chăn ghép, vỏ gối lụa) và ≥ 3 đồ sinh hoạt.
- Độ dài: mỗi tường 38–48 từ. Lưu ý cho bước dựng prompt: `prompt_mac_dinh` lặp mỗi tường 3 lần (tường xa + trái + phải), nên prompt bảng ≈ 5.100–5.500 ký tự trước `[RENDER]`. `kinh-nghiem-news.md` ghi rằng prompt bảng 4.400 ký tự bị cổng cắt kết nối khoảng 10 lần, còn khoảng 1.400 ký tự thì qua ngay. Nếu cổng rớt, rút phần trái/phải xuống chỉ còn cụm đầu của mỗi tường.
