import keyboard

caps_lock: bool = False
shift: bool = False
alt: bool = False
alt_gr: bool = False
ctrl: bool = False


def press_key(key: str):
    if key == 'shift':
        if keyboard.is_pressed('shift'):
            keyboard.release('shift')
        else:
            keyboard.press('shift')
    elif key == 'alt':
        if keyboard.is_pressed('alt'):
            keyboard.release('alt')
        else:
            keyboard.press('alt')
    elif key == 'ctrl':
        if keyboard.is_pressed('ctrl'):
            keyboard.release('ctrl')
        else:
            keyboard.press('ctrl')
    else:
        keyboard.press_and_release(key)

