# **📌 Multilingual FAQ API with Django**  

🚀 A **high-performance** and **multilingual** FAQ management system with **WYSIWYG editor**, **Redis caching**, and **REST API** support.

---

## **✨ Features**
✅ **Multilingual Support** – Fetch FAQs in **English, Hindi, Bengali, French** via `?lang=` query parameter.  
✅ **WYSIWYG Editor** – Rich-text formatting with **django-ckeditor**.  
✅ **Fast API Responses** – Optimized with **Redis caching**.  
✅ **Auto Translations** – Uses Google Translate API for automatic FAQ translations.  
✅ **Admin Panel** – Manage FAQs with a user-friendly Django admin interface.  
✅ **REST API Ready** – Fully functional API with **Django REST Framework (DRF)**.  

---

## **🛠 Installation & Setup**  

### **1️⃣ Clone & Install Dependencies**  
```bash
git clone https://github.com/Siddharth-Nama/Bharatfd_assignment
cd multilingual_faq
pip install -r requirements.txt
```

### **2️⃣ Apply Migrations & Create Superuser**  
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### **3️⃣ Run the Server**  
```bash
python manage.py runserver
```

---

## **🌍 API Usage**  

### 📌 **Fetch FAQs in English (default)**  
```bash
curl http://127.0.0.1:8000/api/faqs/
```

### 📌 **Fetch FAQs in Hindi**  
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### 📌 **Fetch FAQs in Bengali**  
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```
### 📌 **Fetch FAQs in French**  
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=fr
```

✅ **Example Response:**  
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "question_translated": "डिजैंगो क्या है?", 
        "answer": "<p>Django is a web framework...</p>"
    }
]
```

---

## **⚡ Caching with Redis**
This project uses **Redis** to cache translated FAQs for **faster API responses**.

### **Setup Redis**  
```bash
sudo apt update && sudo apt install redis-server
redis-server  # Start Redis
```

---

## **✅ Testing**
Run **unit tests**:
```bash
py manage.py test
```

---

## **📖 Contribution Guide**
- Fork the repository.  
- Create a feature branch: `git checkout -b feature-name`.  
- Commit changes with clear messages: `git commit -m "feat: Add caching support"`.  
- Push and create a **Pull Request (PR)**.

---

## **🚀 Deployment (Bonus)**
To deploy using **Docker**, use:
```bash
docker-compose up --build
```

---

## **🔗 Contact & Support**
For any queries, open an issue or tag `@Siddharth-Nama` or `@theakshaydhiman`.  

🚀 **Get started now and power up your multilingual FAQ system!** 🚀