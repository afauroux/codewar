import threading
import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN     
import numpy as np, numpy.array as Vect
import logging, logging.info as log


logging.basicConfig(filename='log.txt',level=logging.DEBUG,
                    format='[%(asctime)s] %(message)s',
                    datefmt='%I:%M:%S',
                    filemode='w')



#class Vect(tuple):
#    def __init__(self,*args):
#        super(Vect,self).__init__(*args)
#    def __add__(s,o):
#        return Vect(s.x+o.x,s.y+o.y)

def init(screen):
    curses.noecho()
    curses.cbreak()
    screen.keypad(1) 
    screen.border(0)
    screen.refresh()

def main(screen):

    
    y, x = 0,0
    h, w = screen.getmaxyx()

    screen_pos = Vect((y,x))
    screen_size = Vect((h-2,w-2))
    pad_size = Vect((500,500))

    world = curses.newpad(*pad_size)
    world.addstr("hello"*(499))
    world.move(10,10)
    cursor = (10,10)
    world.refresh(x,y,1,1,h-2,w-2)


    while 1:            
        key = world.getch()
        if key == ord('q'):
            break


        prevcursor = Vect(world.getyx())

        newcursor = move(prevcursor,key,(0,0),pad_size)
        world.move(*newcursor)

        try:                
            if 32< key < 128:
                world.addstr(*prevcursor,chr(key))
        except Exception as e:
            log(e)
            
       
        if any(newcursor >= (screen_pos+screen_size)):  # when cursor on border we move the screen
            vec = newcursor - (screen_pos+screen_size)
            screen_pos += [c+1 if c>=0 else 0 for c in vec] # we keep only the coord that is outside the scr

        if any(newcursor < screen_pos):
            vec = newcursor - screen_pos
            screen_pos += [c if c<0 else 0 for c in vec]
            
        log('screen_pos = {}    cursor = {}'.format(screen_pos,newcursor))
    
        #newyx = move((y,x),key,(0,0),pad_size-screen_size)
            
        
        world.refresh(screen_pos[0],screen_pos[1],1,1,h-2,w-2)
     
           

            
def move(coord,key,cmin,cmax):
    coord = np.array(coord)
    cmin = np.array(cmin)
    cmax = np.array(cmax)
    
    shift =  ((key == KEY_DOWN  and  1)
            + (key == KEY_UP    and -1),
              (key == KEY_LEFT  and -1)
            + (key == KEY_RIGHT and  1))

    return (coord + (all(coord + shift >= cmin) 
            and all(coord + shift < cmax) 
            and shift or np.array([0,0])))


if __name__ == '__main__':   
    curses.wrapper(main)
