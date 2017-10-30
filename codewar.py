
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
        cursor = world.getyx() 
        if cursor[0]<1 and y > 2:
            y+=-1
        if cursor[0]>h-2 and y < h-2:
            y+=1
        if cursor[1]<1 and x> 2:
            x+=-1
        if cursor[0]>w-2 and x<w-2:
            x+=1
        else:
            world.move(cursor[0]+ 
                (key == KEY_DOWN and 1)+ 
                (key == KEY_UP and -1), 
               	cursor[1] +
               	 (key == KEY_LEFT and -1)+
                 (key == KEY_RIGHT and 1))
            
        world.refresh(y,x,1,1,h-2,w-2)
        #stdscr.getkey()                   

wrapper(main)