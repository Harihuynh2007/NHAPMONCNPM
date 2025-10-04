# 🛠️LAB01:  Software Engineering Project – TaskNest

## 📌 Giới thiệu
**TaskNest** là một hệ thống quản lý công việc nhóm theo mô hình **Kanban**, được phát triển trong môn *Nhập môn Công nghệ Phần mềm*.  
Mục tiêu dự án: áp dụng kiến thức **fullstack web** để xây dựng nền tảng hỗ trợ nhóm/doanh nghiệp trong việc **tạo, quản lý, phân loại, kéo-thả và lọc thẻ công việc**.

---

## 👥 Thành viên nhóm
- Huỳnh Minh Hải – Leader, Backend Developer, ux/ui  
- Nguyễn Bá Bảo Nam – Frontend Developer  


---

## 🎯 Mục tiêu
- Ứng dụng kiến thức fullstack để xây dựng hệ thống quản lý công việc trực tuyến.  
- Tối ưu trải nghiệm người dùng với tính năng **drag & drop**.  
- Đáp ứng nhu cầu quản lý dự án: phân quyền, cộng tác thời gian thực, theo dõi tiến độ.  

---

## 📂 Nội dung chính
- Thiết kế giao diện (UI/UX) trực quan, hỗ trợ kéo–thả danh sách/thẻ.  
- Tích hợp **Authentication & Authorization**: JWT + Google OAuth.  
- Xây dựng **API** quản lý board, danh sách, thẻ, nhãn, thành viên, bình luận.  
- Đảm bảo bảo mật, quản lý session và hiệu năng hệ thống.  

---

## 🎯 Use Case chính
- Quản lý người dùng (đăng ký, đăng nhập, phân quyền).  
- Quản lý board, danh sách, thẻ (Kanban).  
- Hỗ trợ cộng tác (thành viên, bình luận, thông báo).  
- Báo cáo & phân tích tiến độ.  

*(Sơ đồ use case có thể chèn hình ảnh vào đây)*

---

## 📐 Thiết kế hệ thống
- **Use Case Diagram**: [Xem chi tiết tại đây](https://github.com/Harihuynh2007/NHAPMONCNPM/blob/main/uml/readme.md#lab-03--uml-thi%E1%BA%BFt-k%E1%BA%BF-use-case--sequence-diagram)
- **Sequence Diagram**: [Xem chi tiết tại đây](https://github.com/Harihuynh2007/NHAPMONCNPM/blob/main/uml/readme.md#2-sequence-diagram)
- **ERD (Entity Relationship Diagram)**: ![ERD](./docs/erd.png)  

---

## 💻 Công nghệ sử dụng
- **Frontend**: ReactJS / Next.js + Tailwind CSS  
- **Backend**: Django  
- **CSDL**: MongoDB / PostgreSQL  
- **Authentication**: JWT + Google OAuth  
- **Quản lý phiên bản**: Git + GitHub  
- **Mô hình phát triển**: Agile – Scrum  

---

## 🚀 Cài đặt & chạy thử
-Clone repo:
```bash
git clone https://github.com/vancv43/tasknest.git
cd tasknest
```
-Chạy Server
```bash
npm run dev
# hoặc: npm start
```
-Kết quả dự kiến
```bash
Server chạy tại http://localhost:3000
Trang trả về: Hello World
```
## 📊 Kết quả dự kiến
- **Báo cáo**: Quá trình phát triển, phân tích yêu cầu, thiết kế hệ thống (CSDL, API, UI), đánh giá sản phẩm.  
- **Slide thuyết trình**: Mục tiêu, quy trình, demo sản phẩm, kết quả đạt được.  
- **Source code**: Mã nguồn đầy đủ của hệ thống.  
