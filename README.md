# E-Commerce Flask Application

A simple e-commerce web application built with Flask, featuring user authentication, product management, and a shopping cart system.

## Features

- **User Authentication**: Register and login functionality
- **Product Management**: View all products and product details
- **Shopping Cart**: Add products to cart (session-based)
- **Admin Panel**: Add new products
- **Database**: SQLAlchemy ORM with SQLite database
- **Database Migrations**: Flask-Migrate for schema management
- **Docker Support**: Containerized for easy deployment

## Tech Stack

- **Framework**: Flask 2.3.3
- **Database**: SQLAlchemy with SQLite
- **Authentication**: Flask-Login
- **Migrations**: Flask-Migrate
- **Web Server**: Gunicorn (for production)
- **Container**: Docker

## Prerequisites

- **Docker** (latest version)
- **Python** 3.9+ (for local development)
- **Git**

## Quick Start with Docker (Recommended)

### 1. Clone or Navigate to the Project
```bash
cd ecommerce-flask
```

### 2. Build the Docker Image
```bash
docker build -t ecommerce-flask:latest .
```

### 3. Run the Docker Container
```bash
docker run -p 5000:5000 --name ecommerce-flask-container ecommerce-flask:latest
```

### 4. Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```

### 5. Stop the Container
Press `CTRL+C` in the terminal or run:
```bash
docker stop ecommerce-flask-container
```

### 6. Restart the Container
```bash
docker start ecommerce-flask-container
```

## Local Development Setup (Without Docker)

### 1. Create a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
```

### 5. Initialize the Database
```bash
python create_db.py
```

### 6. Run the Application
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
ecommerce-flask/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── models.py                # Database models (User, Product)
│   ├── routes.py                # Application routes
│   ├── create_db.py             # Database initialization
│   ├── __pycache__/             # Python cache
│   └── templates/               # HTML templates
│       ├── base.html            # Base template
│       ├── index.html           # Home page
│       ├── product.html         # Product detail page
│       ├── cart.html            # Shopping cart page
│       ├── login.html           # Login page
│       ├── register.html        # Registration page
│       └── new_product.html     # Add product page (admin)
├── instance/                    # Instance-specific files
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── create_db.py                 # Database setup script
└── README.md                    # This file
```

## Available Routes

### Public Routes
- `GET /` - Home page with all products
- `GET /product/<id>` - Product details
- `GET /register` - Registration page
- `POST /register` - Register a new user
- `GET /login` - Login page
- `POST /login` - Login user
- `GET /cart` - View shopping cart
- `GET /cart/add/<id>` - Add product to cart

### Authenticated Routes
- `GET /logout` - Logout user

### Admin Routes
- `GET /admin/product/new` - Add product form
- `POST /admin/product/new` - Create a new product

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `dev-secret` | Flask secret key for sessions |
| `DATABASE_URL` | `sqlite:///app.db` | Database connection string |
| `FLASK_ENV` | `development` | Flask environment |

## Dependencies

All dependencies are listed in `requirements.txt`:
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.3
- Flask-Migrate 4.0.4
- Flask-Login 0.6.3
- Werkzeug 2.3.7
- python-dotenv 1.0.0
- gunicorn 20.1.0

## Common Docker Commands

### View Running Containers
```bash
docker ps
```

### View All Containers
```bash
docker ps -a
```

### View Container Logs
```bash
docker logs ecommerce-flask-container
```

### Remove a Container
```bash
docker rm ecommerce-flask-container
```

### Remove Docker Image
```bash
docker rmi ecommerce-flask:latest
```

## Troubleshooting

### Port 5000 Already in Use
If port 5000 is already in use, you can map to a different port:
```bash
docker run -p 8000:5000 --name ecommerce-flask-container ecommerce-flask:latest
```
Then access the app at `http://localhost:8000`

### Container Won't Start
Check the logs:
```bash
docker logs ecommerce-flask-container
```

### Database Issues
Reinitialize the database:
```bash
python create_db.py
```

## Production Deployment

For production, consider:
1. Using **Gunicorn** instead of Flask development server
2. Setting `DEBUG=False`
3. Using a production database (PostgreSQL recommended)
4. Implementing HTTPS/SSL
5. Using environment-specific configuration

### Production Docker Command
```bash
docker run -p 80:5000 -e FLASK_ENV=production --name ecommerce-flask-prod ecommerce-flask:latest
```

## Development Tips

- **Debug Mode**: Currently enabled in development. Disable in production.
- **Database Migrations**: Use Flask-Migrate for schema changes:
  ```bash
  flask db migrate -m "Description"
  flask db upgrade
  ```
- **Session Management**: Shopping cart is stored in Flask sessions (server-side)

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please check the logs and ensure all dependencies are properly installed.

---

**Last Updated**: November 12, 2025
