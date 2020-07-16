import termios, sys

stdin_fd = sys.stdin.fileno()

def getch():

    new = termios.tcgetattr(stdin_fd)
    new[3] = new[3] & ~termios.ICANON
    new[3] = new[3] & ~termios.ECHO

    try:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, new)

        ch = sys.stdin.read(1)
        if ch != '\x1b': return ch

        ch = sys.stdin.read(1)
        if ch != '[': return ch

        ch = sys.stdin.read(1)
        return ch

    except: return 'exception'

if __name__ == "__main__":
    while True:
        print(getch()*100)