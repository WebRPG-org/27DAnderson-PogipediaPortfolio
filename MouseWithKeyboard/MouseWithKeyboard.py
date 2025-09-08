import keyboard
import mouse
import ctypes
import time
import pyautogui
pyautogui.FAILSAFE = False
import os
import sys
import json

exit_shortcut = 'win+shift+escape'
scroll_lock_shortcut = 'ctrl+alt+insert'
cursor_up = 'up'
cursor_down = 'down'
cursor_left = 'left'
cursor_right = 'right'
cursor_fast_modifier = 'shift'
cursor_slow_modifier = 'ctrl'
left_click = 'enter'
right_click = 'backspace'
middle_click = 'delete'
scroll_up = 'page up'
scroll_down = 'page down'
normal_scroll_key = 'home'
fast_scroll_key = 'insert'
slow_scroll_key = 'end'
normal_scroll_speed = 0.175
fast_scroll_speed = 0.35
slow_scroll_speed = 0.0875
goto_middle_shortcut = 'win+alt+home'
goto_top_shortcut = 'win+alt+up'
goto_bottom_shortcut = 'win+alt+down'
goto_left_shortcut = 'win+alt+left'
goto_right_shortcut = 'win+alt+right'

if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(current_dir, 'mwk-config.json')):
    try:
        with open(os.path.join(current_dir, 'mwk-config.json'), 'r') as config_file:
            config = json.load(config_file)
        exit_shortcut = config.get('exit_shortcut', exit_shortcut)
        try:
            keyboard.parse_hotkey(exit_shortcut)
            if exit_shortcut == ' ':
                exit_shortcut = 'win+shift+escape'
        except ValueError:
            if not exit_shortcut == '':
                exit_shortcut = 'win+shift+escape'
        scroll_lock_shortcut = config.get('scroll_lock_shortcut', scroll_lock_shortcut)
        try:
            keyboard.parse_hotkey(scroll_lock_shortcut)
            if scroll_lock_shortcut == ' ':
                scroll_lock_shortcut = 'ctrl+alt+insert'
        except ValueError:
            if not scroll_lock_shortcut == '':
                scroll_lock_shortcut = 'ctrl+alt+insert'
        cursor_up = config.get('cursor_up', cursor_up)
        try:
            keyboard.parse_hotkey(cursor_up)
            if cursor_up == ' ':
                cursor_up = 'up'
        except ValueError:
            if not cursor_up == '':
                cursor_up = 'up'
        cursor_down = config.get('cursor_down', cursor_down)
        try:
            keyboard.parse_hotkey(cursor_down)
            if cursor_down == ' ':
                cursor_down = 'down'
        except ValueError:
            if not cursor_down == '':
                cursor_down = 'down'
        cursor_left = config.get('cursor_left', cursor_left)
        try:
            keyboard.parse_hotkey(cursor_left)
            if cursor_left == ' ':
                cursor_left = 'left'
        except ValueError:
            if not cursor_left == '':
                cursor_left = 'left'
        cursor_right = config.get('cursor_right', cursor_right)
        try:
            keyboard.parse_hotkey(cursor_right)
            if cursor_right == ' ':
                cursor_right = 'right'
        except ValueError:
            if not cursor_right == '':
                cursor_right = 'right'
        cursor_fast_modifier = config.get('cursor_fast_modifier', cursor_fast_modifier)
        try:
            keyboard.parse_hotkey(cursor_fast_modifier)
            if cursor_fast_modifier == ' ':
                cursor_fast_modifier = 'shift'
        except ValueError:
            if not cursor_fast_modifier == '':
                cursor_fast_modifier = 'shift'
        cursor_slow_modifier = config.get('cursor_slow_modifier', cursor_slow_modifier)
        try:
            keyboard.parse_hotkey(cursor_fast_modifier)
            if cursor_slow_modifier == ' ':
                cursor_slow_modifier = 'ctrl'
        except ValueError:
            if not cursor_slow_modifier == '':
                cursor_slow_modifier = 'ctrl'
        left_click = config.get('left_click', left_click)
        try:
            keyboard.parse_hotkey(left_click)
            if left_click == ' ':
                left_click = 'enter'
        except ValueError:
            if not left_click == '':
                left_click = 'enter'
        right_click = config.get('right_click', right_click)
        try:
            keyboard.parse_hotkey(right_click)
            if right_click == ' ':
                right_click = 'backspace'
        except ValueError:
            if not right_click == '':
                right_click = 'backspace'
        middle_click = config.get('middle_click', middle_click)
        try:
            keyboard.parse_hotkey(middle_click)
            if middle_click == ' ':
                middle_click = 'delete'
        except ValueError:
            if not middle_click == '':
                middle_click = 'delete'
        scroll_up = config.get('scroll_up', scroll_up)
        try:
            keyboard.parse_hotkey(scroll_up)
            if scroll_up == ' ':
                scroll_up = 'page up'
        except ValueError:
            if not scroll_up == '':
                scroll_up = 'page up'
        scroll_down = config.get('scroll_down', scroll_down)
        try:
            keyboard.parse_hotkey(scroll_down)
            if scroll_down == ' ':
                scroll_down = 'page down'
        except ValueError:
            if not scroll_down == '':
                scroll_down = 'page down'
        normal_scroll_key = config.get('normal_scroll_key', normal_scroll_key)
        try:
            keyboard.parse_hotkey(normal_scroll_key)
            if normal_scroll_key == ' ':
                normal_scroll_key = 'home'
        except ValueError:
            if not normal_scroll_key == '':
                normal_scroll_key = 'home'
        fast_scroll_key = config.get('fast_scroll_key', fast_scroll_key)
        try:
            keyboard.parse_hotkey(fast_scroll_key)
            if fast_scroll_key == ' ':
                fast_scroll_key = 'insert'
        except ValueError:
            if not fast_scroll_key == '':
                fast_scroll_key = 'insert'
        slow_scroll_key = config.get('slow_scroll_key', slow_scroll_key)
        try:
            keyboard.parse_hotkey(slow_scroll_key)
            if slow_scroll_key == ' ':
                slow_scroll_key = 'end'
        except ValueError:
            if not slow_scroll_key == '':
                slow_scroll_key = 'end'
        normal_scroll_speed = config.get('normal_scroll_speed', normal_scroll_speed)
        if not isinstance(normal_scroll_speed, (int, float)):
            normal_scroll_speed = 0.175
        fast_scroll_speed = config.get('fast_scroll_speed', fast_scroll_speed)
        if not isinstance(fast_scroll_speed, (int, float)):
            normal_scroll_speed = 0.35
        slow_scroll_speed = config.get('slow_scroll_speed', slow_scroll_speed)
        if not isinstance(slow_scroll_speed, (int, float)):
            normal_scroll_speed = 0.0875
        goto_middle_shortcut = config.get('goto_middle_shortcut', goto_middle_shortcut)
        try:
            keyboard.parse_hotkey(goto_middle_shortcut)
            if goto_middle_shortcut == ' ':
                goto_middle_shortcut = 'win+alt+home'
        except ValueError:
            if not goto_middle_shortcut == '':
                goto_middle_shortcut = 'win+alt+home'
        goto_top_shortcut = config.get('goto_top_shortcut', goto_top_shortcut)
        try:
            keyboard.parse_hotkey(goto_top_shortcut)
            if goto_top_shortcut == ' ':
                goto_top_shortcut = 'win+alt+up'
        except ValueError:
            if not goto_top_shortcut == '':
                goto_top_shortcut = 'win+alt+up'
        goto_bottom_shortcut = config.get('goto_bottom_shortcut', goto_bottom_shortcut)
        try:
            keyboard.parse_hotkey(goto_bottom_shortcut)
            if goto_bottom_shortcut == ' ':
                goto_bottom_shortcut = 'win+alt+down'
        except ValueError:
            if not goto_bottom_shortcut == '':
                goto_bottom_shortcut = 'win+alt+down'
        goto_left_shortcut = config.get('goto_left_shortcut', goto_left_shortcut)
        try:
            keyboard.parse_hotkey(goto_left_shortcut)
            if goto_left_shortcut == ' ':
                goto_left_shortcut = 'win+alt+left'
        except ValueError:
            if not goto_left_shortcut == '':
                goto_left_shortcut = 'win+alt+left'
        goto_right_shortcut = config.get('goto_right_shortcut', goto_right_shortcut)
        try:
            keyboard.parse_hotkey(goto_right_shortcut)
            if goto_right_shortcut == ' ':
                goto_right_shortcut = 'win+alt+right'
        except ValueError:
            if not goto_right_shortcut == '':
                goto_right_shortcut = 'win+alt+right'
    except json.JSONDecodeError:
        pass

blocked_keys = []
enter_held = False
backspace_held = False
tab_held = False
scroll_lock_shortcut_held = False
scroll_speed = normal_scroll_speed

def block_key(key):
    if key not in blocked_keys:
        keyboard.block_key(key)
        blocked_keys.append(key)
def unblock_key(key):
    if key in blocked_keys:
        keyboard.unblock_key(key)
        blocked_keys.remove(key)

while True:
    time.sleep(0.01)

    if exit_shortcut and keyboard.is_pressed(exit_shortcut):
        break

    if scroll_lock_shortcut and keyboard.is_pressed(scroll_lock_shortcut):
        if not scroll_lock_shortcut_held:
            pyautogui.press('scrolllock')
            scroll_lock_shortcut_held = True
    else:
        scroll_lock_shortcut_held = False  

    if ctypes.windll.user32.GetKeyState(0x91) & 1:
        try:
            if cursor_up not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(cursor_up):
                block_key(cursor_up)
        except ValueError:
            pass
        try:
            if cursor_down not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(cursor_down):
                block_key(cursor_down)
        except ValueError:
            pass
        try:
            if cursor_left not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(cursor_left):
                block_key(cursor_left)
        except ValueError:
            pass
        try:
            if cursor_right not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(cursor_right):
                block_key(cursor_right)
        except ValueError:
            pass
        try:
            if left_click not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(left_click):
                block_key(left_click)
        except ValueError:
            pass
        try:
            if right_click not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(right_click):
                block_key(right_click)
        except ValueError:
            pass
        try:
            if middle_click not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(middle_click):
                block_key(middle_click)
        except ValueError:
            pass
        try:
            if scroll_up not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(scroll_up):
                block_key(scroll_up)
        except ValueError:
            pass
        try:
            if scroll_down not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(scroll_down):
                block_key(scroll_down)
        except ValueError:
            pass
        try:
            if normal_scroll_key not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(normal_scroll_key):
                block_key(normal_scroll_key)
        except ValueError:
            pass
        try:
            if slow_scroll_key not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(slow_scroll_key):
                block_key(slow_scroll_key)
        except ValueError:
            pass
        try:
            if fast_scroll_key not in ['', ' ', 'ctrl', 'shift', 'alt', 'win'] and keyboard.key_to_scan_codes(fast_scroll_key):
                block_key(fast_scroll_key)
        except ValueError:
            pass
        
        dx = 0
        dy = 0

        if cursor_up and keyboard.is_pressed(cursor_up):
            if keyboard.is_pressed(cursor_fast_modifier) and keyboard.is_pressed(cursor_slow_modifier):
                dy -= 3.75
            elif keyboard.is_pressed(cursor_fast_modifier):
                dy -= 7.5
            elif keyboard.is_pressed(cursor_slow_modifier):
                dy -= 1.875
            else:
                dy -= 3.75
        if cursor_down and keyboard.is_pressed(cursor_down):
            if keyboard.is_pressed(cursor_fast_modifier) and keyboard.is_pressed(cursor_slow_modifier):
                dy += 3.75
            elif keyboard.is_pressed(cursor_fast_modifier):
                dy += 7.5
            elif keyboard.is_pressed(cursor_slow_modifier):
                dy += 1.875
            else:
                dy += 3.75
        if cursor_left and keyboard.is_pressed(cursor_left):
            if keyboard.is_pressed(cursor_fast_modifier) and keyboard.is_pressed(cursor_slow_modifier):
                dx -= 3.75
            elif keyboard.is_pressed(cursor_fast_modifier):
                dx -= 7.5
            elif keyboard.is_pressed(cursor_slow_modifier):
                dx -= 1.875
            else:
                dx -= 3.75
        if cursor_right and keyboard.is_pressed(cursor_right):
            if keyboard.is_pressed(cursor_fast_modifier) and keyboard.is_pressed(cursor_slow_modifier):
                dx += 3.75
            elif keyboard.is_pressed(cursor_fast_modifier):
                dx += 7.5
            elif keyboard.is_pressed(cursor_slow_modifier):
                dx += 1.875
            else:
                dx += 3.75    
        if dx != 0 or dy != 0:
            mouse.move(dx, dy, absolute=False, duration=0)

        if left_click and keyboard.is_pressed(left_click):
            if not enter_held:
                mouse.press(button='left')
                enter_held = True
        else:
            if enter_held:
                mouse.release(button='left')
                enter_held = False  
        if right_click and keyboard.is_pressed(right_click):
            if not backspace_held:
                mouse.press(button='right')
                backspace_held = True
        else:
            if backspace_held:
                mouse.release(button='right')
                backspace_held = False
        if middle_click and keyboard.is_pressed(middle_click):
            if not tab_held:
                mouse.press(button='middle')
                tab_held = True
        else:   
            if tab_held:
                mouse.release(button='middle')
                tab_held = False

        if normal_scroll_key and keyboard.is_pressed(normal_scroll_key):
            scroll_speed = normal_scroll_speed
        elif slow_scroll_key and keyboard.is_pressed(slow_scroll_key):
            scroll_speed = slow_scroll_speed
        elif fast_scroll_key and keyboard.is_pressed(fast_scroll_key):
            scroll_speed = fast_scroll_speed

        if scroll_up and keyboard.is_pressed(scroll_up):
            mouse.wheel(scroll_speed)
        if scroll_down and keyboard.is_pressed(scroll_down):
            mouse.wheel(-scroll_speed)

        if goto_middle_shortcut and keyboard.is_pressed(goto_middle_shortcut):
            width, height = pyautogui.size()
            mouse.move(width//2, height//2, absolute=True, duration=0)
        if goto_top_shortcut and keyboard.is_pressed(goto_top_shortcut):
            x, y = pyautogui.position()
            pyautogui.moveTo(x, y - 100000, duration=0)
        elif goto_top_shortcut and keyboard.is_pressed(goto_bottom_shortcut):
            x, y = pyautogui.position()
            pyautogui.moveTo(x, y + 100000, duration=0)
        elif goto_bottom_shortcut and keyboard.is_pressed(goto_left_shortcut):
            x, y = pyautogui.position()
            pyautogui.moveTo(x - 100000, y, duration=0)
        elif goto_right_shortcut and keyboard.is_pressed(goto_right_shortcut):
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 100000, y, duration=0)
        
    else:
        unblock_key(cursor_up)
        unblock_key(cursor_down)
        unblock_key(cursor_left)
        unblock_key(cursor_right)
        unblock_key(left_click)
        unblock_key(right_click)
        unblock_key(middle_click)
        unblock_key(scroll_up)
        unblock_key(scroll_down)
        unblock_key(normal_scroll_key)
        unblock_key(slow_scroll_key)
        unblock_key(fast_scroll_key)

unblock_key(cursor_up)
unblock_key(cursor_down)
unblock_key(cursor_left)
unblock_key(cursor_right)
unblock_key(left_click)
unblock_key(right_click)
unblock_key(middle_click)
unblock_key(scroll_up)
unblock_key(scroll_down)
unblock_key(normal_scroll_key)
unblock_key(slow_scroll_key)
unblock_key(fast_scroll_key)
mouse.release(button='left')
mouse.release(button='right')
mouse.release(button='middle')