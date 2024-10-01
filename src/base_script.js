const SERVERLOC = 'http://<enter your server address here>';



function sendTextInput() {
    const input = document.getElementById('inputField').value;
    
    fetch(SERVERLOC + '/text_input', {
        method: 'POST',
        body: input,
        headers: {
            'Content-Type': 'text/plain'
        }
    }).then(response => {
        console.log("Input sent:", input);
    }).catch(err => {
        console.error("Error:", err);
    });
}

const Buttons = {
    BUTTON_0: '0',
    BUTTON_1: '1', 
    BUTTON_2: '2', 
    BUTTON_3: '3', 
    BUTTON_4: '4', 
    BUTTON_5: '5', 
    BUTTON_6: '6', 
    BUTTON_7: '7', 
    BUTTON_8: '8', 
    BUTTON_9: '9',
    BUTTON_SPACE: 'space',
    BUTTON_A: 'a',
    BUTTON_B: 'b',
    BUTTON_C: 'c',
    BUTTON_D: 'd',
    BUTTON_E: 'e',
    BUTTON_F: 'f',
    BUTTON_G: 'g',
    BUTTON_H: 'h',
    BUTTON_I: 'i',
    BUTTON_J: 'j',
    BUTTON_K: 'k',
    BUTTON_L: 'l',
    BUTTON_M: 'm',
    BUTTON_N: 'n',
    BUTTON_O: 'o',
    BUTTON_P: 'p',
    BUTTON_Q: 'q',
    BUTTON_R: 'r',
    BUTTON_S: 's',
    BUTTON_T: 't',
    BUTTON_U: 'u',
    BUTTON_V: 'v',
    BUTTON_W: 'w',
    BUTTON_X: 'x',
    BUTTON_Y: 'y',
    BUTTON_Z: 'z',
    BUTTON_BACKSPACE: 'backspace',
    BUTTON_ENTER: 'enter',
    BUTTON_SHIFT: 'shift',
    BUTTON_CTRL: 'ctrl',
    BUTTON_TAB: 'tab',
    BUTTON_CAPSLOCK: 'capslock',
    BUTTON_ALT: 'alt',
    BUTTON_FN: '',                        // not implemented...
    BUTTON_LEFT: 'left',
    BUTTON_RIGHT: 'right',
    BUTTON_UP: 'up',
    BUTTON_DOWN: 'down',
    BUTTON_ALTGR: '',                       // not implemented ...
    BUTTON_BSLASH: '\\',
    BUTTON_SEMICOL: ';',
    BUTTON_QUOTATION: '\'',
    BUTTON__: '-',
    BUTTON_EQ: '=',
    BUTTON_Á: '`',
    BUTTON_BRACKET: '[',
    BUTTON_BACKBRA: ']',
    BUTTON_Â: '~',
    BUTTON_COLON: ',',
    BUTTON_DOT: '.',
    BUTTON_SLASH: '/',
    BUTTON_Ç: '',                           // not implemented ...
    BUTTON_VSLASH: '|',
};



function sendButtonId(button_id){
    fetch(SERVERLOC + '/button_id', {
        method: 'POST',
        body: button_id.toString(),
        headers: {
            'Content-Type': 'text/plain'
        }
    }).then(response => {
        console.log("Button Pressed:", button_id);
    }).catch(err => {
        console.error("Error:", err);
    });
}
// Get the keyboard and toggle button
const keyboard = document.getElementById('keyboard');

// Initially set to horizontal layout
keyboard.classList.add('button-grid-H');

// Toggle between horizontal and vertical layouts
function toggleLayoutBtn() {
    const keyboard = document.getElementById('keyboard');
    keyboard.classList.toggle('button-grid-V');
    keyboard.classList.toggle('button-grid-H');
}