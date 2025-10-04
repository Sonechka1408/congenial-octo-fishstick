#!/bin/bash

# Webmaster Deployment Script
# This script helps you deploy to various platforms

echo "🚀 Webmaster Deployment Helper"
echo "================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Webmaster project"
    echo "✅ Git repository initialized"
    echo ""
    echo "⚠️  Please push to GitHub first:"
    echo "   git remote add origin https://github.com/yourusername/webmaster.git"
    echo "   git push -u origin main"
    echo ""
fi

echo "Choose your deployment platform:"
echo "1) Railway (Recommended - Easiest)"
echo "2) Render"
echo "3) Heroku"
echo "4) DigitalOcean App Platform"
echo "5) VPS (Manual setup)"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🚂 Deploying to Railway..."
        echo ""
        echo "Steps:"
        echo "1. Go to https://railway.app"
        echo "2. Sign up with GitHub"
        echo "3. Click 'New Project' → 'Deploy from GitHub repo'"
        echo "4. Select your webmaster repository"
        echo "5. Add PostgreSQL database"
        echo "6. Set environment variables (see DEPLOYMENT.md)"
        echo "7. Deploy!"
        echo ""
        echo "Your app will be live at: https://your-app-name.railway.app"
        ;;
    2)
        echo "🎨 Deploying to Render..."
        echo ""
        echo "Steps:"
        echo "1. Go to https://render.com"
        echo "2. Connect GitHub account"
        echo "3. Create 'New Web Service'"
        echo "4. Select your repository"
        echo "5. Configure build/start commands (see DEPLOYMENT.md)"
        echo "6. Add PostgreSQL database"
        echo "7. Deploy!"
        ;;
    3)
        echo "🟣 Deploying to Heroku..."
        echo ""
        echo "Prerequisites:"
        echo "- Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli"
        echo ""
        echo "Commands:"
        echo "heroku login"
        echo "heroku create your-app-name"
        echo "heroku addons:create heroku-postgresql:mini"
        echo "heroku config:set TELEGRAM_BOT_TOKEN=your_token"
        echo "heroku config:set TELEGRAM_CHAT_ID=your_chat_id"
        echo "git push heroku main"
        ;;
    4)
        echo "🌊 Deploying to DigitalOcean..."
        echo ""
        echo "Steps:"
        echo "1. Go to https://cloud.digitalocean.com"
        echo "2. Create new app"
        echo "3. Connect GitHub repository"
        echo "4. Configure build/run commands (see DEPLOYMENT.md)"
        echo "5. Add managed PostgreSQL database"
        echo "6. Deploy!"
        ;;
    5)
        echo "🖥️  VPS Deployment..."
        echo ""
        echo "This requires manual setup. See DEPLOYMENT.md for detailed instructions."
        echo ""
        echo "Recommended VPS providers:"
        echo "- DigitalOcean Droplets"
        echo "- Linode"
        echo "- Vultr"
        echo "- AWS EC2"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "📚 For detailed instructions, see DEPLOYMENT.md"
echo "🎉 Happy deploying!"
