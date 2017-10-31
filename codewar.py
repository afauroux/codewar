
import curses
from curses import wrapper,KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN            
def main(screen):
    
    
    # Clear screen
    curses.noecho()
    curses.cbreak()
    screen.keypad(1) 
   
    screen.border(0)
    screen.refresh()
    
    world = curses.newpad(500,500)
    y,x = 0,0
    h,w = screen.getmaxyx()
    world.addstr("hello"*(499))
    world.move(10,10)
    cursor = (10,10)
    world.refresh(x,y,1,1,h-2,w-2)
    world.keypad(1)
    while 1:
            
        key = world.getch()
        if key == ord('q'):
            break
    
    
        prevcursor = world.getyx()
        newcursor = move(prevcursor,key)
    
        if newcursor[0]<2 or newcursor[0]>h-3 or newcursor[1]>w-3 or newcursor[1]<2:
            y,x = move((y,x),key)
            world.move(*prevcursor)
        else:
            world.move(*newcursor)
        
        world.refresh(y,x,1,1,h-2,w-2)
        #stdscr.getkey()
                   
def move(coord,key):
    return (coord[0] +
    (key == KEY_DOWN and 1)+
    (key == KEY_UP and -1),
    coord[1] +
    (key == KEY_LEFT and -1)+
    (key == KEY_RIGHT and 1))

wrapper(main)