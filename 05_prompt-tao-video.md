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
