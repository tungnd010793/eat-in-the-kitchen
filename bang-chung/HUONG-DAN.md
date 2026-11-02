# BẰNG CHỨNG (tự động, đừng sửa tay)

| Thành phần | Ý nghĩa |
|---|---|
| `manifest/*.sha256.txt` | Mã SHA-256 của **mọi file** trong dự án tại một thời điểm, kể cả video không đẩy lên GitHub |
| `manifest/*.ots` | Dấu thời gian **OpenTimestamps**: mã của manifest được ghi vào blockchain Bitcoin. Vài giờ sau mới hoàn tất, và từ đó không ai, kể cả bạn, sửa lùi ngày được |
| `manifest/*.tsr` | Dấu thời gian **RFC 3161** do FreeTSA cấp ngay, có chữ ký số của bên thứ ba |
| `freetsa-cacert.pem`, `freetsa-tsa.crt` | Chứng chỉ của FreeTSA, dùng để xác minh file `.tsr` |
| `khoa-ky-so.pub`, `allowed_signers` | Khóa công khai của tác giả, dùng để xác minh chữ ký trên các commit |

## Chuỗi chứng minh
File video → mã SHA-256 nằm trong manifest → manifest có dấu thời gian (Bitcoin + FreeTSA) → **file đó đã tồn tại muộn nhất vào thời điểm đó.**

Bấm `KIEM-TRA.bat` để xem mỗi file có bằng chứng sớm nhất từ khi nào.

## Tự xác minh, không cần bộ công cụ này
- **SHA-256 của một file:** `certutil -hashfile "đường\dẫn\file.mp4" SHA256`
- **OpenTimestamps:** kéo thả file manifest và file `.ots` cùng tên vào https://opentimestamps.org
- **FreeTSA:** `openssl ts -verify -data <manifest> -in <manifest>.tsr -CAfile freetsa-cacert.pem`
- **Cả manifest:** mở Git Bash tại thư mục gốc dự án: `sha256sum -c bang-chung/manifest/<tên>.sha256.txt` (bỏ qua cảnh báo về các dòng `#`)
