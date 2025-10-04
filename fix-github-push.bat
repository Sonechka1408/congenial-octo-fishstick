@echo off
echo 🔐 GitHub Push Issue Resolver
echo =============================
echo.

echo Current situation:
echo - You're authenticated as: Sonechka1408
echo - Trying to push to: goiddochka1408/congenial-octo-fishstick
echo - This causes a permission error
echo.

echo Choose your solution:
echo 1) Create your own repository (Recommended)
echo 2) Try to push to existing repository with proper auth
echo 3) Fork the existing repository
echo.

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo ✅ Creating your own repository...
    echo.
    echo Steps:
    echo 1. Go to https://github.com/new
    echo 2. Repository name: webmaster (or congenial-octo-fishstick)
    echo 3. Description: Webmaster - Website Development Service Platform
    echo 4. Choose Public or Private
    echo 5. DON'T initialize with README
    echo 6. Click "Create repository"
    echo.
    echo After creating, run these commands:
    echo git remote add origin https://github.com/Sonechka1408/YOUR_REPO_NAME.git
    echo git push -u origin main
    echo.
) else if "%choice%"=="2" (
    echo.
    echo 🔑 Trying to push to existing repository...
    echo.
    echo This requires you to have write access to goiddochka1408/congenial-octo-fishstick
    echo.
    git remote add origin https://github.com/goiddochka1408/congenial-octo-fishstick.git
    git push -u origin main
    echo.
) else if "%choice%"=="3" (
    echo.
    echo 🍴 Forking the repository...
    echo.
    echo Steps:
    echo 1. Go to https://github.com/goiddochka1408/congenial-octo-fishstick
    echo 2. Click "Fork" button
    echo 3. This creates a copy under your account
    echo 4. Then push to your forked repository
    echo.
    echo After forking, run:
    echo git remote add origin https://github.com/Sonechka1408/congenial-octo-fishstick.git
    echo git push -u origin main
    echo.
) else (
    echo ❌ Invalid choice
    pause
    exit /b 1
)

echo.
echo 🎯 Recommended: Option 1 (Create your own repository)
echo This gives you full control and avoids permission issues.
echo.

pause
