# Quy chuẩn viết tay bài tiếng Trung — EAT IN THE KITCHEN (03/11/2026)

70 cụm × 30 giây (23 tập), bài tiếng Trung viết TAY, ghi thẳng mã ảnh `TÊN（@图片N）`, thoại `{…}` KHÔNG ngoặc kép. Render qua tool Bigup (cổng 2).
Khuôn = quy chuẩn DIRT ON HER HANDS (`F:\Tungnd\phim\DIRT_ON_HER_HANDS\_zh\QUY_CHUAN_VIET.md`, 31/10/2026, cùng look màu, cùng bảng 4 góc) áp vào bộ ảnh của phim này; chỗ nào phim này khác thì theo file này.
**Bài mẫu, đọc TRƯỚC khi viết:** (1) `F:\Tungnd\phim\EAT_IN_THE_KITCHEN\_zh\prompt\cum_001.txt` của phim NÀY (người điều phối viết, đã qua bộ kiểm) cùng phiếu `_zh\so_do\so_do_001.md`; (2) `F:\Tungnd\phim\DIRT_ON_HER_HANDS\_zh\prompt\cum_001.txt` (cách gắn mã, đặt máy ↔ panel); (3) `F:\Tungnd\Github\the-sorry-jar\05_prompt\video_zh\cum_001.txt` (giọng văn, độ dài).
Câu nào ghi **NGUYÊN VĂN** thì chép đúng từng chữ. **Ảnh thắng chữ**: câu chuẩn trong brief đã viết theo ảnh thật; kịch bản (04) viết trước khi có ảnh nên chỗ nào kịch bản nói trái / phải, trước / sau mà ảnh nói khác thì theo ảnh (mục 4).

## 0. Ràng buộc
- Mỗi người viết chỉ ghi các file của cụm mình: `_zh\prompt\cum_NNN.txt` (UTF-8, KHÔNG BOM, xuống dòng LF), `_zh\so_do\so_do_NNN.md` (mục 9) và, nếu đổi ảnh gửi, `_zh\refs_moi\cum_NNN.json` (mục 7). KHÔNG sửa `du_an.json`, `bible.json`, `anh\`, `_zh\anh_tham_chieu.json`, `_zh\data\`, `_zh\QUY_CHUAN_VIET.md`, `_zh\cong_cu\`, `_zh\brief\`, cụm của người khác.
- KHÔNG chạy lệnh tốn tiền (tạo ảnh, `gui_video.py` không `--thu`, `xuong.py`). KHÔNG chạy `xuong.py prompt`, `export_kich_ban_md.py` (viết đè prompt).
- Thư mục dự án: `F:\Tungnd\phim\EAT_IN_THE_KITCHEN`. Brief từng cụm: `_zh\brief\cum_NNN.md` (câu chuẩn, mã ảnh, kịch bản cụm, KẾT cụm trước, MỞ cụm sau). Tấm ghép ảnh có nhãn `@图片N`: `_zh\soat\anh_gui\cum_NNN.jpg` — **MỞ BẰNG Read, và mở thêm từng panel / bảng nhân vật khi cần xem kỹ** (`anh\<TÊN>.png`).
- Tài liệu dàn cảnh (đọc phần nơi của cụm mình): mặt bằng 4 tường, bảng "câu kịch bản → panel", 7 câu đời thực của từng nơi: `F:\Tungnd\Github\eat-in-the-kitchen\05_prompt\ghi-chu-dung\boi-canh-A-nha-bowie.md` (nhà Bowie trong / ngoài), `boi-canh-B-noi-lam-viec-cong-cong.md` (tiệm tạp hoá, Keystone, phòng hầm, Maison Bayou, văn phòng bán nhà), `boi-canh-C-lot7-va-cuoi-phim.md` (Lot 7, căn hộ Charlene, bệnh viện, toà án, hội trường nhà thờ, kho, phòng Devin). Tủ đồ và trạng thái liên tục: `tu-do-nhan-vat.md` cùng thư mục.
- Kiểm (miễn phí): `python -X utf8 F:\Tungnd\phim\EAT_IN_THE_KITCHEN\_zh\cong_cu\kiem_le.py <cụm…>` — dùng đúng bộ kiểm của skill, tự lấy refs từ `_zh\refs_moi\` nếu cụm có đổi ảnh. → **0 LỖI**, đọc hết CẢNH BÁO (CẢNH BÁO "nhắc tên … nhưng cụm không gửi ảnh" và "夜/阳光" phải sửa; CẢNH BÁO độ dài thì đọc lại).
- Viết TAY trọn bài từng cụm (không sinh bằng script, không ghép mảnh, không chép khối của cụm khác mà không đọc lại cho khớp vị trí / trang phục / ảnh).
- Độ dài: **mục tiêu ≤ 15.000 byte UTF-8** (> 15.000 cảnh báo, > 15.700 là LỖI không gửi được — B14). Đo bằng `wc -c`. Cụm 8–9 ảnh, 9–11 shot thì viết gọn thân shot (dòng 2 mỗi shot ≤ ~140 ký tự), không lặp ý.

## 1. Dữ liệu cứng của cụm (không được đổi)
- **Thoại**: nguyên văn, đúng thứ tự, đúng người nói, kể cả `...` và dấu `'` thẳng; mỗi câu `{…}` ở đúng đoạn `[a–b秒]` như kịch bản. Không thêm câu, không thêm tiếng cười / kêu có lời. Tên riêng chỉ nằm trong thoại (`Ines`, `Mama`, `Ms. Batiste`…).
- **Mốc giây**: đúng từng nhịp `[a–b秒]` của kịch bản (số nguyên, liền 0 → 30), kể cả nhịp 1–2 giây.
- **Ảnh gửi**: danh sách trong brief (thứ tự = `@图片N`). MỌI ảnh gửi phải được gọi ít nhất một lần. Một người một bảng trong một cụm.
- **Mở / Kết**: `【人物位置】开场时…` tả đúng khung MỞ (shot 1 kịch bản); `结尾时…` tả đúng khung KẾT (dòng `KẾT:` của cụm). Khung KẾT = vị trí MỞ cụm sau.
- **Chữ trên giấy / màn hình / điện thoại / thẻ**: `上面的字看不清`. Nhân vật đọc to thì giữ nguyên thoại.
- **Điện thoại**: kịch bản viết một phía hoặc cắt chéo hai nơi. Câu của người đầu dây chỉ vào `{…}` khi người đó CÓ MẶT trong khung ở nơi của họ (cụm cắt chéo: hai nơi, mỗi nơi panel riêng). Tiếng từ loa máy không có người trong khung: không viết thoại, chỉ tả cái máy áp tai.

## 2. Khuôn 9 khối (các khối cách nhau MỘT dòng trống)
Trong bài MỌI tên ngoài thoại có mã `TÊN（@图片N）` (nhân vật, panel, đạo cụ). Tên nhân vật trong bài = tên ảnh viết hoa không dấu: MARGUERITE, DEVIN, RAVEN, CHARLENE, **INES**, PRENTICE, ASHANTI, BERNICE, PEARL, MANAGER, BOUNCER, AGENT, GUARD, SECURITY, OKONJO, TANISHA, REPORTER, OFFICER, COORDINATOR, COWORKER, FOREMAN, APPLICANT. Nơi chốn không phiên âm tên riêng (Bowie, Keystone, Maison Bayou, Lot 7 → tả bằng chữ).

1. **Câu nhận ảnh** (một dòng, mở đầu bài): `参考图识别说明：BOWIE_KITCHEN_DAY（@图片1）、FOYER_STAIRS（@图片2）是同一栋房子一楼朝不同方向拍的场景图；RAVEN（@图片3）、MARGUERITE（@图片4）是两张人物图；PROP_BURGUNDY_BAG（@图片5）是一张道具图。每个名字后面括号里的编号就是它对应的参考图，请按这个编号认图，再用画面内容核对。`
   - hai nơi: `…A（@图片1）、B（@图片2）是<nơi 1>朝不同方向拍的场景图；C（@图片3）是<nơi 2>的场景图；…`. Ảnh chèn `LOC_LAUNDRY_NIGHT` là một场景图 riêng.
   - số: 一 两 三 四 五 六 七 八 (không `二张`). Không có đạo cụ thì bỏ vế đạo cụ.
2. **【场景图】** — dòng đầu: `【场景图】下面<两张/三张…>都是没有任何人物的横版照片，拍的是同一个<tên nơi>，每张朝一个方向：` (hai nơi: `…拍的是两个地方，每张朝一个方向：`). Mỗi panel MỘT dòng: `PANEL（@图片k）：<câu panel NGUYÊN VĂN trong brief>。` (không mở dòng bằng `- `). Dòng chốt: `这几张图只用来认<nơi>的样子和每个方向的背景，拍摄角度以下面每个镜头写明的机位为准，每个镜头的背景就是它写明的那一张。这是全片唯一的地方；<câu người nền>。` (hai nơi: `…这一段只有这两个地方：前<N>张是<…>，后<M>张是<…>，<ai đi từ A sang B qua cánh cửa nào / cắt chéo hai nơi>；<câu người nền>。`). Gửi ≥ 2 panel một nơi: thêm **câu phương vị** trong brief (chỉ giữ vế nói về các panel có gửi). Trạng thái khác ảnh → `图里<món / chỗ>这时<trạng thái mới>…`, lặp lại ở [保持不变].
3. **【人物参考图】** — câu mở NGUYÊN VĂN (có sẵn trong brief), rồi mỗi ảnh một dòng `- TÊN（@图片k）：<nhận diện NGUYÊN VĂN>。`; có câu "lấy phần" trong brief thì đặt ngay dưới.
4. **【道具图】** (chỉ cụm có ảnh đạo cụ), ngay sau 【人物参考图】: câu mở trong brief, rồi `PROP_X（@图片k）：<câu đạo cụ NGUYÊN VĂN>。<ở cụm này: tay ai / đặt ở đâu, từ giây nào>。`
5. **【人物位置】** — cụm nối liền cụm trước (shot 1 tiếp đúng KẾT cụm trước, không nhảy thời gian, cùng nơi) → `【人物位置】开场时（这一段紧接着上一段的最后一个画面往下拍，中间没有跳过任何时间，不是新的一场戏）：`; cụm mở cảnh mới / cách thời gian / đổi nơi → `【人物位置】开场时：`. Mỗi người MỘT dòng (không mở bằng `- `): `TÊN（@图片k）<trang phục NGUYÊN VĂN trong brief + trạng thái hiện tại>，<đứng/坐 ở đâu so với HAI mốc thật>，<mặt quay về mốc nào>，<cầm gì / tay nào>。` Người chưa vào khung: ghi trang phục rồi `；她这时还在<chỗ>，开场时看不见她，第N秒才第一次出现。` Dòng cuối: `开场机位：镜头在<chỗ>，和人的眼睛一样高，朝<mốc>拍，背景是<PANEL（@图片p）>：画面左边是…，画面右边是…；<ai quay lưng 看不见她的脸>。`
6. **Dòng 30秒** (một đoạn): `30秒美式剧情电影短片，对白全部为美式英语、逐字念出、每句一次、口型同步；全片没有背景音乐、配乐和旋律。这一段的内容，按时间顺序：在<nơi>里，<việc 1>；<việc 2>；…。<câu chặn bẫy mục 5>。只有A（@图片k）和B（@图片m）开口：先是A（@图片k）一句，再是B（@图片m）两句……；C（@图片n）全程不开口。全片只有下面<N>句英语台词，除此之外没有任何人说话。` (bộ kiểm cần nguyên cụm `全片只有下面<N>句英语台词` và `除此之外没有任何人说话`). Cụm có câu tiếng Pháp: mục 3a. Số câu `<N>` = số thoại kịch bản (五句 / 六句…). KHÔNG câu giới thiệu vai; quan hệ gói vào sự việc; hành động chính phải có mặt ở đây.
7. **Mỗi shot HAI dòng**:
   `[a–b秒] TÊN（@图片k）<cỡ cảnh>，<ai đang làm gì theo NGHĨA cảnh>，<góc>，<máy>。`
   `镜头在<chỗ đặt máy so với mốc / người>，朝<mốc>拍，背景是<PANEL>（@图片p）的<mốc CÓ trong panel đó>：<ai ở trái / phải khung, ai quay lưng>；<động tác ngắn, 1–2 chi tiết nhìn thấy>，用英语清清楚楚地说：{…}`
   Cỡ cảnh: `全景 / 中景 / 中近景 / 近景 / 特写 / 双人中景 / 过肩中景`; góc: `正面角度 / 侧面角度 / 过肩角度 / 背面角度 / 低角度 / 高角度`; máy: `镜头不动 / 镜头缓慢推近 / 镜头跟着X（@图片k）移动 / 镜头缓慢拉远`. Dòng 1 nói Ý NGHĨA khoảnh khắc (giật túi, đuổi xuống ăn trong bếp, chửi bằng tiếng Pháp, lật bài, vạch trần…). Dòng 2 chỉ nhắc mốc CÓ trong panel nền. Nhịp không thoại vẫn tả kín hành động. Mỗi người 1–2 chi tiết nhìn thấy mỗi shot. Kịch bản "giọng nhỏ nhưng rõ" → `声音很冷，但一字一字很清楚` (KHÔNG `压低 轻声 小声 低声 喃喃 耳语 悄悄`).
8. **Đoạn cuối**: hành động sau thoại cuối, đúng **một** câu `从这里到结尾没有人再说话。` (cụm có thoại tới giây 30 thì bỏ), rồi `结尾时<ai ở đâu, quay về đâu, cầm gì>；<những ai>都在画面里。` (người đã rời khung: `X（@图片k）已经不在画面里`).
9. **镜头语言 + [保持不变]**: `镜头语言：<cỡ cảnh từng đoạn nối bằng →>，固定机位为主，自然运镜。环境音全程：<…>，随后<…>，结尾<…>。` (không nhạc) rồi `[保持不变] 全程以<PANEL（@图片1）、…>这几张图里的同一个<nơi>为唯一的地方，镜头一直在<…>里，不切到别的地方；全程保持A（@图片k）…的五官、发型、服装、肤色与各自人物图一致，不换脸、不新增人物；站位锁：<mục 4>；<2–6 câu chặn riêng>；` + **câu chốt NGUYÊN VĂN** (trong brief, từ `所有人的眼白都干净，不发红；` tới hết). Hai nơi: `全程只在两个地方：<A…>这几张图里的<nơi A>，和<B…>这几张图里的<nơi B>，不切到别的地方；…`. Người đổi trạng thái đồ so với ảnh trong cụm (cởi tạp dề, tháo thẻ, khoác áo…): không khoá `服装与人物图一致` cho người đó; khoá theo trạng thái đúng giây.

## 3. Luật chữ
- Cấm: `打` (trừ `打乱`; 打开→拉开/推开/掀开, 打电话→拨电话/讲电话, 打量→从上到下看着, 打翻→碰翻, 打印→印), `二张`, `血 枪 杀 暴力 性感 低胸`, số ảnh `图1`, `Image 1`. Tránh `胸`: 胸前 → 衣襟上 / 身前; 胸针 → 别针.
- **Không chữ giờ**: 上午 下午 中午 早上 早晨 清晨 傍晚 黄昏 晚上 夜晚 深夜 午后 白天 晨光 夕阳 日落 夜色 凌晨 半夜 午夜 正午 入夜 天黑 天亮 黎明 拂晓 夜里 夜间 今晚 今早 当晚 点钟, `<số>点`; tránh `夜 阳光 日光`. Ánh sáng do ảnh quyết; khác ảnh thì tả bằng thứ nhìn thấy (`窗外黑漆漆的`, `门廊灯亮着`). Thoại có "tonight / morning" là thoại, giữ nguyên.
- **Mắt (A1+G7):** KHÔNG `眼泪 / 哭 / 眼里含着泪 / 眼眶湿润 / 红` gắn mắt. Cảnh khóc / sốc / sụp đổ tả bằng hàm / môi / giọng / tay: `下巴发抖，嘴唇抿紧，用手背擦了一下脸，声音发颤却很清楚`; mỗi cận mặt thêm `眼白干净，眼睛和人物图一样清亮自然`. Kịch bản ghi "nước mắt đọng ở khoé mắt" (C70) → tả bằng giọng / hàm, không chữ nước mắt.
- **Mặt (A12/A17):** không `脸色一变 / 涨红 / 通红 / 红肿 / 红晕 / 泛红`; không màu nào trên má / mặt.
- Chữ im lặng chỉ MỘT lần cả bài (`从这里到结尾没有人再说话。`); người có mặt không nói: `只有A和B开口` + `C全程不开口`. Không `安静戏 / 对话戏 / 先是笑…然后…`.
- Không `跪` ở đoạn mở. Không câu nào về chủng tộc ngoài câu khoá màu da trong câu chốt.
- Đoạn `[0–…秒]` đầu phải có `站 / 坐 / 停在 / 躺 / 靠`; đoạn cuối có `结尾时`; shot đầu không mở bằng cận tay / hành động `走进来 推门 刚到`.
- Thoại là câu nguyên văn; KHÔNG thêm tiếng Trung trong `{…}`; KHÔNG nhắc tên nhân vật không gửi ảnh ở cụm.

### 3a. Thoại TIẾNG PHÁP (11 câu: C3 Raven 10–13 · C5 Charlene 5–8 · C6 Marguerite 2–5 và 5–8 (nửa Pháp nửa Anh) · C7 Marguerite 2–6 · C15 Inès 2–5 · C16 Inès 2–5 và Marguerite 18–21 · C24 Inès 5–9 · C30 Inès 4–7 và Marguerite 14–17 — brief có thể sót, danh sách này là chuẩn)
- Dòng 30秒 đổi vế đầu thành: `30秒美式剧情电影短片，对白除了写明用法语说的句子以外，全部为美式英语，逐字念出、每句一次、口型同步；…`; câu khoá thoại giữ nguyên khuôn `全片只有下面<N>句英语台词，除此之外没有任何人说话。` (N = tổng số câu, kể cả câu tiếng Pháp; bộ kiểm cần đúng cụm này) và thêm ngay sau một câu `其中第<k>句是法语。` (hoặc `其中第<k>句和第<m>句是法语。`; câu nửa Pháp nửa Anh: `其中第<k>句先说法语再说英语。`).
- Câu tiếng Pháp thuần: `用法语清清楚楚地说：{Elle sent la friture.}`. Câu nửa Pháp nửa Anh (C6): `先用法语、再用英语清清楚楚地说：{Elle sent la friture. She smells like grease.}`. Giọng: Raven / Charlene nói tiếng Pháp kiểu học ở trường, giọng chế giễu; Marguerite và Inès nói tiếng Pháp lưu loát, tự nhiên.
- Không dịch câu tiếng Pháp sang tiếng Trung trong bài; nghĩa chỉ thể hiện qua cử chỉ / phản ứng nhìn thấy.

## 4. Hình học bối cảnh — luật nền (bắt buộc)
1. **Nền của một shot = bức tường máy NHÌN TỚI** (sau lưng người được quay). Panel k nhìn VỀ tường k; trái khung = tường k−1, phải khung = tường k+1. Dòng 2 mỗi shot phải có `镜头在<chỗ>，朝<mốc>拍，背景是<PANEL>（@图片p）的<mốc CÓ trong câu panel>`. Không tả mốc sau lưng máy.
2. **Hai người đối diện nói chuyện (A ↔ B):** cú của A quay từ phía B → nền = tường sau lưng A; cú của B → nền = tường sau lưng B → **hai panel NGƯỢC nhau** (cặp ngược: ô1↔ô3, ô2↔ô4 của cùng bảng; brief ghi sẵn panel ĐỐI DIỆN và có gửi hay không). TUYỆT ĐỐI không dùng cùng một panel cho hai cú ngược.
3. **Trục 180°:** trong một chuỗi đối thoại máy ở cùng một bên trục → A luôn ở cùng một phía khung; ghi rõ `A在画面左边，B在画面右边`. Qua vai: máy sau **vai phải** X ⇒ vai / đầu X ở mép **TRÁI** khung; sau **vai trái** ⇒ mép **PHẢI**.
4. **Hướng mặt khớp nền:** ai quay mặt về tường X thì chỉ thấy mặt khi máy ở phía X nhìn ngược lại. Người quay lưng về máy: `背对镜头，看不见她的脸`.
5. **Bảng vị trí (站位):** mỗi người đứng / ngồi ở đâu so với HAI mốc có thật trong ảnh, mặt về mốc nào; ai di chuyển thì viết đường đi trong shot đó; không ai "nhảy" chỗ giữa hai shot; người đứng sau lưng máy KHÔNG thể có trong khung.
6. **Trái / phải của bàn dài, quầy, giường** neo bằng mốc phòng (`长餐桌靠厨房的那一头`, `病床靠窗的那一边`), không viết trần "bàn bên phải".
7. **Trong / ngoài cửa, cổng sắt:** ai ở trong, ai ở ngoài ghi rõ mỗi shot gần cửa / cổng (C57–C62: bà Marguerite PHÍA TRONG cổng sắt Lot 7, Devin / Raven / Charlene / phóng viên / hàng xóm PHÍA NGOÀI); máy đổi phía thì panel đổi theo.
8. **Câu khoá vị trí ở [保持不变] (bắt buộc, `站位锁：`)**: mỗi người ở đâu suốt cụm + panel nền của cú chính diện từng người, ví dụ `站位锁：MARGUERITE（@图片4）一直站在前门旁边的白色边柜前，面朝厨房；RAVEN（@图片3）从厨房岛台走到她面前，隔着一步；拍MARGUERITE（@图片4）正脸的镜头背景是FOYER_STAIRS（@图片2）的前门，拍RAVEN（@图片3）正脸的镜头背景是BOWIE_KITCHEN_DAY（@图片1）的厨房，两边背景不互换。`
9. **Mặt bằng từng nơi**: đọc mục "mặt bằng / bảng câu kịch bản → panel" của nơi mình trong `boi-canh-A/B/C.md`. Tóm tắt nhà Bowie (dùng nhiều nhất): một khối mở, 4 tường theo chiều kim đồng hồ = **bếp** (ô 1: đảo bếp đá trắng, ghế đỏ rượu, bồn rửa dưới cửa sổ bên trái, cửa gỗ hẹp phòng giặt ở đầu PHẢI bếp) → **tường tủ buffet + bàn ăn** (ô 2) → **cửa chính** (ô 3: bàn console + gương tròn bên trái cửa, chân cầu thang trắng bên phải) → **sofa chữ L dưới hai cửa sổ** (ô 4). Cặp ngược: bếp ↔ cửa chính, bàn ăn ↔ sofa.

### 4b. Chỗ ẢNH khác ghi chú mặt bằng / kịch bản (đã soi ảnh thật — ảnh thắng; viết theo ảnh, món ảnh không có mà kịch bản cần thì tả thêm bằng chữ)
- **Nhà Bowie (trong):** bồn rửa nằm dưới cửa sổ giữa-trái phía sau đảo bếp (mép trái khung bếp là cửa sổ phòng khách); khăn sage treo ở tủ bên phải bếp nấu. Tường bàn ăn có HAI tranh trừu tượng; "quạt nhà thờ" trên tủ buffet là lá cọ vàng khô trong hai bình — C10 giây 12–15 cần quạt giấy cán gỗ: tả bằng chữ (`一把纸做的教会扇子，木头扇柄`). Bảng tiệc: hai bình trà đá (trên buffet và trên bàn console cửa chính); bóng bay ở đầu bàn phía bếp, bên buffet = ghế Charlene. Không thấy dây sạc điện thoại.
- **Nhà Bowie (ngoài):** ba bậc thềm bê tông (không phải bốn); cây phong bên trái đã đỏ hẳn. Đêm: cả ba cửa sổ tầng trên sáng đèn; xe khách đỗ dọc lề phía bên kia đường. Tuyết: tờ thông báo trắng dán bốn góc bằng băng dính cam, ở nửa trên cánh cửa.
- **Tiệm tạp hoá:** quầy bên PHẢI (sát cửa) = quầy 1, bên trái = quầy 2 (nhìn từ phía sau quầy thì quầy 1 ở bên trái); hũ quyên góp ở quầy 2. MARKET không có kệ đồ hộp thấp ở góc trái (C14 giây 19–23 cần → tả bằng chữ hoặc đổi sang kệ bên phải khung). GROCERY_AISLES không có xô lau nhà, không có đậu bắp.
- **Phòng họp Keystone:** tủ credenza trong HEAD có đèn bàn + cây xanh, trong CREDENZA có kẹo bạc hà + lan, không đèn — chỉ nhắc món có trong panel nền. DOOR: ghế lưới thứ bảy ở đầu bàn phía cửa, bàn để bình nước đứng giữa trước vách kính. DOOR_NIGHT: văn phòng sau kính còn nhiều đèn trần mờ. **KEYSTONE_CONF_GLASS (từ tầng văn phòng nhìn vào phòng họp) KHÔNG khớp phòng họp** (không thấy cửa kính, bàn chạy song song vách kính): chỉ dùng làm nền mờ, không cho thấy màn hình qua kính. KEYSTONE_FLOOR_WINDOWS: cả hai bàn cạnh cửa sổ đều trống.
- **Phòng hầm:** khung ảnh kính nứt trên bàn là khung lớn, không có ảnh → cận khung theo PROP_LOUISIANA_FRAME; hai cái bát đứng ngửa, hai ấm nước. Panel DRESSER thấy cửa đóng, panel DOOR thấy cửa mở vào trong.
- **Lot 7:** LOT7_DINING_ARCH thấy qua vòm một tiền sảnh KHÁC bảng tiền sảnh (cầu thang lan can trắng ở bên trái, cửa kính ô vuông, bàn tròn có hoa cẩm tú cầu) → shot nào nền là vòm thì không tả tiền sảnh phía sau. LOT7_DINING_ARCH có HAI đĩa viền xanh → kịch bản C68–70 chỉ MỘT chỗ ngồi đầu bàn: viết `桌上只有一个盘子`. Phòng ăn có hai cửa sổ; LOT7_DINING_KITCHEN thấy hai nồi đen trên bếp, không thấy hũ filé / chai tương ớt. LOT7_WORK: ảnh căn nhà là một bức tranh lớn trên tường sau bàn (nhà kem hai tầng có cột) → cận khung ảnh nhỏ trên góc bàn (C66) theo PROP_LOUISIANA_FRAME_NEW, không tả bức tranh. Kính cửa chính: trong nhà (LOT7_FOYER_DOORS) là kính gợn lớn dưới ô cửa bán nguyệt rộng; ngoài nhà (*_HOUSE) là kính ô vuông, ô bán nguyệt nhỏ trên cửa — tả theo panel nền đang dùng. Tuyết: cẩm tú cầu còn hoa khô màu nâu nhạt; không thấy rõ vỉa hè ngoài cổng.
- **Căn hộ Charlene:** cửa phòng ngủ ở bên PHẢI sofa (phía bếp), không phải phía cửa chính; CHARLENE_DOOR không thấy cửa phòng ngủ. "Quạt nhà thờ" là một chiếc quạt vàng trong bình tím. Hộp mũ tím trên tủ lạnh.
- **Phòng bệnh:** HOSP_BED không thấy dây gọi y tá trắng (C52 giây 0–4, C53 giây 26–28 cần → tả bằng chữ `床栏上夹着一根白色呼叫铃线`); đầu giường nằm phẳng; hoa vàng có cả trên tủ đầu giường. HOSP_DOOR thấy thành giường ở góc dưới phải → C53 giây 28–30 (máy cạnh cửa sổ nhìn về cửa): Charlene ở mép PHẢI khung (kịch bản ghi mép trái — theo ảnh).
- **Hành lang toà án:** ghế băng chỉ có trong COURT_DOORS và COURT_WINDOWS; COURT_HALL_WEST không có ghế dọc tường phải.
- **Hội trường nhà thờ:** thánh giá gỗ trơn ở cùng tường với cửa ra (thấy trong CHURCH_HALL_OUT và CHURCH_HALL_EXIT).
- **Phòng Devin:** bếp ga có kiềng, tủ lạnh thường (ngăn đá trên); móc treo dây đeo cam không thấy từ hướng cửa → C67 giây 0–3 cần thì tả bằng chữ.
- **Nhân vật (theo ảnh):** tóc xoăn của bà Marguerite xoã dày che tai (không vén sau tai) — tả theo ảnh; vết bỏng tay trái không thấy trong ảnh → cận tay thì viết `左手手背上有一块淡淡的旧烫伤疤痕`. M1 gi-lê bốn cúc. V0 henley tay NGẮN (kịch bản C18–20 ghi dài tay — theo ảnh). V4 áo phao mở khoá hẳn. R4 / R5 tóc bob vẫn mượt (kịch bản "hơi xù chân tóc" → thêm chữ `发根有点毛躁` ở cận mặt nếu muốn); R5 xổ tóc từ C60 viết bằng chữ. Charlene: lọn tóc bạc rõ ở trán; CH5 / CH5C / CH5W vẫn có son và khuyên vàng, CH5W có đồng hồ vàng cạnh vòng tay bệnh viện, chân trần. CH6 son đậm, không áo dạ vắt tay, không túi → C63 áo dạ tím vắt tay tả bằng chữ. Sister Pearl SP1 / SP2 màu đỏ rượu (酒红色), giống tông Raven — không đứng cạnh Raven trong cùng khung mà không nêu tên rõ. COORDINATOR tóc locs dài quá vai, khuyên bạc nhỏ.

## 5. Bẫy dàn cảnh của phim này (chặn ở khối 6 và [保持不变]; câu mẫu tên trơn, chép vào bài thì gắn mã)
| Cụm | Bẫy | Chặn |
|---|---|---|
| 1–3 (giật túi, sáng sinh nhật) | xô xát, đánh nhau, ngã | `RAVEN只是一把从她手里抽走包，没有人推人，没有人倒下`; không ai chạm người khác ngoài cú giật túi |
| 4–10 (tiệc sinh nhật Charlene) | tiệc vui: nâng ly, hát mừng, mọi người ăn uống cười nói, Marguerite ngồi ăn cùng | `这不是欢乐的聚会：没有人举杯，没有人唱歌`; khách ngồi yên, chỉ nhìn; `MARGUERITE一直站着，没有坐到餐桌边` (trừ chỗ kịch bản ghi); chửi bằng tiếng Pháp chỉ là lời nói, không ai động tay |
| 10–11 (kéo vali ra hiên, khung ảnh rơi) | đẩy ngã, ném đồ vào người, khóc ôm | vali tự bung / rơi theo kịch bản, `没有人推她`; Devin chỉ đứng trong khung cửa rồi đóng cửa |
| 12–17 (tiệm tạp hoá) | trộm cướp, rượt đuổi, đánh nhau; mua sắm vui vẻ | đúng sự việc kịch bản; `没有人动手`; người nền chỉ đứng xếp hàng |
| 22–31 (Keystone, đề án, đoàn Pháp) | họp vui, bắt tay ăn mừng, vỗ tay, nâng ly | `这不是庆祝`; chỉ ký giấy / trao séc đúng kịch bản; đoàn đối tác Pháp không nói |
| 34–38 (Maison Bayou) | bữa tối vui, nâng ly; bảo vệ xô đẩy | `不是用餐聚会：没有人举杯`; bảo vệ chỉ đưa tay chỉ cửa, đi cạnh, không ai bị kéo hay đẩy |
| 39–43 (văn phòng bán nhà, Lot 7) | Marguerite bị đuổi, bảo vệ lôi đi | đúng kịch bản: bà là chủ nhà; bảo vệ khu chỉ hỏi, đứng ở cửa |
| 45–47 (đuổi việc) | đánh nhau, ném đồ | Devin nộp thẻ, ôm thùng giấy; bảo vệ toà nhà chỉ đi cạnh |
| 52–55 (phòng bệnh, bệnh án giả) | cảnh y tế: tiêm, mổ, cấp cứu, máy kêu; bắt giữ thô bạo | `这不是抢救的戏`; bác sĩ chỉ đứng cầm bìa hồ sơ nói; bảo vệ bệnh viện chỉ giữ khuỷu tay TANISHA (một lần, đúng kịch bản); Charlene bỏ chạy chỉ đi nhanh ra cửa |
| 57–62 (livestream trước cổng, cảnh sát) | bạo động, súng, đè người, còi hú | `OFFICER腰带上只有手铐套和对讲机`; `没有人被按倒，没有推搡，没有警笛声`; còng đúng người, đúng giây kịch bản; hàng xóm đứng yên ngoài vỉa hè |
| 63 (toà án) | phiên toà, thẩm phán | chỉ hành lang ngoài phòng xử; không có thẩm phán |
| 64 (bếp từ thiện) | tiệc nhà thờ vui vẻ | đúng việc múc gumbo / rửa nồi; `这不是庆祝`; người xếp hàng im lặng (trừ tiếng cười khẽ kịch bản ghi) |
| 65 (kho) | tai nạn xe nâng | xe nâng đỗ yên |
| 68–70 (sinh nhật 67, bàn ăn) | đoàn tụ ôm khóc, cả nhà tiệc tùng | `不是久别重逢的拥抱：没有拥抱` (KHÔNG viết 哭 / 眼泪 kể cả phủ định); chỉ đúng một cái chạm kịch bản ghi (tay trái có vết bỏng đặt lên cẳng tay Devin); hai người ngồi CÙNG bàn ăn, không ai ăn trong bếp |
| mọi cụm có điện thoại | gọi video, màn hình sáng có chữ | `屏幕上的字看不清`; người đầu dây chỉ xuất hiện khi kịch bản cắt chéo |

## 6. Trạng thái kéo dài nhiều cụm — ảnh KHÔNG vẽ → viết bằng chữ
- **Marguerite:** vết bỏng cũ mờ trên mu bàn tay TRÁI (mọi cụm có cận tay); không trang sức trừ thánh giá vàng nhỏ ở M2, M3, M4 (M3W bị khăn che); M0A = M0 + tạp dề trắng có vết ố (cụm 4–9, cởi tạp dề ở cụm 9 giây 19 → sau đó như M0). Điện thoại nắp gập bạc trầy (PROP_FLIP_PHONE) trong túi gi-lê M1 / trên bàn làm việc.
- **Devin:** kính gọng chữ nhật kim loại mảnh MỌI cụm. V1 có thẻ nhân viên dây xanh tới cụm 47 giây ~10 (tháo nộp) → cụm 47 phần sau, 48, 49: `领口空着，没有工牌`. V4 / V4H: râu lún phún, tóc Caesar dài ra (cụm 50–62); cụm 57–59 mũ trùm hoodie kéo lên theo kịch bản. Cụm 63 trở đi cạo sạch, tóc gọn.
- **Raven:** móng hạnh nhân be hồng ánh vàng + khuyên kim cương tới cụm 62; tóc bob hơi xù chân tóc từ cụm 50, **xổ ra từ cụm 60**; R6 / R7 (cụm 63–64): tóc dài quá cằm, chân tóc đen mọc khoảng hai phân, kẹp sau tai, không khuyên, không trang điểm, móng cắt ngắn — ảnh chưa vẽ rõ chân tóc → viết bằng chữ. Túi: **túi da đỏ rượu khoá vàng** (PROP_BURGUNDY_BAG) cụm 1–43 khi kịch bản nhắc; **túi da bóng đen mới** (PROP_BLACK_BAG) từ cụm 44 (cụm 48 dù KẾT ghi R2 thì túi là túi đen).
- **Charlene:** kính mắt mèo gọng đen MỌI cụm; CH1 = CH3 + mũ nhà thờ tím rộng vành; vòng tay bệnh viện trắng cổ tay trái từ cụm 52 tới 62; cụm 55 chạy khỏi bệnh viện khoác vội áo dạ tím sẫm, chân đi tất; cụm 63 áo dạ tím sẫm vắt trên cẳng tay (không có ảnh đạo cụ → chữ).
- **Khung ảnh căn nhà Louisiana:** kính nứt chéo từ cụm 11 (PROP_LOUISIANA_FRAME) → kính đã thay ở cụm 66 (PROP_LOUISIANA_FRAME_NEW). Ảnh nhỏ trong khung trên bảng LOT7_WORK / BASEMENT_TABLE vẽ kiểu cũ: cụm có cận khung thì nền theo ảnh đạo cụ.
- **Mùa:** cụm 1–49 tháng 9–10 (cây xanh / lá vàng tháng Mười ở Lot 7); **cụm 50–62 tuyết tháng Giêng** (tuyết cũ đọng dọc mép cỏ, hơi thở phả khói — tả bằng thứ nhìn thấy, không chữ giờ); 63–64 đầu xuân; 65–70 tháng Chín năm sau.
- Đồ khác ảnh: tả thẳng trạng thái hiện tại, không câu phủ định (A14).

## 7. Thêm / bớt PANEL
- Được thêm panel cùng nơi khi cần cú ngược / hướng máy kịch bản ghi mà cụm chưa gửi; được bỏ panel KHÔNG shot nào nhìn tới; tổng ≤ 9 ảnh. KHÔNG bỏ nhân vật có thoại hay có cận mặt; người chỉ ở hậu cảnh toàn cảnh (vd Sister Pearl cụm 4, Sister Bernice ở cụm không có thoại của bà) được bỏ ảnh khi thiếu chỗ — khi đó tả bằng 1–2 chi tiết đồ mặc, không tên, không mã. Đạo cụ gửi mà ngoài khung cả cụm thì bỏ.
- Thứ tự mới: panel (theo nơi, rồi thứ tự xuất hiện) → nhân vật (giữ thứ tự cũ) → đạo cụ (giữ thứ tự cũ). `@图片N` trong bài phải theo thứ tự MỚI.
- Ghi `_zh\refs_moi\cum_NNN.json` = `{"N": ["PANEL…", …, "SHEET_TÊN_MÃ", …, "PROP_…"]}` (N không số 0 đầu; đúng tên file ảnh trong `anh\`). Không đổi thì KHÔNG tạo file. `kiem_le.py` tự dùng file này.

## 8. Người nền, người không có ảnh
- Câu người nền: lấy trong brief, chỉnh số lượng / vị trí theo kịch bản cụm.
- Người có trong kịch bản mà cụm KHÔNG gửi ảnh (khách tiệc, đoàn Pháp, phục vụ, thu ngân trẻ, bảo vệ bệnh viện, cảnh sát thứ hai, hàng xóm…): không tên, không mã, không cận mặt; tả bằng 1–2 chi tiết đồ mặc, không thoại.

## 9. Phiếu sơ đồ `_zh\so_do\so_do_NNN.md` (viết TRƯỚC khi viết chữ Trung)
```
# Cụm N — <tên>
Nơi: … — panel đang có (và cặp ngược)
## Vị trí mở
- TÊN: đứng/ngồi ở <mốc>, mặt về <mốc>, cầm …   (khớp KẾT cụm N−1: có/không, lệch gì)
## Bảng shot
| Giây | Ai | Máy ở đâu | Nhìn về | Panel nền | Trái khung | Phải khung |
## Cặp ngược đã dùng: A ↔ B (shot …)
## Kết: … (khớp MỞ cụm N+1: có/không)
## Lệch ảnh ↔ kịch bản đã xử lý / Cần người dùng quyết
```
Ngắn gọn (một màn hình). Đây là chỗ soát hình học: mỗi shot ghi rõ máy ở đâu và nhìn về tường nào, rồi mới viết chữ.

## 10. Checklist trước khi nộp một cụm
- [ ] Khối đủ và đúng thứ tự: câu nhận ảnh → 【场景图】 (+phương vị) → 【人物参考图】 → (【道具图】) → 【人物位置】 → 30秒 → các shot → 镜头语言 → [保持不变].
- [ ] Mọi ảnh gửi được gọi; mã `（@图片N）` đúng số ở MỌI chỗ ngoài thoại (kể cả `开场机位`, `结尾时`, 站位锁).
- [ ] Thoại đúng nguyên văn, đúng người, đúng mốc; số câu ở 全片只有下面X句 đúng; câu tiếng Pháp theo 3a.
- [ ] Mỗi shot: dòng 2 có chỗ đặt máy + hướng + nền bằng panel đúng hình học; cú ngược dùng panel ngược; trục 180° giữ.
- [ ] Vị trí / trang phục từng người khớp ảnh và khớp KẾT cụm trước / MỞ cụm sau.
- [ ] Không chữ cấm, không chữ giờ, không nước mắt / mắt đỏ, không người vắng mặt bị nhắc tên.
- [ ] `kiem_le.py` 0 LỖI; ≤ 15.000 byte.
