#!/usr/bin/env python3
"""
Development server runner for Webmaster website
"""

import os
import sys
from app import app, init_database

def main():
    """Run the development server"""
    print("🚀 Starting Webmaster development server...")
    
    # Initialize database
    if init_database():
        print("✅ Database initialized successfully")
    else:
        print("⚠️  Database initialization failed - continuing anyway")
    
    # Set development environment
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = 'True'
    
    print("🌐 Server starting at http://localhost:5000")
    print("📊 Admin panel available at http://localhost:5000/admin")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
