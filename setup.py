import sys
import os
from cx_Freeze import setup, Executable


# ADD FILES
files = ['books.ico','themes/','modules/','shedule.sqlite']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="books.ico",
    target_name = "Shedule"
)

# SETUP CX FREEZE
setup(
    name = "Расписание КемГУ",
    version = "1.6",
    description = "Приложение для просмотра учебного рассписания",
    author = "Egorov Andrey",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
