import curses
from curses import wrapper

def main(screen):
    
    while True:
        # Clear screen
        screen.clear()
        screen.refresh()
        curses.cbreak()
        world = curses.newpad(500,500)
        y,x = 100,100
        h,w = screen.getmaxyx()
        #world.addstr("hello"*(500*500))
        for y in range(0, 500):
            for x in range(0, 500):
                try:
                    world.addch(y,x, ord('a') + (x*x+y*y) % 26)
                except curses.error:
                    pass

        while 1:
            
            c = world.getkey()
            if c == curses.KEY_BACKSPACE:
                break
            world.refresh(x,y,0,0,h-1,w-1)
        #stdscr.getkey()           

wrapper(main)