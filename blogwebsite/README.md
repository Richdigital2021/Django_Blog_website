# Blog Website

A modern, responsive Django blog website with a customized admin panel and clean public interface.

## Features

- **Modern Public Interface**: Clean, responsive design with card-based layout
- **Custom Admin Panel**: Enhanced Django admin with modern UI/UX
- **Blog Management**: Full CRUD operations for blog posts
- **SEO-Friendly**: Slug-based URLs and semantic HTML
- **Mobile Responsive**: Works perfectly on all devices
- **SQLite Database**: Simple, file-based database

## Project Structure

```
blogsite/
├── manage.py
├── blogsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── tests.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── post_detail.html
│   └── admin/
│       └── base_site.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd blogwebsite
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install Django**:
   ```bash
   pip install django
   ```

5. **Install Pillow** (for image handling):
   ```bash
   pip install pillow
   ```

6. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser account** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin username and password.

8. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the application**:
   - **Public website**: http://127.0.0.1:8000/
   - **Admin panel**: http://127.0.0.1:8000/admin/

## Usage

### Managing Blog Posts

1. **Access the Admin Panel**:
   - Go to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

2. **Create Blog Posts**:
   - Click on "Blog posts" or "+ Add" next to Blog posts
   - Fill in the required fields:
     - **Title**: The post title
     - **Slug**: URL-friendly version (auto-generated from title)
     - **Content**: Full post content (supports line breaks)
     - **Featured Image**: Optional post image
     - **Author**: Select from available users
     - **Published**: Check to make post visible on public site

3. **View Posts**:
   - Published posts appear on the home page
   - Click "Read More" to view full post
   - Only published posts are visible to the public

### URL Structure

- `/` - Home page (lists all published posts)
- `/post/<slug>/` - Individual blog post page
- `/admin/` - Django admin panel

## Customization

### Styling

- **CSS**: Located in `static/css/style.css`
- **JavaScript**: Located in `static/js/main.js`
- **Templates**: Located in `templates/` directory

### Admin Panel Customization

The admin panel has been customized with:
- Modern gradient header
- Improved form styling
- Enhanced button designs
- Better spacing and typography
- Responsive design

### Blog Model Fields

The `BlogPost` model includes:
- `title`: CharField (max 200 characters)
- `slug`: SlugField (unique, auto-generated)
- `content`: TextField (supports rich text)
- `featured_image`: ImageField (optional)
- `author`: ForeignKey to User model
- `published`: BooleanField (controls visibility)
- `created_at`: DateTimeField (auto-set on creation)
- `updated_at`: DateTimeField (auto-updated on changes)

## Development

### Running Tests

```bash
python manage.py test
```

### Creating New Migrations

```bash
python manage.py makemigrations
```

### Collecting Static Files (for production)

```bash
python manage.py collectstatic
```

## Production Deployment

For production deployment, make sure to:

1. **Set `DEBUG = False`** in `settings.py`
2. **Configure `ALLOWED_HOSTS`** with your domain
3. **Set up a proper database** (PostgreSQL recommended)
4. **Configure static files serving**
5. **Set up environment variables** for sensitive data
6. **Use HTTPS** for secure connections

## Troubleshooting

### Common Issues

1. **Static files not loading**:
   - Run `python manage.py collectstatic`
   - Check `STATIC_URL` and `STATICFILES_DIRS` settings

2. **Images not uploading**:
   - Ensure Pillow is installed: `pip install pillow`
   - Check media file permissions

3. **Admin panel styling not applied**:
   - Verify admin template is in correct location
   - Check template inheritance

4. **Database errors**:
   - Delete `db.sqlite3` and re-run migrations
   - Ensure all migrations are applied

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please refer to the Django documentation or create an issue in the project repository.