from pynput.keyboard import Key, KeyCode

buttons: dict[str, str | KeyCode] = {
    '0': '0',
    '1': '1', 
    '2': '2', 
    '3': '3', 
    '4': '4', 
    '5': '5', 
    '6': '6', 
    '7': '7', 
    '8': '8', 
    '9': '9',
    'space': Key.space,
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    'backspace': Key.backspace,
    'enter': Key.enter,
    'shift': Key.shift,
    'ctrl': Key.ctrl,
    'tab': Key.tab,
    'capslock': Key.caps_lock,
    'alt': Key.alt,
    'left': Key.left,
    'right': Key.right,
    'up': Key.up,
    'down': Key.down,
    'altgr': Key.alt_gr,
    '\\': '\\',
    ';': ';',
    '\'': '\'',
    '-': '-',
    '=': '=',
    '`': '`',
    '[': '[',
    ']': ']',
    '~': '~',
    ',': ',',
    '.': '.',
    '/': '/'
}

