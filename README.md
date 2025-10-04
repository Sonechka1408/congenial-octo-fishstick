# Webmaster - Website Development Service

A modern, full-stack website development service platform with organized project structure.

## 📁 Project Structure

```
congenial-octo-fishstick/
├── frontend/                    # Frontend files
│   ├── html/                   # HTML templates
│   │   ├── index.html          # Main homepage
│   │   ├── about-us.html       # About us page
│   │   ├── cases.html          # Business cases
│   │   ├── contact.html        # Contact page
│   │   ├── marketing.html      # Marketing services
│   │   ├── personal-design.html # Design services
│   │   ├── strategy.html       # Strategy services
│   │   └── admin.html          # Admin dashboard
│   ├── css/                    # Stylesheets
│   │   └── styles.css          # Main stylesheet
│   ├── js/                     # JavaScript files
│   │   └── main.js             # Main JavaScript functionality
│   └── images/                 # Image assets
│       └── (image files)
├── backend/                    # Backend files
│   ├── api/                    # API modules
│   ├── config/                 # Configuration files
│   │   └── config.py           # App configuration
│   ├── utils/                  # Utility functions
│   ├── app.py                  # Main Flask application
│   ├── run.py                  # Development server runner
│   ├── setup.py                # Setup script
│   ├── test_api.py             # API testing script
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Docker configuration
├── database/                   # Database files
│   ├── migrations/             # Database migrations
│   │   └── 001_initial_schema.sql
│   ├── scripts/                # Database scripts
│   │   ├── init.sql            # Database initialization
│   │   └── backup.sql          # Backup script
│   └── database.conf           # Database configuration
├── docs/                       # Documentation
│   └── README.md               # Detailed documentation
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Clone and navigate to project
cd congenial-octo-fishstick

# Start with Docker Compose
docker-compose up --build
```

### Option 2: Manual Setup
```bash
# Navigate to backend directory
cd congenial-octo-fishstick/backend

# Install dependencies
pip install -r requirements.txt

# Run setup script
python setup.py

# Start development server
python run.py
```

## 🌐 Access Points

- **Main Website**: http://localhost:5000
- **Admin Dashboard**: http://localhost:5000/admin
- **API Health Check**: http://localhost:5000/health

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the `backend/` directory:

```env
# Database Configuration
DB_HOST=localhost
DB_NAME=webmaster_db
DB_USER=webmaster_user
DB_PASSWORD=webmaster_password
DB_PORT=5432

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Database Setup
```bash
# Using Docker Compose (automatic)
docker-compose up db

# Manual PostgreSQL setup
psql -U postgres
CREATE DATABASE webmaster_db;
CREATE USER webmaster_user WITH PASSWORD 'webmaster_password';
GRANT ALL PRIVILEGES ON DATABASE webmaster_db TO webmaster_user;
```

## 📋 Features

### Frontend
- ✅ Modern responsive design with Tailwind CSS
- ✅ Interactive projects carousel
- ✅ Contact form with validation
- ✅ Dropdown navigation menus
- ✅ Smooth scrolling
- ✅ Mobile-friendly interface

### Backend
- ✅ Flask REST API
- ✅ PostgreSQL database integration
- ✅ Form submission handling
- ✅ Telegram bot notifications
- ✅ Admin dashboard
- ✅ Health check endpoints

### Database
- ✅ User management
- ✅ Form submission tracking
- ✅ Database migrations
- ✅ Backup scripts
- ✅ Performance indexes

## 🛠️ Development

### Running Tests
```bash
cd backend
python test_api.py
```

### Database Migrations
```bash
# Apply migrations
psql -U webmaster_user -d webmaster_db -f ../database/migrations/001_initial_schema.sql
```

### Backup Database
```bash
# Create backup
pg_dump -U webmaster_user -d webmaster_db > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore backup
psql -U webmaster_user -d webmaster_db < backup_file.sql
```

## 📚 API Documentation

### Endpoints

#### POST /api/submit-form
Submit contact form data.

**Request:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "form_type": "price_calculator",
  "message": "Optional message"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Form submitted successfully"
}
```

#### GET /api/users
Get all users and submissions (admin).

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "+1234567890",
      "created_at": "2024-01-01T10:00:00",
      "form_type": "price_calculator",
      "message": "Optional message",
      "submission_time": "2024-01-01T10:00:00"
    }
  ]
}
```

#### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T10:00:00"
}
```

## 🐳 Docker

### Build and Run
```bash
# Build image
docker build -t webmaster-app ./backend

# Run container
docker run -p 5000:5000 --env-file .env webmaster-app
```

### Docker Compose
```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support, please contact us through the contact form on the website or create an issue in the repository.