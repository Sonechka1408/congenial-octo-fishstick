@echo off
echo 🚀 Webmaster GitHub Push Helper
echo ================================
echo.

echo Step 1: Create a new repository on GitHub.com
echo - Go to https://github.com/new
echo - Repository name: webmaster (or your preferred name)
echo - Description: Webmaster - Website Development Service Platform
echo - Choose Public or Private
echo - DON'T initialize with README, .gitignore, or license
echo - Click "Create repository"
echo.

echo Step 2: Copy your repository URL from GitHub
echo - It will look like: https://github.com/yourusername/webmaster.git
echo.

set /p repo_url="Enter your GitHub repository URL: "

if "%repo_url%"=="" (
    echo ❌ Please enter a valid repository URL
    pause
    exit /b 1
)

echo.
echo 📦 Adding remote origin...
git remote add origin %repo_url%

echo.
echo 🚀 Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ✅ Success! Your project has been pushed to GitHub
echo 🌐 You can now view it at: %repo_url%
echo.
echo 🎉 Next steps:
echo 1. Go to your repository on GitHub
echo 2. Verify all files are uploaded
echo 3. You can now deploy using Railway, Render, or other platforms
echo 4. See DEPLOYMENT.md for deployment instructions
echo.

pause
