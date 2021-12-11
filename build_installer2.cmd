echo off
cls
pip3 install nuitka
pip install pynput
pip install zstandard
rem py -m nuitka --mingw64 .\pda.py --standalone --onefile 
py -m nuitka --mingw64 .\pda.py --standalone 
pause