#!/usr/bin/env python3
"""
Setup script for Webmaster website
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True

def install_dependencies():
    """Install Python dependencies"""
    return run_command("pip install -r requirements.txt", "Installing Python dependencies")

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    env_content = """# Database Configuration
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
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ Created .env file with default configuration")
        print("⚠️  Please update the Telegram bot configuration in .env file")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Webmaster website...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Setup failed at .env file creation")
        sys.exit(1)
    
    print("=" * 50)
    print("✅ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Update the .env file with your Telegram bot configuration")
    print("2. Set up PostgreSQL database (or use Docker Compose)")
    print("3. Run: python app.py")
    print("4. Visit: http://localhost:5000")
    print("\nFor Docker setup, run: docker-compose up --build")

if __name__ == "__main__":
    main()
