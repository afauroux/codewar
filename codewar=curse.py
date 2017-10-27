import curses
from curses import wrapper

def main(screen):
    curses.textpad.Textbox(screen)
    while True:
        # Clear screen
        screen.clear()
        

        screen.refresh()
        #stdscr.getkey()           

wrapper(main)