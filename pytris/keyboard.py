import sys
import tty
import termios


# TODO maybe check
# http://stackoverflow.com/questions/1054380/how-can-you-read-keystrokes-when-the-python-program-isnt-in-the-foreground
# evdev
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch