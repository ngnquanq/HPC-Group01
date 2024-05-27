# Giới thiệu 

Repository này là đồ án môn học Tính Toán Hiệu Suất Cao, **mã học phần: INF50907701**

Các thành viên bao gồm:
- Nguyễn Nhật Quang
- Lê Minh Triều
- Thái Bảo An
- Vương Chí Bình
- Lê Ngọc Anh Hùng

Trong khuôn khổ đồ án, nhóm xây dựng **hệ thống phân loại ảnh** đơn giản với Docker và các framework khác trong Python để hỗ trợ (PyTorch, FastAPI,v.v...)

# Cách chạy
Đầu tiên, để chạy được mô hình, cần một file trọng số, file này mọi người có thể tải từ google drive, sau đó cho vào thư mục: `models\weights\<file trọng số>`.

Link của file trọng số mình để ở link [này](https://drive.google.com/file/d/1AeKAv96_khbQGLbylIRMMHHDW0f4guL_/view?usp=sharing)

Sau khi giải nén vào thư mục đó thành công, nhìn cấu trúc file của mọi người sẽ như thế này: 

![File_Structure](/images/file_structure.png)

Kế đến mọi người có thể chạy lệnh: `docker compose up --build` để chạy. Lúc này nhìn nó như hình:

![Docker](/images/docker.png)

Cuối cùng, mọi người đừng có thể truy cập vào đường dẫn [`localhost:8000\docs`](localhost:8000\docs) để truy cập vào SwaggerUI của FastAPI rồi kiểm tra thử các endpoint của ứng dụng. Nhìn cái SwaggerUI sẽ như hình sau:

![SwaggerUI](/images/swaggerui.png)

# Lời kết
Xin 1 ✨, cảm ơn.

Cheers
