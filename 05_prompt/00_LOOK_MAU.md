# LOOK MÀU — EAT IN THE KITCHEN

Mã look: `GD+TC-35_54-US_DEN-16x9` · tạo bằng skill `look-mau-theo-the-loai` (`scripts/tao_look.py`) · số máy đọc: `look.json` cạnh file này.
Skill viết kịch bản đọc file này ở Bước 5 (bảng màu trang phục), Bước 6 (ánh sáng bối cảnh), Bước 10 (prompt ảnh), Bước 11 (câu màu trong `[保持不变]`) và lúc dựng (LUT). **Không dùng lại câu màu cố định cũ** (`muted … low saturation`, `restrained, slightly desaturated`, `色彩自然柔和`).

## 0. Quyết định look (Claude điền lý do — người dùng có thể đổi)

| Trục | Chọn | Lý do (từ kịch bản / hồ sơ) |
|---|---|---|
| Thể loại | Drama gia đình / hôn nhân (+ Tình cảm / tổng tài / trả thù 30%) | Mẹ chồng – con dâu, bữa tiệc sinh nhật, căn nhà gia đình; thêm 30% chất "lật mặt sang trọng" vì có phòng họp 40 triệu, nhà hàng sang, biệt thự Lot 7 |
| Độ tuổi khán giả | 35–54 | Khán giả drama gia đình Mỹ gốc Phi trên YouTube ngang; nhân vật chính 66 tuổi |
| Quốc gia / thị trường | Mỹ — khán giả người Mỹ gốc Phi | Skill `viet-kich-ban-drama-phuong-tay`, dàn diễn viên người Mỹ gốc Phi, Prince George's County |
| Nền tảng | YouTube ngang 16:9 | Ý tưởng gốc: khung 16:9 |

Look màu: người dùng uỷ quyền (30/10/2026), Claude chốt ngày 02/11/2026.

**Look một câu:** Nhà có hơi người: ánh cửa sổ và đèn bàn ấm, trắng vẫn trắng, mặt luôn sáng rõ, da nâu ấm có điểm sáng, không bao giờ xám. Phe ác mang màu đỏ rượu và đen bóng; bà Marguerite đi từ xanh sage bạc màu tới emerald.

## 1. Thông số

| Trục | Thể loại | + Tuổi | + Quốc gia | + Nền tảng | = Look | Đọc là |
|---|---|---|---|---|---|---|
| Độ sáng | +0.15 | +0.5 | +0.5 | +0.0 | **+1.15** | hơi cao |
| Tương phản | +0.80 | +0.5 | +0.5 | +0.0 | **+1.80** | cao |
| Bão hoà | +0.30 | +0.0 | +1.0 | +0.0 | **+1.30** | cao |
| Độ ấm | +0.70 | +0.5 | +0.5 | +0.0 | **+1.50** | cao |

Thang −3…+3 so với baseline Rec.709 trung tính; look cũ của xưởng ≈ tương phản −2, bão hoà −2. Chân đen ≈ 2.55%. Mặt cảnh tối nên ở luma 40–50, da cảnh ngày (vùng sáng) 60–68. Tỉ lệ ngày/đêm của thể loại: ≈70/30 — đêm dành cho cãi vã, đọc tin nhắn, khóc một mình.

- **Thể loại:** Mid-key ấm tự nhiên, 'nhà có hơi người': ánh cửa sổ + đèn practical ấm, trắng vẫn trắng; da ấm mềm dễ đọc; độ rực vừa; đen mềm có chi tiết. Hai thế giới: mặt tiền gia đình ấm gọn ↔ sự thật / xung đột lạnh dần, tương phản tăng.
- **Tuổi:** Độ nhạy tương phản bắt đầu giảm 40–50 tuổi → tránh cảnh tối phẳng; mặt phải dễ đọc trên cả TV lẫn điện thoại (cũng là nhóm khán giả chính của app phim ngắn dọc).
- **Thị trường:** Look desat + đen nâng + lạnh chính là công thức da 'ashy' — rủi ro số 1. Jewel tones (vàng kim, burgundy, emerald, tím) hợp gu.
- **Da (ràng buộc cứng, thắng mọi thứ khác):** Da nâu sâu ấm, có highlight 'glow' vàng – đồng, chi tiết trong bóng; cấm xám tro (ashy), cấm cam / đỏ gạch, cấm đen bết, cấm làm sáng da. Ánh sáng hắt (bounce), da có độ ẩm phản xạ.
- **Nền tảng:** Xem cả TV (≈36% thời lượng YouTube) — gamma web 2.2; cảnh tối dễ vỡ mảng khi nén → không để vùng đen lớn bết, thêm hạt mịn ở hậu kỳ, upload 4K nếu được.

## 2. Lớp ảnh nhân vật (B05 / B10)

Ảnh nhân vật **giữ nền xám nhạt trơn + cân trắng trung tính** (dùng lại cho mọi cảnh ngày / đêm; Seedance kéo màu nền ảnh nhân vật vào video). Chỉ đổi câu ánh sáng – màu dưới đây.

**Câu ánh sáng mặt** (dán vào chỗ `<LOOK câu ánh sáng mặt>` của khuôn ảnh mặt B10 mục 3 / B05 — khuôn đã có sẵn `plain light grey backdrop,` đứng trước; ảnh đồ / bảng nhân vật giữ `soft natural daylight, true-to-life colours`):
```
soft directional daylight from a large window at one side with a gentle white bounce on the shadow side, natural warm-neutral colours, moderate natural contrast
```
**Đuôi "Colour and finish"** (thay nguyên văn đuôi cũ ở B10 mục 8, mọi ảnh):
```
Colour and finish: camera white balance at neutral daylight, so warmth comes only from the practical lamps and the warm materials in the room, never from a global grade; whites read white; natural earthy saturation, not punchy and not washed out; moderate contrast, soft but present blacks, gentle highlight roll-off; real mature skin with pores and fine lines. Anti-AI: photorealistic, looks like a real photograph taken on a real camera; camera white balance neutral so white objects render clean white, no overall yellow, amber, orange or sepia cast; true-to-life skin with visible pores and natural unevenness, not airbrushed, not plastic or waxy; natural lens sharpness, no oversharpening or edge halos; no HDR or tone-mapped look; no glow, bloom or haze on faces; highlights and shadows keep detail; colour comes from real objects and real light sources, not from a filter.
```

## 3. Bảng màu trang phục và bối cảnh (B05 / B06)

- **Chủ đạo:** kem #E9D8BC · gỗ óc chó #A8754A · xanh sage #8A9A7E · hồng trầm #C4A09A · navy bạc #3B4A5E
- **Nhấn:** đỏ rượu #7A1E2C (phe gây hại: kẻ phản bội / người thứ ba / mẹ chồng quyền lực — gán theo kịch bản) · vàng đèn #E0A458 (chỉ ở nguồn sáng)
- **Trang phục:** Chất liệu thật, màu đất và màu trầm: len kem, sơ mi xanh nhạt bạc, cardigan sage, váy hồng trầm, vest navy. Phe 'mặt tiền' gọn, màu hài hoà; phe phản diện có một màu nhấn đậm (đỏ rượu, đen bóng). Tránh neon, tránh pastel kẹo.
- **Bối cảnh:** Gỗ ấm, vải lanh, ảnh gia đình đóng khung, đèn bàn chao vải, chút bừa bộn đời thường; một đồ vật màu nhấn mỗi phòng.
- **Tránh:** neon · pastel kẹo · teal-orange · toàn xám

**Điều chỉnh theo thị trường (Mỹ — khán giả người Mỹ gốc Phi) — thắng bảng của thể loại khi trái nhau:** Thêm jewel tones vào bảng của thể loại: vàng kim, burgundy, emerald, tím hoàng gia — trang phục đi nhà thờ / tiệc là chỗ đặt màu đậm; màu đồ phải tách hẳn màu da (không nude bó sát — kinh-nghiem-news A9).

**Màu chữ ký từng nhân vật** (Claude điền khi làm Bước 5):

| Nhân vật | Màu chữ ký | Đổi màu theo cung (nếu có) |
|---|---|---|
| MARGUERITE | xanh sage bạc màu + be | bị coi thường: sage bạc + be sờn → đi làm: gi-lê xanh lá thu ngân → đứng dậy: navy → vị thế mới: emerald |
| DEVIN | xám + navy | đi làm: sơ mi navy, nhà: henley xám → sụp đổ: áo phao đen cũ → chuộc lỗi: gi-lê cam kho, áo len navy |
| RAVEN | đỏ rượu (phe ác) | tiệc: satin đen bóng → bị bắt, ra toà: xám than, mất bóng bẩy |
| CHARLENE | tím | nhà thờ / tiệc: tím hoàng gia → bệnh viện, livestream: áo bệnh nhân + tím sẫm → công ích: tạp dề xanh dương |
| INÈS | kem + lạc đà | quiet luxury suốt phim, không đổi |
| PRENTICE | xám than + navy | không đổi |
| ASHANTI | be + đen | không đổi |

## 4. Lớp bối cảnh (B06 / B06b / B10 mục 6) — nơi mang look

**Dòng phong cách chung** (thay vế màu `muted natural colours with low saturation, gentle contrast, soft natural light, shallow focus, subtle film grain` của B10 mục 2 và `[RENDER]` bảng 4 góc):
```
a warm, naturalistic prestige family drama look: mid-key exposure with faces well exposed and gentle shadow falloff into the corners, soft directional daylight from windows plus warm practical lamps visible in frame making small warm pools of light, daylight areas and white surfaces staying clean neutral white, natural earthy colours, moderate contrast with soft but present blacks, faces clearly lit and easy to read even in the darker scenes, rich warm brown skin with luminous highlights and detail in the shadows, never grey or ashy
```
**Ánh sáng mẫu theo loại nơi** (chọn / sửa cho từng nơi của phim, đưa vào `[WORLD]` / câu tả ánh sáng của bảng 4 góc):

| Loại nơi | Câu ánh sáng (EN) |
|---|---|
| `nha_ngay` | soft daylight through sheer curtains as the key, one warm table lamp on in the corner, white walls and white cups render clean white |
| `bep` | bright window daylight across the counter, warm pendant lights above the island, polished surfaces with soft reflections |
| `phong_ngu_toi` | dim room lit by a warm bedside lamp and the cool spill of a window, faces softly lit, the room falling into soft shadow |
| `phong_khach_toi` | two warm floor lamps and a table lamp make pools of light, the far corners in soft shadow that still holds detail |
| `van_phong_luat_su` | even cool-neutral daylight through tall windows, a single warm desk lamp, wood panelling |
| `benh_vien` | flat cool-white overhead light, pale green-grey walls, one warm detail (flowers, a blanket) |

**Bảng nơi của phim này** (Claude điền ở Bước 6; nơi có cả cảnh ngày và đêm → **hai bảng 4 góc**, cùng góc máy, cùng bày trí):

| Nơi | Trạng thái | Câu ánh sáng | Nhịp dùng |
|---|---|---|---|
| BOWIE_HOUSE_DAY_BANG | ngày | Soft neutral daylight through the sheer curtains, the sink window and the frosted door panel, one fabric-shade table lamp on at the sofa end, pendants and chandelier off, whites stay clean white, mid-key, no yellow or orange cast. | C1, C2, C3 |
| BOWIE_HOUSE_MESSY_BANG (vẽ từ BOWIE_HOUSE_DAY_BANG) | ngày, bừa bộn | Soft neutral midday daylight through the sheer curtains, the sink window and the frosted door panel, one fabric-shade table lamp on at the sofa end, pendants and chandelier off, whites stay clean white, mid-key, no yellow or orange cast. | C18, C19, C20, C48 |
| BOWIE_HOUSE_NIGHT_BANG (vẽ từ BOWIE_HOUSE_MESSY_BANG) | đêm | Night: the windows read blue-black behind the sheer curtains, light comes only from visible practicals, the glass-bead chandelier over the dining table, two brass pendants over the island, two cream-shaded buffet lamps and the fabric-shade table lamp by the sectional, making small warm pools on a neutral white balance, mid-key, corners in soft shadow that keeps detail, whites stay white, no global amber cast. | C21, C33, C44 |
| BOWIE_PARTY_NIGHT_BANG (vẽ từ BOWIE_HOUSE_DAY_BANG) | đêm, tiệc | Night party light: every practical on, the glass-bead chandelier over the long table, the brass island pendants, both buffet lamps, the sofa table lamp and a few short candles on the table, a bright mid-key room with warm pools only around the lamps on a neutral white balance, the white tablecloth and plates reading clean white, windows blue-black behind the sheers, no global amber cast. | C4, C5, C6, C7, C8, C9, C10 |
| BOWIE_FRONT_DAY_BANG | ngày | Clear early-autumn daylight from a high sun on the south-facing front, soft shadow under the porch roof, neutral white balance so the white door, trim and columns stay clean white, natural green lawn, mid-key, no yellow or orange cast. | C3, C18, C20, C48 |
| BOWIE_FRONT_NIGHT_BANG (vẽ từ BOWIE_FRONT_DAY_BANG) | đêm | Night: the warm porch lantern lights the porch and steps, lamplight glows through the frosted door panel and the sheer-curtained dining window, one cool-neutral street lamp pools light on the street, deep navy sky, the lawn and side yard falling into soft dark that still holds detail, mid-key around the porch, no global orange cast. | C10, C11 |
| BOWIE_FRONT_SNOW_BANG (vẽ từ BOWIE_FRONT_DAY_BANG) | tuyết tháng Giêng | Flat overcast January daylight from a uniform grey sky, light snowflakes in the air, neutral white balance so the snow reads clean white and neither blue nor yellow, soft low-contrast shadows, the porch lantern off and the windows unlit, mid-key. | C50 |
| GROCERY_BANG | ngày | Even neutral-white LED ceiling panels over the aisles and checkout counters, bright daylight through the storefront glass at the entrance, the cooler and deli cases lit from inside, two warm heat lamps over the hot-food case as the only warm light, white floor tiles and shelves staying clean white. | C12, C13, C14, C15, C16, C17, C26 |
| KEYSTONE_CONF_BANG | ngày | Soft directional daylight through the tall windows as the key, recessed neutral-white ceiling lights on, gentle reflections on the glass partition, white walls and white cups staying clean white, the light-oak table and walnut credenza giving the only warmth. | C22, C23, C24, C25, C26, C30, C31, C45, C46, C47 |
| KEYSTONE_CONF_NIGHT_BANG (vẽ từ KEYSTONE_CONF_BANG) | đêm | Only one row of recessed neutral-white ceiling lights is on, directly above the top end of the table, making a pool of light on the light-oak top while the rest of the room falls into soft shadow that still shows detail; the windows are black with a few distant parking-lot lamps and faint reflections of the room; the office floor beyond the glass is dark except a few low security lights; no warm cast. | C44 |
| KEYSTONE_FLOOR_BANG | ngày | Daylight through the floor-to-ceiling windows falling across the desks, neutral-white recessed ceiling lights, a brass desk lamp glowing on the reception desk as the only warm light, white desks and ceiling staying clean white. | C27, C28, C29, C47 |
| BASEMENT_BANG | chạng vạng | A single bare bulb in the ceiling socket as the only lamp, making a small warm pool of light over the bed and the table, dim blue dusk through the high window and the open stairwell, the cinderblock corners in soft shadow that still holds detail, neutral white balance. | C32 |
| MAISON_BANG | đêm | Low glass candle lamps on every table and brass sconces make small warm pools of light, three pendant lamps and backlit bottle shelves light the bar, the river glass stays dark with cool reflected shore lights, white tablecloths stay clean white, mid-key with soft shadows that keep detail. | C34, C35, C36, C37, C38 |
| SALES_OFFICE_BANG | ngày | Bright late-morning daylight through the glass front door and the lake-side glass as the key, neutral-white recessed ceiling lights, one brass floor lamp glowing beside the sofa as the only warm light, white walls and the white desk staying clean white. | C39, C40, C41, C43 |
| LOT7_FOYER_BANG | ngày | Soft neutral daylight from the arched window above the doors and through the textured door glass, gentler daylight through the study's sheer curtains, the chandelier off, the linen-shaded desk lamp in the study glowing as the one warm accent, mid-key, cream walls and white trim staying clean white with no orange or amber cast. | C42, C43, C49, C51, C66, C68 |
| LOT7_DINING_BANG | cuối chiều nắng thấp | Low late-afternoon sun slanting through the west windows and sheer curtains in long bright bands across the walnut table and pale floor, the rest of the room in soft neutral daylight, the two brass sconces by the arch switched on as small warm pools, white porcelain staying clean white, no global orange or amber cast. | C68, C69, C70 |
| LOT7_EXT_BANG | tuyết tháng Giêng | Clear cold late-morning winter sun, low from the street side under a pale blue sky, lighting the brick facade and casting long crisp shadows of the fence and bare branches, the old snow along the edges reflecting clean white, neutral daylight white balance, coach lanterns off. | C57, C58, C59, C60, C61, C62 |
| LOT7_EXT_THU_BANG (vẽ từ LOT7_EXT_BANG) | tháng Mười | Bright clear noon sun of mid-October from high over the street side, lighting the brick facade and the yellow oak canopy, short crisp shadows and dappled leaf shade on the driveway, neutral daylight white balance so the yellow leaves read true and whites stay white, coach lanterns off. | C42, C43, C49 |
| LOT7_EXT_CHIEU_BANG (vẽ từ LOT7_EXT_BANG) | cuối chiều nắng thấp | Low late-afternoon sun from the west raking across the front lawn and brick facade in long bright bands, long shadows of the oaks and fence stretching across the driveway, the shaded areas in soft neutral daylight, neutral white balance with no global orange or amber cast, coach lanterns off. | C68 |
| CHARLENE_APT_BANG | ngày | Soft overcast January daylight through the half-raised white blinds as the key, the pleated yellow-shaded lamp by the sofa switched on as the one small warm pool, ceiling light off, mid-key, walls and blinds staying clean neutral white with no orange cast. | C50, C51 |
| CHARLENE_APT_DEM_BANG (vẽ từ CHARLENE_APT_BANG) | đêm | Night: the pleated yellow-shaded table lamp beside the sofa is the only light, a warm pool over the sofa, the end table and the ajar bedroom door, the kitchenette and front door falling into soft dim shadow that still holds detail, the window dark, no other lamps, walls reading neutral off-white where the lamp reaches. | C56 |
| HOSP_BANG | ngày | Flat cool-white overhead panel light as the key with soft overcast winter daylight from the window, even and nearly shadowless on the pale green-grey walls, the one warm detail the small vase of yellow carnations on the sill, white sheets rendering clean white, mid-key, no orange cast. | C52, C53, C54, C55 |
| COURT_HALL_BANG | ngày | Bright white daylight from the tall south windows washing across the marble floor and oak paneling, flush ceiling fixtures adding even neutral fill, no lamps, mid-key, neutral daylight white balance with whites clean and no amber cast. | C63 |
| CHURCH_HALL_BANG | ngày | Flat fluorescent light from the drop-ceiling tube panels as the key, a little soft daylight from the high frosted basement windows, steam rising from the stock pot, even and mid-key, neutral white balance so tablecloths and bowls stay clean white, no amber cast. | C64 |
| WAREHOUSE_BANG | ngày | Even cool-white light from the LED high-bay fixtures, neutral daylight spilling in through the half-open dock door, no warm lamps, mid-key, plain cartons and painted lines staying clean and neutral, no amber cast. | C65 |
| DEVIN_STUDIO_BANG | đêm | Night: the yellow fabric-shaded desk lamp and the small light under the range hood are the only lights, small warm pools on the table and the cooktop, steam rising from the pot, the rest of the room in soft shadow that still holds detail, the window dark behind closed blinds, the walls reading neutral off-white. | C67 |

## 5. Lớp video (B11 khối 9 `[保持不变]`)

Thay đúng vế `色彩自然柔和` của câu `…保留自然肤质；色彩自然柔和，不过度锐化。整体ARRI Alexa 35电影感…` bằng câu dưới (63 chữ). Mọi chữ khác của khuôn giữ nguyên.
```
中性白平衡，白色干净不偏黄，暖意只来自画面里看得见的灯和窗边光，色彩自然温润，中等对比，暗部有细节，面部明亮清楚，色温、光影、亮度参考场景图
```
Luật: không gắn từ màu vào 脸 / 面部 / 肤色 / 表情; không chữ giờ (B11 mục 5 — 夜景 cũng cấm); ánh sáng khác ảnh thì tả bằng nguồn sáng nhìn thấy. Bỏ `变形宽银幕构图` / `细腻35mm颗粒` **chỉ** sau khi render đối chứng (kinh-nghiem-look.md C-L7, C-L8).

## 6. Nhịp cảm xúc → LUT (lúc dựng)

Prompt video không đổi màu theo nhịp (model dễ nhấp nháy màu); nhịp đổi bằng **LUT riêng** + (nếu cần) **bảng bối cảnh biến thể** cùng góc máy.

| Nhịp | Dùng khi | Câu bối cảnh biến thể (EN) | Trục sau nhịp (S/TP/BH/Ấm) |
|---|---|---|---|
| `vui` | hạnh phúc, ký ức đẹp | warm late-sun patch through the window, slightly brighter room, gentle bloom on the lamps | +1.6 / +1.5 / +1.8 / +1.5 |
| `hoi_tuong` | hồi tưởng — đổi bằng LUT riêng, không đổi prompt video | same room, softer light, warmer lamps | +1.4 / +1.0 / +0.3 / +1.5 |
| `xung_dot` | cãi vã, phát hiện phản bội | harder side light from a single practical, cooler daylight from the window, deeper shadows | +0.8 / +2.5 / +0.8 / +0.8 |
| `day_vuc` | tuyệt vọng, đáy | flat overcast grey daylight, lamps off, quieter drained colours that are still not grey, an emptier room | +0.8 / +1.5 / +0.1 / +0.7 |
| `cao_trao` | vạch trần, đối mặt | strong motivated practical, deep shadows, faces half-lit but readable | +1.1 / +2.8 / +1.3 / +1.5 |
| `ket` | hoá giải, hàn gắn | soft clean morning daylight, fresh whites, warm but clean | +1.6 / +1.8 / +1.6 / +1.5 |

**Bản đồ cụm → nhịp** (Claude điền ở Bước 7 khi có bảng cụm; cụm không ghi = LUT gốc):

| Cụm | Nhịp |
|---|---|
| <001–004> | <vui> |

## 7. Hậu kỳ

- **Ảnh tham chiếu (bot_ai):** bão hoà ×0.973, da ×0.977, bớt ám cảnh 0.45, làm mềm 0.42 (look cũ: ×0.87 / ×0.93 / 0.6 / 0.42 cho mọi phim). `tao_anh.py` tự đọc `look.json` của dự án.
- **LUT gốc:** gamma 0.954, tương phản k 1.108, chân đen 0.0255, bão hoà ×1.091 (da ×1.0325), bớt xanh lá 0.08.
- Lệnh: `python -X utf8 <skill>/scripts/tao_lut.py --look look.json --tat-ca --ra _dung/lut_look` → `look_goc.cube` + một file mỗi nhịp; `--xem <ảnh>` ra ảnh trước | sau. Bộ `mau.py` của phim (cân cụm theo cảnh) gọi `ap_look()` của `tao_lut.py` thay cho hàm `look()` cố định.
- Hạt phim: thêm ở bước dựng cho đều mọi cụm (mức 0.6), không thêm trong prompt ảnh.

## 8. Kiểm màu (QC)

`python -X utf8 <skill>/scripts/do_mau.py anh/*_BANG.png --so look.json` (bảng bối cảnh) và trên khung video. **Không đo bảng nhân vật nền xám.**

| Số đo | Mục tiêu |
|---|---|
| `luma_p50` | 38.8 – 52.8 |
| `chroma_tb` | 9.4 – 16.4 |
| `tuong_phan` | 48.2 – 66.2 |
| `luma_p05` | 2.5 – 13 |
| `am_b_trung_tinh` | -3.0 – 5.0 |

## 9. Tránh

- **Sai gu:** grade kiểu thriller Fincher/Ozark: mặt chìm trong bóng · neon / bão hoà cao kiểu teen · da bóng nhựa, beauty filter · xám đơn sắc suốt phim · teal-orange blockbuster
- **Chữ tránh trong prompt ảnh:** cinematic lighting · dramatic color grading · golden hour · vintage film · moody · neon
- **Phim mốc của thị trường (gu khán giả — ưu tiên):** Queen Sugar · Insecure (da sẫm) · Tyler Perry's Sistas / The Oval (chưa chắc) · Harlem
- **Phim mốc của thể loại (cách xử lý màu theo cung):** This Is Us · Big Little Lies · Little Fires Everywhere · Yellowstone · Ginny & Georgia
