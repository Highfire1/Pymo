import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only

# base="Win32GUI" should be used only for Windows GUI app
base = None

setup(
    name="Pymo",
    version="0.1",
    description="Pymo!!!",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["assets"]}},
    executables=[Executable("main.py", base=base)],
    
)