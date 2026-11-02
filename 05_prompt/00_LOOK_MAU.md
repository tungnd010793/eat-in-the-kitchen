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
| <NOI_BANG> | ngày | <…> | <…> |

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
