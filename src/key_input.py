from pynput.keyboard import Controller
from buttons import buttons

keyboard = Controller()

caps_lock: bool = False
shift: bool = False
alt: bool = False
alt_gr: bool = False
ctrl: bool = False


def press_key(key: str):
    match key:
        case 'shift':
            if keyboard.shift_pressed:
                keyboard.release(keyboard._Key.shift)
            else:
                keyboard.press(keyboard._Key.shift)
        case 'alt':
            if keyboard.alt_pressed:
                keyboard.release(keyboard._Key.alt)
            else:
                keyboard.press(keyboard._Key.alt)
        case 'altgr':
            if keyboard.alt_gr_pressed:
                keyboard.release(keyboard._Key.alt_gr)
            else:
                keyboard.press(keyboard._Key.alt_gr)
        case 'ctrl':
            if keyboard.ctrl_pressed:
                keyboard.release(keyboard._Key.ctrl)
            else:
                keyboard.press(keyboard._Key.ctrl)
        case _:
            keyboard.press(buttons[key])
            keyboard.release(buttons[key])


def write(text: str):
    keyboard.type(text)
