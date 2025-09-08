# Mouse With Keyboard Project

## This is a project I made that allows you to use a Windows computer without a mouse. Because, what if you don't have a mouse, lost your mouse, or your mouse battery dies? A Windows computer is really difficult to use without a keyboard. And this solves that!

### Using the program

You can run this program in two different ways:

1. `MouseWithKeyboard.exe`  
    Nothing else is required. You can just download and run the file.

2. `MouseWithKeyboard.py`  
    Requires these to be installed in order to run:
    - Python 3.12.10 or later
    - `keyboard` library
    - `mouse` library
    - `pyautogui` library

Python can be installed from [python.org](https://python.org)

The libraries can be installed by running this in the command line: 
```
pip install keyboard mouse pyautogui
```

### Files included in the repository  
* `MouseWithKeyboard.exe` - Full program in an executable file. Nothing outside of this file is required to run the program.  
* `MouseWithKeyboard.py` - Full program in a python file. In order to run this file you need to have python installed, it was written in 3.12.10, so ideally that version or later.  
* `mwk-config.json` - Configuration file. Works with both the executable file and the python file. It allows you to customize the settings of the program. It must be named exactly `mwk-config.json` and be in the same folder as the executable/python file to work. All values contained in the file in this repository are the default values used in the executable/python file, and will not change the functionality unless you change any of the values. You can also leave a value blank (as in "") in order to disable that functionality.  
* `MWK Final Icon.png` - Portable Network Graphics file of the icon I made to use for the executable file.  
* `MWK Final Icon.ico` - Icon file of the icon I made to use for the executable file. I had to convert the PNG file to this format in order to use it as the icon for executable file.  
* `LICENSE` - Just the license
* `README.md` - The file you are reading right now!

### Default keybinds
**Arrow Keys**: Move the mouse  
**Shift+Arrow Keys**: Move the mouse faster  
**Ctrl+Arrow Keys**: Move the mouse slower

**Enter**: Left click  
**Backspace**: Right click  
**Delete**: Middle click

**Page Up**: Scroll up  
**Page Down**: Scroll down  
**Home**: Normal scroll speed  
**End**: Slow scroll speed  
**Insert**: Fast scroll speed

**Win+Alt+Home**: Go to middle of the main screen  
**Win+Arrow Keys**: Go to edge of screen in that direction

**Ctrl+Alt+Insert**: Toggle Scroll Lock  
**Win+Shift+Escape**: Exit the program
