from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime
import requests
import json

app = Flask(__name__, 
            template_folder='../frontend/html',
            static_folder='../frontend')
CORS(app)

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'webmaster_db'),
    'user': os.getenv('DB_USER', 'webmaster_user'),
    'password': os.getenv('DB_PASSWORD', 'webmaster_password'),
    'port': os.getenv('DB_PORT', '5432')
}

# Telegram Bot configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

def get_db_connection():
    """Get database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def init_database():
    """Initialize database tables"""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create form_submissions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS form_submissions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                form_type VARCHAR(50) NOT NULL,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"Database initialization error: {e}")
        return False

def send_telegram_message(message):
    """Send message to Telegram bot"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram configuration missing")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(url, data=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram send error: {e}")
        return False

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/admin')
def admin():
    """Serve the admin page"""
    return render_template('admin.html')

@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    """Handle form submission"""
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        form_type = data.get('form_type', 'price_calculator')
        message = data.get('message', '')
        
        if not all([name, email, phone]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Save to database
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor()
        
        # Insert user
        cursor.execute("""
            INSERT INTO users (name, email, phone) 
            VALUES (%s, %s, %s) 
            RETURNING id
        """, (name, email, phone))
        
        user_id = cursor.fetchone()[0]
        
        # Insert form submission
        cursor.execute("""
            INSERT INTO form_submissions (user_id, form_type, message) 
            VALUES (%s, %s, %s)
        """, (user_id, form_type, message))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        # Send to Telegram
        telegram_message = f"""
        <b>New Form Submission - {form_type.title()}</b>
        
        <b>Name:</b> {name}
        <b>Email:</b> {email}
        <b>Phone:</b> {phone}
        <b>Message:</b> {message if message else 'No additional message'}
        <b>Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        send_telegram_message(telegram_message)
        
        return jsonify({'success': True, 'message': 'Form submitted successfully'})
        
    except Exception as e:
        print(f"Form submission error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users (for admin purposes)"""
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT u.*, fs.form_type, fs.message, fs.created_at as submission_time
            FROM users u
            LEFT JOIN form_submissions fs ON u.id = fs.user_id
            ORDER BY u.created_at DESC
        """)
        
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return jsonify({'users': users})
        
    except Exception as e:
        print(f"Get users error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    # Initialize database
    if init_database():
        print("Database initialized successfully")
    else:
        print("Database initialization failed")
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)
