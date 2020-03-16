from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pynput.keyboard import Key

# This file will define mouse functions

mouse = PyMouse()
mykeyboard = PyKeyboard()

myFlag = True
start = False
def on_press(key):
    print('{0} pressed'.format(key))


def on_release(key):
    global stop
    print('{0} release'.format(key))
    if key == Key.esc:
        return False
    if key == Key.enter:
        stop = True
        return False


def track_write():
    myFlag = True

    while myFlag:
        print(mouse.position())


def click_mouse(xPos, yPos):
    mouse.click(xPos, yPos)


def type_page(pageLocation):
    global stop
    stop = False
    try:
        with open(pageLocation, 'r') as pageRead:
            for line in pageRead:
                for words in line:
                    try:
                        mykeyboard.type_string(words, .01)
                    except:
                        continue
                mykeyboard.press_key(mykeyboard.enter_key)
                mykeyboard.release_key(mykeyboard.enter_key)


        mykeyboard.press_key(mykeyboard.enter_key)
        mykeyboard.release_key(mykeyboard.enter_key)

        print("Done")
    except:
        print("Failed openning the file Try again")


def get_mouse():
    done = False
    while not done:
        xloc, yloc = mouse.position()
    return xloc, yloc


