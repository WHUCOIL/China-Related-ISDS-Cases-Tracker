@echo off
chcp 65001 >nul
echo ========================================
echo   启动本地Web服务器
echo ========================================
echo.
echo 正在启动服务器...
echo.

cd /d "%~dp0"
python start_server_simple.py

if errorlevel 1 (
    echo.
    echo ========================================
    echo   启动失败！
    echo ========================================
    echo.
    echo 可能的原因：
    echo 1. Python 未安装或未添加到PATH
    echo 2. 端口 8000 已被占用
    echo 3. 权限不足
    echo.
    echo 请查看上面的错误信息
    echo.
    pause
    exit /b 1
)
