@echo off
echo 🚀 Push to Your GitHub Repository
echo =================================
echo.

echo Step 1: Create a new repository on GitHub
echo - Go to: https://github.com/new
echo - Repository name: webmaster
echo - Description: Webmaster - Website Development Service Platform
echo - Choose Public or Private
echo - DON'T initialize with README
echo - Click "Create repository"
echo.

set /p repo_name="Enter your repository name (e.g., webmaster): "

if "%repo_name%"=="" (
    echo ❌ Please enter a repository name
    pause
    exit /b 1
)

echo.
echo 📦 Adding remote origin...
git remote add origin https://github.com/Sonechka1408/%repo_name%.git

echo.
echo 🚀 Pushing to GitHub...
git push -u origin main

echo.
if %errorlevel%==0 (
    echo ✅ Success! Your project has been pushed to GitHub
    echo 🌐 Repository URL: https://github.com/Sonechka1408/%repo_name%
    echo.
    echo 🎉 Next steps:
    echo 1. Go to your repository on GitHub
    echo 2. Verify all files are uploaded
    echo 3. You can now deploy using Railway, Render, or other platforms
    echo 4. See DEPLOYMENT.md for deployment instructions
) else (
    echo ❌ Push failed. Please check your repository name and try again.
    echo Make sure you created the repository on GitHub first.
)

echo.
pause
