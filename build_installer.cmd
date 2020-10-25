echo off
cls
pyinstaller --onefile -w sam.py
copy dist\* .
pause