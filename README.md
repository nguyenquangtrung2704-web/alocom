# Đặt Cơm Online bằng Python + Streamlit

## Thành phần
- `app.py`: ứng dụng chính
- `requirements.txt`: thư viện Python cần cài
- `supabase-schema.sql`: tạo bảng dữ liệu trên Supabase
- `.streamlit/secrets.toml.example`: mẫu cấu hình khóa kết nối

## Bước 1 — Tạo Supabase
1. Tạo project trên Supabase.
2. Vào SQL Editor.
3. Copy toàn bộ file `supabase-schema.sql` và bấm Run.
4. Lấy Project URL và Publishable key.

## Bước 2 — Chạy online bằng Streamlit Community Cloud
1. Tạo tài khoản GitHub.
2. Tạo repository mới, ví dụ `dat-com-online`.
3. Upload các file trong thư mục dự án này lên repository.
4. Vào `https://share.streamlit.io`.
5. Đăng nhập bằng GitHub.
6. Chọn `Create app`.
7. Chọn repository vừa tạo.
8. Main file path: `app.py`.
9. Trước khi chạy, vào App settings / Secrets và nhập:

SUPABASE_URL = "PROJECT_URL_CUA_CO"
SUPABASE_KEY = "PUBLISHABLE_KEY_CUA_CO"

10. Deploy.

Streamlit sẽ cấp link dạng:
`https://ten-ung-dung.streamlit.app`

## Bước 3 — Chạy trên máy tính nếu muốn
Tạo file `.streamlit/secrets.toml` từ file mẫu, sau đó chạy:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Chức năng V1
- Nhập họ tên.
- Chọn ngày.
- Chọn món ăn.
- Chọn số lượng.
- Nhập ghi chú.
- Tự tính tiền.
- Lưu đơn online vào Supabase.
- Xem đơn theo ngày.
- Xóa đơn.
- Dashboard số đơn / số suất / tổng tiền.
- Tổng hợp theo món.
- Tổng hợp theo người.

## Lưu ý
V1 chưa có đăng nhập. Người có link có thể xem và xóa đơn.
Nếu sử dụng chính thức cho nhiều người, nên làm V2 với đăng nhập và phân quyền.
