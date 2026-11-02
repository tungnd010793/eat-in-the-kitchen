# 05 — PROMPT TẠO HÌNH / VIDEO

> Ghi **mọi lần thử**, kể cả lần hỏng. Chuỗi *thử → chọn → sửa* chính là bằng chứng đóng góp sáng tạo: Nghị định 134/2026/NĐ-CP coi việc **thiết lập prompt, đánh giá, lựa chọn, chỉnh sửa kết quả** là đóng góp của con người.
> File kết quả đặt tên trùng **mã** của lần thử (vd `C01-03.mp4`) và lưu trong `09_media/ai-tao-ra/`.

**Tác phẩm:** EAT IN THE KITCHEN

## Ảnh nhân vật — lượt 1 (tác giả đã chốt ngoại hình 02/11/2026)

### NV-01 · 7 nhân vật chính, bộ đồ cảnh đầu tiên
- **Ngày:** 02/11/2026, 17:53–17:59
- **Công cụ / model:** Xưởng phim · Bigup Studio (`F:\Tungnd\bigup_xuong_phim_1.0.23`), model ảnh mặc định của cổng · **Gói:** trả phí
- **Thiết lập:** mỗi nhân vật 3 ảnh — ảnh mặt 1024x1536 → ảnh bộ đồ 1024x1536 (lấy ảnh mặt làm gốc) → bảng nhân vật 2 ô 16:9 (cận mặt bên trái, toàn thân bên phải). Look màu `GD+TC-35_54-US_DEN-16x9` (`05_prompt/00_LOOK_MAU.md`), hậu kỳ "bớt AI" theo look.
- **Tư liệu đầu vào:** không dùng ảnh ngoài; chỉ chữ từ kịch bản `04_kich-ban-chinh-thuc.md` (tóc, kính, trang phục cảnh đầu tiên của từng nhân vật).
- **Prompt:** hồ sơ nhân vật và câu phong cách ở `05_prompt/anh/du_an.json`; prompt ảnh mặt viết riêng (có cổ áo, trang sức, makeup của bộ đầu tiên) ở `05_prompt/anh/_prompt_rieng.json`.
- **Kết quả:** `09_media/ai-tao-ra/nhan-vat/` — 21 ảnh (7 `CHAR_*_FACE`, 7 `OUTFIT_*`, 7 `SHEET_*`) + 2 ảnh xem nhanh `_XEM_NHANH_*.jpg`. 22 lần gọi cổng (bảng của Prentice lỗi tải về một lần, tạo lại).
- **Đánh giá & quyết định:** Claude soát: cả 7 đạt 7,5–9/10 (đúng mặt, tóc, dấu nhận diện, bộ đồ). Ghi chú: cardigan của Marguerite còn hơi mới so với vai osin; bảng Prentice có vệt nối mờ giữa hai ô. **Tác giả chốt cả 7 nhân vật như bản này (02/11/2026), giữ nguyên hai điểm ghi chú.** Ảnh mặt và bảng đầu của mỗi người là gốc cho mọi bộ đồ sau.

## Ảnh nhân vật — lượt 2 (các bộ đồ còn lại + nhân vật phụ có thoại, tác giả đã chốt 02/11/2026)

### NV-02 · 29 bộ đồ còn lại của 7 nhân vật chính, 14 nhân vật phụ
- **Ngày:** 02/11/2026, 20:12–20:50
- **Công cụ / model:** như NV-01 · **Gói:** trả phí
- **Thiết lập:**
  - **Bộ đồ mới:** ảnh đồ toàn thân lấy ảnh mặt đã chốt làm gốc. Bảng 2 ô được dựng từ ba ảnh: ảnh mặt, bảng đầu đã chốt (giữ mặt) và ảnh đồ.
  - **Bộ chỉ thêm một lớp** (tạp dề, áo khoác mùa đông, mũ): tạo thẳng từ bảng gốc, chỉ đổi đúng món đó. CH5C và CH5W gửi thêm bảng CH2 / CH4 để chiếc cardigan, áo dạ, khăn và mũ len giống hệt.
  - **Đổi tóc / râu theo thời gian:** prompt viết riêng cho V4 (râu lún phún, tóc Caesar dài ra), R4 (tóc hơi xù chân), R6 và R7 (tóc dài quá cằm, chân tóc đen, bỏ trang điểm, bỏ khuyên tai).
- **Tư liệu đầu vào:** ảnh mặt và bảng đầu đã chốt ở NV-01; chữ trong kịch bản `04_kich-ban-chinh-thuc.md`. Claude đọc trọn 70 cụm để lập bảng tủ đồ: bộ nào, cụm nào, tả thế nào.
- **Chỗ kịch bản bỏ trống, Claude tự chọn theo vai và bảng màu của look:**
  - **Quần và giày:** M1 quần tây navy + giày thể thao đen; M3 quần tây navy + giày gót thấp đen; V2 quần len xám + giày lười nâu.
  - **Áo phao mùa tuyết:** V4 là áo phao đen mờ, ngắn, cũ; R5 là áo phao đen bóng dài tới gối. Hai chiếc phải khác nhau rõ.
  - **Vest xám than:** V3 dáng ôm, xám nhạt hơn, cà vạt satin bóng, để không lẫn với P1 của Prentice.
  - **R3:** chốt là đầm ôm vừa cổ vuông, vì kịch bản ghi vừa "suông" vừa "ôm dáng".
  - **Phóng viên livestream:** kịch bản không ghi giới tính; Claude chọn nữ.
- **Mã mới đặt cho bộ kịch bản tả mà chưa gắn mã:** M0A, V2, V4H, V7, V8, R1, R4, R6, R7, CH1, CH5C, CH6, CH7.
- **Prompt:** `05_prompt/anh/du_an.json` (mô tả bộ đồ, hồ sơ nhân vật phụ), `05_prompt/anh/_prompt_rieng.json` (ảnh mặt nhân vật phụ, đổi tóc/râu), `05_prompt/anh/_goc_rieng.json` (ảnh gốc thêm cho CH5C, CH5W).
- **Kết quả:** `09_media/ai-tao-ra/nhan-vat/` — 98 ảnh mới (14 `CHAR_*_FACE`, 38 `OUTFIT_*`, 46 `SHEET_*`) + 6 ảnh xem nhanh `_XEM_NHANH_3…8`. 103 lần gọi cổng: ảnh mặt viên cảnh sát lỗi tải về, nên ảnh đó và hai ảnh dựng từ nó được tạo lại ở một lượt riêng.
- **Đánh giá của Claude:**
  - Cả 46 bảng giữ đúng mặt đã chốt và đúng bộ đồ kịch bản tả. Ba bộ emerald của Marguerite, ba sắc tím của Charlene, bốn bộ đỏ rượu của Raven, hai áo phao đen, hai bộ vest xám than đều phân biệt được.
  - **Ghi chú:**
    - R6, R7: đã bỏ trang điểm, khuyên tai, tóc hết bóng, nhưng tóc chưa dài thêm và chân tóc đen còn mờ (7/10). Ở R7 lưới tóc che phần lớn tóc; prompt video cần tả thêm chân tóc đen.
    - CH1, CH4: ảnh cận mặt cũng đội mũ, giữ vì hai cảnh đó bà đội mũ suốt.
    - Áo khoác "đỏ mận" của Sister Pearl ngả gần đỏ rượu.
    - CH5, CH6 vẫn còn son tím.
  - Chưa ảnh: Sister Pearl lúc dự tiệc (C4, chỉ thấy ở toàn cảnh), bảo vệ nhà hàng (không thoại), khách và người nền.
- **Quyết định:** **Tác giả chốt cả 98 ảnh lượt 2 như bản này (02/11/2026), giữ nguyên các điểm ghi chú.** Khi viết prompt video, cụm C63–C64 tả thêm chân tóc đen của Raven bằng chữ.

## Ảnh bối cảnh — bảng 4 góc (tác giả đã chốt 02/11/2026)

### BC-01 · 26 bảng 4 góc cho 16 nơi quay
- **Ngày:** 02/11/2026, 21:30–21:53
- **Công cụ / model:** như NV-01 · **Gói:** trả phí
- **Thiết lập:**
  - Mỗi bảng là một ảnh 16:9 chia lưới 2×2. Bốn ô là bốn hướng nhìn của cùng một nơi, vẽ trong một lượt để chung tường, sàn, đồ đạc và ánh sáng. Tool tự cắt thành 4 panel làm ảnh tham chiếu riêng.
  - Bốn tường khai theo chiều kim đồng hồ: ô k nhìn thẳng tường k, tường bên phải là tường k+1, bên trái là tường k−1. Mỗi ô ghi đủ tường xa; hai tường hai bên chỉ ghi mốc chính, để prompt không quá dài.
  - **Bảng biến thể** (đêm, bừa bộn, tiệc, mùa tuyết, tháng Mười, cuối chiều) vẽ lại từ ảnh bảng gốc, giữ nguyên lưới và bày trí, chỉ đổi đúng phần ghi trong prompt. Có 9 bảng loại này.
  - Look `GD+TC-35_54-US_DEN-16x9`, dòng phong cách bối cảnh ở mục 4 của `05_prompt/00_LOOK_MAU.md`.
- **Tư liệu đầu vào:** chữ trong kịch bản. Claude đọc từng shot của 70 cụm, ghi mọi hướng máy và vị trí trái/phải, rồi dựng mặt bằng 4 tường khớp với tất cả. Bằng chứng từng câu, sơ đồ, bảng "câu kịch bản → panel" và 7 câu đời thực của mỗi nơi nằm ở `05_prompt/ghi-chu-dung/boi-canh-*.md`.
- **Prompt:** khai báo bảng ở `05_prompt/anh/du_an.json` (khoá `bang_4_goc`), prompt đầy đủ từng bảng ở `05_prompt/anh/_prompt_rieng.json`, ô cắt ở `05_prompt/anh/_bang_4_goc.json`. Bảng ánh sáng theo nơi đã điền vào mục 4 của `05_prompt/00_LOOK_MAU.md`.
- **Soát trước khi tạo:** `kiem_doi_thuc.py` báo 4 cảnh báo ở nhà Lot 7 (thiếu dấu hiệu đời thực). Claude thêm khăn móc len và đĩa kẹo bạc hà ở tiền sảnh, chậu gang đen trồng thường xuân ở bậc thềm; chạy lại còn 0 cảnh báo.
- **Kết quả:** `09_media/ai-tao-ra/boi-canh/` — 26 ảnh bảng (`*_BANG.png`) + 104 panel + 7 ảnh xem nhanh `_XEM_NHANH_1…7`. 35 lần gọi cổng.
  - Bảng nội thất nhà Bowie ban ngày lỗi tải về một lần, tạo lại cùng 3 bảng vẽ từ nó.
  - Ba bảng tạo lại vì lệch màu (xem dưới).
  - Maison Bayou thử tạo lại 2 lần không được.
- **Đo màu** (`do_mau.py --so look.json`, xét từng file):
  - Phần lớn bảng chỉ lệch chân đen bị nâng; để LUT xử lý khi dựng.
  - Bảng đêm, phòng hầm và mặt tiền cuối chiều tối hơn mục tiêu, đúng chủ ý cảnh.
  - Ba bảng lệch sáng/màu, đã sửa câu ánh sáng và tạo lại:
    - Văn phòng bán nhà: sáng 63.8 → 57.5.
    - Hành lang toà án: độ rực 19.9 → 17.6, hết ngả vàng.
    - Phòng thuê của Devin: hết ám vàng.
- **Đánh giá của Claude:**
  - Cả 26 bảng đúng mặt bằng đã dựng. Các bảng cùng một nơi khớp nhau: nhà Bowie ngày / bừa bộn / tối / tiệc; mặt tiền ngày / đêm / tuyết; phòng họp ngày / đêm; Lot 7 tuyết / tháng Mười / cuối chiều; căn hộ Charlene ngày / đêm.
  - Không chữ đọc được, không người.
  - **Ghi chú:**
    - Maison Bayou nhỏ hơn các bảng khác (panel ~630x355) và có viền xám rộng; nhiều khả năng do cổng tự chuyển sang model dự phòng. Hai lần tạo lại, model mặc định của cổng đều không tạo được, nên giữ bản này.
    - Văn phòng bán nhà vẫn hơi sáng.
- **Chỗ kịch bản lệch giờ / trái phải** (Claude ghi lại, chưa sửa kịch bản):
  - C4–C11 tiệc lúc 19:00 ngày 26/09: trời mới chạng vạng, nhưng kịch bản tả cửa sổ tối. Bảng vẽ đêm hẳn.
  - C33 lúc 18:00 ngày 09/10: trời còn sáng. Bảng dùng bảng tối.
  - C53 giây 28–30: máy đặt cạnh cửa sổ nhìn về cửa thì giường phải ở mép phải khung, kịch bản ghi mép trái.
  - C56: sofa giường "đã kéo ra", trong khi bảng đêm giữ sofa gấp. Prompt video sẽ tả sofa đã kéo ra.
- **Chưa có ảnh:** phòng giặt nơi bà Marguerite ngủ (C10, 4 giây đầu). Nên làm thành ảnh đạo cụ / ảnh chèn riêng.
- **Quyết định:** **Tác giả chốt cả 26 bảng (104 panel) như bản này (02/11/2026), giữ nguyên các điểm ghi chú.** Khi viết prompt video, những chỗ kịch bản lệch giờ / trái phải ở trên sẽ được xử lý bằng chữ trong prompt.

## Ảnh còn thiếu — đạo cụ, ảnh chèn phòng giặt, hai nhân vật phụ (chờ tác giả duyệt)

### DC-01 · 17 đạo cụ, phòng giặt (C10), Sister Pearl dự tiệc, bảo vệ nhà hàng
- **Ngày:** 02/11/2026, 22:52–23:00
- **Công cụ / model:** như NV-01 · **Gói:** trả phí
- **Thiết lập:**
  - **Đạo cụ:** ảnh 1536x1024 trên nền xám nhạt trơn, ánh sáng studio một bên, không tay, không người, không chữ, không logo.
  - **Khung ảnh kính mới (C66):** vẽ lại từ chính ảnh khung kính nứt, chỉ thay kính.
  - **Thẻ bệnh viện cũ:** lấy ảnh mặt Marguerite đã chốt làm gốc cho ảnh nhỏ trên thẻ.
  - **Phòng giặt:** ảnh chèn 16:9, vẽ từ panel `NIGHT_KITCHEN` (cùng cánh cửa gỗ hẹp, cùng đêm tiệc) và ảnh vali. Chỉ có một hướng nhìn qua cửa, nên không làm bảng 4 góc.
  - **Hai nhân vật phụ:** Sister Pearl dự tiệc (SP1) dựng từ bảng SP2 đã chốt, giữ đúng mặt. Bảo vệ nhà hàng (BV1) dựng mặt → đồ → bảng, như NV-02.
- **Tư liệu đầu vào:** chữ trong kịch bản (C1–C3 túi đỏ rượu, C10 phòng giặt và vali, C11 / C32 / C66 khung ảnh Louisiana, C12–C51 điện thoại nắp gập, C21–C30 xấp đề án, C36–C43 phong bì kraft và chìa khoá, C44 đồng hồ vàng, C44–C49 túi đen mới, C47–C48 thùng đồ, C51–C53 thẻ bệnh viện, C57–C62 bộ livestream, C67 tờ công thức, C4–C9 / C70 nồi gang và bát sứ viền xanh, C70 tám phong bì).
- **Prompt:** `05_prompt/anh/du_an.json` (khoá `dao_cu`, `boi_canh.LAUNDRY_NIGHT`, nhân vật `PEARL.SP1`, `BOUNCER`), `05_prompt/anh/_prompt_rieng.json`, `05_prompt/anh/_goc_rieng.json`.
- **Kết quả:**
  - `09_media/ai-tao-ra/dao-cu/`: 17 `PROP_*.png` + 2 ảnh xem nhanh.
  - `09_media/ai-tao-ra/boi-canh/LOC_LAUNDRY_NIGHT.png` + `_XEM_NHANH_8_phong-giat.jpg`.
  - `09_media/ai-tao-ra/nhan-vat/`: `CHAR_BOUNCER_FACE`, `OUTFIT_SP1`, `OUTFIT_BV1`, `SHEET_PEARL_SP1`, `SHEET_BOUNCER_BV1` + `_XEM_NHANH_9`.
  - 26 lần gọi cổng, không lỗi.
- **Đánh giá & sửa:**
  - **Khung ảnh Louisiana, lần đầu:** ảnh trong khung ra một dinh thự kiểu đồn điền cột trắng. Hình ảnh này sai kịch bản ("căn nhà gỗ sơn vàng nhạt có hiên trước") và gợi liên tưởng nặng nề với một gia đình Creole da đen. Claude sửa prompt thành nhà gỗ một tầng của gia đình lao động: vàng bơ, hiên mái tôn, cột mảnh, xích đu, cây sồi rủ rêu; ghi rõ "not a plantation house". Tạo lại cả hai bản kính nứt và kính mới.
  - **Thẻ bệnh viện, lần đầu:** ảnh thẻ ra bà gần bằng tuổi hiện tại. Đã sửa thành khoảng 45 tuổi, tóc đen, và tạo lại.
  - Các ảnh khác đạt ngay lần đầu.
  - **Ghi chú:**
    - Ảnh nhỏ trong khung trên bảng `LOT7_WORK` và `BASEMENT_TABLE` vẫn là nhà kiểu cũ. Cảnh cận khung ảnh sẽ gửi ảnh đạo cụ mới.
    - Bảo vệ nhà hàng (đầu trọc, râu dê bạc, đúng kịch bản) hơi giống Prentice; hai người không xuất hiện cùng nơi.
- **Quyết định:** chờ tác giả duyệt.

## Cảnh 1 — [tên cảnh]

### C01-01
- **Ngày:**
- **Công cụ / model:** [vd: Seedance 2.5] · **Gói:** [trả phí / miễn phí]
- **Thiết lập:** [tỷ lệ khung hình, thời lượng, seed, độ mạnh ảnh tham chiếu…]
- **Tư liệu đầu vào:** [file trong `09_media/tham-khao/`, do bạn tự làm hoặc có quyền dùng]
- **Prompt:**

```text

```

- **Kết quả:** `09_media/ai-tao-ra/C01-01.mp4`
- **Đánh giá & quyết định:** [Giữ / Bỏ / Sửa. Vì sao? Lần sau đổi gì?]

### C01-02
- **Ngày:**
- **Công cụ / model:** · **Gói:**
- **Thiết lập:**
- **Tư liệu đầu vào:**
- **Prompt:**

```text

```

- **Kết quả:** `09_media/ai-tao-ra/C01-02.mp4`
- **Đánh giá & quyết định:**
