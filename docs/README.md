# Webmaster - Website Development Service

A modern website development service platform built with Flask, PostgreSQL, and Tailwind CSS.

## Features

- **Modern Frontend**: Built with HTML, CSS, JavaScript, and Tailwind CSS
- **Backend API**: Flask-based REST API with PostgreSQL database
- **Form Handling**: Contact forms with Telegram bot integration
- **Responsive Design**: Mobile-friendly interface
- **Database Storage**: PostgreSQL for user data and form submissions
- **Docker Support**: Easy deployment with Docker and Docker Compose

## Project Structure

```
congenial-octo-fishstick/
├── app.py                 # Flask backend application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── styles.css           # Custom CSS styles
├── index.html           # Main homepage
├── about-us.html        # About us page
├── cases.html           # Business cases page
├── contact.html         # Contact page
├── marketing.html       # Marketing services page
├── personal-design.html # Personal design services page
├── strategy.html        # Strategy services page
└── README.md           # This file
```

## Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd congenial-octo-fishstick
   ```

2. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_telegram_chat_id_here
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:5000
   - API: http://localhost:5000/api/

## Manual Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 12+
- pip

### Installation

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL database**
   ```sql
   CREATE DATABASE webmaster_db;
   CREATE USER webmaster_user WITH PASSWORD 'webmaster_password';
   GRANT ALL PRIVILEGES ON DATABASE webmaster_db TO webmaster_user;
   ```

3. **Set environment variables**
   ```bash
   export DB_HOST=localhost
   export DB_NAME=webmaster_db
   export DB_USER=webmaster_user
   export DB_PASSWORD=webmaster_password
   export DB_PORT=5432
   export TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   export TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## API Endpoints

### POST /api/submit-form
Submit a contact form with user information.

**Request Body:**
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

### GET /api/users
Get all users and their form submissions (admin endpoint).

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "+1234567890",
      "created_at": "2023-12-01T10:00:00",
      "form_type": "price_calculator",
      "message": "Optional message",
      "submission_time": "2023-12-01T10:00:00"
    }
  ]
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2023-12-01T10:00:00"
}
```

## Telegram Bot Integration

To enable Telegram notifications for form submissions:

1. Create a Telegram bot using [@BotFather](https://t.me/botfather)
2. Get your bot token
3. Get your chat ID (you can use [@userinfobot](https://t.me/userinfobot))
4. Set the environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your bot token
   - `TELEGRAM_CHAT_ID`: Your chat ID

## Database Schema

### Users Table
- `id`: Primary key
- `name`: User's full name
- `email`: User's email address
- `phone`: User's phone number
- `created_at`: Timestamp of user creation

### Form Submissions Table
- `id`: Primary key
- `user_id`: Foreign key to users table
- `form_type`: Type of form submitted
- `message`: Additional message (optional)
- `created_at`: Timestamp of submission

## Development

### Running in Development Mode

```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
python app.py
```

### Database Migrations

The application automatically creates the necessary database tables on startup. For production, consider using a proper migration tool like Alembic.

## Deployment

### Production Considerations

1. **Environment Variables**: Use proper environment variable management
2. **Database**: Use a managed PostgreSQL service
3. **Security**: Set strong passwords and use HTTPS
4. **Monitoring**: Add logging and monitoring
5. **Scaling**: Consider using a WSGI server like Gunicorn

### Docker Production Build

```bash
docker build -t webmaster-app .
docker run -p 5000:5000 --env-file .env webmaster-app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please contact us through the contact form on the website or create an issue in the repository.
