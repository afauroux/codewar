
import curses
from curses import wrapper,KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN     
import numpy as np

Vect = np.array
       
def main(screen):

    # Clear screen
    curses.noecho()
    curses.cbreak()
    screen.keypad(1) 
    screen.border(0)
    screen.refresh()

    y,x = 0,0
    h,w = screen.getmaxyx()

    screen_pos = Vect((y,x))
    screen_size = Vect((h-2,w-2))
    pad_size = Vect((500,500))

    world = curses.newpad(*pad_size)
    world.addstr("hello"*(499))
    world.move(10,10)
    cursor = (10,10)
    world.refresh(x,y,1,1,h-2,w-2)
    world.keypad(1)

    while 1:            
        key = world.getch()
        if key == ord('q'):
            break
    
        prevcursor = Vect(world.getyx())
        newcursor = move(prevcursor,key,(0,0),pad_size)
        world.move(*newcursor)

        if any(newcursor >= (screen_pos+screen_size)):
            screen_pos += newcursor - (screen_pos+screen_size)

        if any(newcursor <= screen_pos):
            screen_pos +=  newcursor - screen_pos
 
    
        newyx = move((y,x),key,(0,0),pad_size-screen_size)
            
        
        world.refresh(screen_pos[0],screen_pos[1],1,1,h-2,w-2)
     
           

            
def move(coord,key,cmin,cmax):
    coord = np.array(coord)
    cmin = np.array(cmin)
    cmax = np.array(cmax)
    
    shift = ((key == KEY_DOWN and  1)
             + (key == KEY_UP   and -1),
             (key == KEY_LEFT and -1)
             + (key == KEY_RIGHT and 1))

    return  coord + (all(coord+shift>cmin) and all(coord+shift<cmax) and shift or np.array([0,0]))
  
wrapper(main)
