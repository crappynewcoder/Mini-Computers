@echo off
title MiniOS V1.7 - Batch Operating System
color 1F

:: Set working directory
set "minios_dir=%~dp0"
cd /d "%minios_dir%"

:: Ensure folders exist
if not exist "cache" mkdir cache
if not exist "cache\scripts" mkdir cache\scripts

:main
cls
echo    __
echo ^<^(o ^^)^>___
echo  ^(  ._^^^>  /
echo   `----'
echo ============================
echo        MiniOS V1.7
echo ============================
echo.
echo 1. Folder Navigator
echo 2. Calculator
echo 3. Notepad (Cache System)
echo 4. System Info
echo 5. Tree Viewer
echo 6. Settings
echo 7. Exit
echo.
set /p choice=Enter your choice: 

if "%choice%"=="1" goto explorer
if "%choice%"=="2" goto calculator
if "%choice%"=="3" goto notepad_menu
if "%choice%"=="4" goto sysinfo
if "%choice%"=="5" goto tree_viewer
if "%choice%"=="6" goto settings
if "%choice%"=="7" exit
goto main

:explorer
cls
set "currentdir=%cd%"
echo --- Folder Navigator ---
echo Current directory: %cd%
echo.
echo [1] List contents
echo [2] Change directory
echo [3] Open file
echo [4] Go to root of drive
echo [5] Return to Main Menu
echo.
set /p fchoice=Choose an option: 

if "%fchoice%"=="1" goto list_contents
if "%fchoice%"=="2" goto change_dir
if "%fchoice%"=="3" goto open_file
if "%fchoice%"=="4" pushd %~d0 & goto explorer
if "%fchoice%"=="5" goto main
goto explorer

:list_contents
cls
echo --- Directory Listing ---
dir /b
pause
goto explorer

:change_dir
cls
echo --- Change Directory ---
set /p newdir=Enter folder name (.. to go up): 
cd "%newdir%" 2>nul
if errorlevel 1 (
    echo Failed to change directory.
    pause
)
goto explorer

:open_file
cls
echo --- Open File ---
set /p filename=Enter file name (no extension needed): 
for %%f in ("%filename%.*") do (
    start "" "%%~ff"
    goto explorer
)
echo File not found.
pause
goto explorer

:calculator
cls
echo --- Calculator ---
set /p exp=Enter expression (e.g., 3+4): 
set /a result=%exp%
echo Result: %result%
pause
goto main

:notepad_menu
cls
echo --- Notepad Cache System ---
echo.
echo 1. Create/Edit a file
echo 2. List files
echo 3. View a file
echo 4. Return to main menu
echo.
set /p npchoice=Choose an option: 

if "%npchoice%"=="1" goto np_create
if "%npchoice%"=="2" goto np_list
if "%npchoice%"=="3" goto np_view
if "%npchoice%"=="4" goto main
goto notepad_menu

:np_create
cls
echo --- Create/Edit File ---
set /p filename=Enter filename (no extension): 
notepad cache\%filename%.txt
goto notepad_menu

:np_list
cls
echo --- Files in Cache ---
dir /b cache\*.txt
pause
goto notepad_menu

:np_view
cls
echo --- View File Content ---
set /p vfilename=Enter filename to view (no extension): 
type cache\%vfilename%.txt
pause
goto notepad_menu

:sysinfo
cls
echo --- System Information ---
echo Username: %username%
echo Computer Name: %computername%
echo Date: %date%
echo Time: %time%
echo IP Config:
ipconfig | findstr /i "IPv4"
pause
goto main

:tree_viewer
cls
echo --- Tree Viewer ---
echo Generating directory tree... please wait.
tree /F /A > cache\tree_output.txt

echo.
echo Displaying directory tree (1 line every 1 second)...
echo Press Ctrl+C to stop early.
echo.

for /f "delims=" %%l in (cache\tree_output.txt) do (
    echo %%l
    timeout /t 1 >nul
)

pause
goto main

:settings
cls
echo --- Settings ---
echo.
echo 1. Change OS Color
echo 2. Return to Main Menu
echo.
set /p setchoice=Select a setting: 

if "%setchoice%"=="1" goto color_setting
if "%setchoice%"=="2" goto main
goto settings

:color_setting
cls
echo --- Change OS Color ---
echo.
echo 1. Yellow
echo 2. Green
echo 3. Red
echo 4. Back to Blue (Default)
echo.
set /p colorchoice=Choose a color: 

if "%colorchoice%"=="1" color 6F
if "%colorchoice%"=="2" color 2F
if "%colorchoice%"=="3" color 4F
if "%colorchoice%"=="4" color 1F
goto settings











