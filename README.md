# Django Blog Website (Modern UI + Custom Admin Panel)

A simple, clean, and modern blog website built with **Django** and **SQLite**, featuring a beautifully designed public homepage and a customized Django admin panel for managing blog content efficiently.

This project is ideal for learning Django fundamentals while applying modern UI/UX principles to both frontend and admin interfaces.

---

## ✨ Features

### Public Website
- Modern, responsive homepage
- Clean blog post detail page
- Card-based blog layout
- Mobile-first design
- SEO-friendly slug-based URLs
---

### Admin Panel
- Fully functional Django admin
- Custom admin UI styling
- Enhanced usability (search, filters, previews)
- Slug auto-generation
- Secure authentication
---

### Backend
- Django framework
- SQLite database
- Clean app structure
- Maintainable and scalable codebase

---

## 🧱 Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS (Flexbox/Grid), JavaScript
- **Admin:** Customized Django Admin
- **Python Version:** 3.10+

---

## 📁 Project Structure

blogsite/

├── manage.py

├── blogsite/

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

├── blog/

│ ├── models.py

│ ├── views.py

│ ├── urls.py

│ └── admin.py

├── templates/

│ ├── base.html

│ ├── home.html

│ ├── post_detail.html

│ └── admin/

│ └── base_site.html

├── static/

│ ├── css/style.css

│ └── js/main.js

└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone or Open the Project
```bash
git clone <your-repo-url>
cd blogsite
Or open the folder directly in VS Code.
```

### 2. Create a Virtual Environment (Recommended)
```python -m venv venv```

#### Activate it:

Windows:

```venv\Scripts\activate```


macOS / Linux:

```source venv/bin/activate ```

### 3. Install Dependencies
``` pip install django```

### 4. Run Database Migrations
``` python manage.py makemigrations python manage.py migrate```

### 5. Create a Superuser (Admin Account)
```python manage.py createsuperuser```


Follow the prompts to set your admin credentials.

### 6. Start the Development Server
```python manage.py runserver```

---
### 🌐 Access the Application

Homepage:
http://127.0.0.1:8000/

Admin Panel:
http://127.0.0.1:8000/admin/

---

### 📝 Managing Blog Posts

- Log in to the admin panel

- Create a new blog post

- Set Published = True

- Save the post

The post will appear on the homepage automatically

---

### 🎨 Custom Admin Design

The admin panel UI has been customized using template overrides and custom CSS to provide:

- Improved spacing and layout

 - Modern fonts and colors

- Card-style sections

- Better visual hierarchy

Admin functionality remains fully compatible with Django’s default behavior.

---

### 🛡️ Security Notes

Do not use DEBUG=True in production

Set a strong SECRET_KEY

Configure allowed hosts properly before deployment

---

### 📄 License

This project is open-source and free to use for learning, personal projects, and experimentation.

---
### 👤 Author
### Richard Akintunde

Built with Django and modern UI principles.
Happy coding! 🚀