import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "packages": ["pygame"], "packages": ["tinytag"], "packages": ["Pillow"],
                     "packages": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Vinyl Music Player",
      version="0.1",
      description="A Music Player for all your musical uses",
      options={"build_exe": build_exe_options},
      executables=[Executable("Vinyl.py", base=base)])
