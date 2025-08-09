# 📚 Django Books Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern and comprehensive Django web application for managing and displaying different types of books with a clean, responsive interface.

## 🌟 Features

### 📖 Book Management
- **8 Book Categories**: Fiction, Non-Fiction, Mystery, Science, Biography, Romance, Fantasy, History
- **Book Display**: Beautiful grid layout with Bootstrap styling
- **Image Support**: Upload and display book cover images
- **Admin Interface**: Full Django admin panel for managing books

### 🎨 User Interface
- **Modern Design**: Clean and responsive Bootstrap-based UI
- **Navigation**: Easy navigation between pages
- **Mobile Friendly**: Responsive design that works on all devices

### 🏠 Pages
- **Home Page**: Welcome landing page with personalized greeting
- **About Page**: Information about the project
- **Contact Page**: Contact information
- **Books Page**: Display all books with categorization

## 🏗️ Project Structure

```
djangoproject/
├── djangoproject/          # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings configuration
│   ├── urls.py            # Main URL routing
│   ├── views.py           # Main project views
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── books/                  # Books app
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Database models
│   ├── views.py           # Books app views
│   ├── urls.py            # Books app URLs
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   │   └── books/
│   │       └── all_books.html
│   └── static/            # Static files (CSS, JS, images)
│       └── style.css
├── templates/             # Main project templates
│   └── index.html         # Home page template
├── static/                # Main project static files
│   └── style.css          # Main CSS styles
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
└── README.md             # Project documentation
```

## 🗄️ Database Models

### Booksvariety Model
```python
class Booksvariety(models.Model):
    BOOKS_TYPE_CHOICE = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('MYS', 'Mystery'),
        ('SCI', 'Science'),
        ('BIO', 'Biography'),
        ('ROM', 'Romance'),
        ('FANT', 'Fantasy'),
        ('HIS', 'History'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices=BOOKS_TYPE_CHOICE)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/django-books-management.git
   cd django-books-management
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   
   # Linux/Mac
   python3 -m venv venv
   ```

3. **Activate Virtual Environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - **Main Page**: http://127.0.0.1:8000/
   - **Books Page**: http://127.0.0.1:8000/books/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 URL Structure

### Main Project URLs
- `/` - Home page
- `/about/` - About page
- `/contact/` - Contact page
- `/admin/` - Admin interface

### Books App URLs
- `/books/` - All books display page

## 🎯 Usage

### Adding Books
1. Access the admin panel at http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Navigate to "Booksvarieties" section
4. Click "Add Booksvariety"
5. Fill in the book details (name, image, type)
6. Save the book

### Viewing Books
1. Visit http://127.0.0.1:8000/books/
2. All books will be displayed in a grid layout
3. Books are categorized by type (Fiction, Non-Fiction, etc.)

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The project uses SQLite by default. For production, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Django not found**
   ```bash
   # Make sure virtual environment is activated
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   
   # Install requirements
   pip install -r requirements.txt
   ```

2. **Migration errors**
   ```bash
   # Remove old migrations and recreate
   python manage.py makemigrations --empty books
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static files not loading**
   ```bash
   # Collect static files
   python manage.py collectstatic
   ```

4. **Port already in use**
   ```bash
   # Use different port
   python manage.py runserver 8001
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments to your code
- Write tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ninad Gawade**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap for UI components
- Python community for excellent packages

## 📞 Support

If you have any questions or need help:
- Open an [issue](https://github.com/yourusername/django-books-management/issues)
- Contact: your.email@example.com

---

⭐ **Star this repository if you found it helpful!** 