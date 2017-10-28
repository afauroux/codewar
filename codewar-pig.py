"""
Main engine of codewar
"""
import traceback
import pygcurse, pygame, sys
from pygame.locals import *
import random
import params as par
from world_class import World 
import generator as G

#------------INIT----------------
def init_win():
    win = pygcurse.PygcurseWindow(par.win_width,par.win_height)
    win.autoblit = False
    pygame.key.set_repeat(1,1)
    win.x = 0
    win.y = 0
    win.cursor=(par.win_width//2,par.win_height//2)
    win.cursorTint = par.cursorTint
    win.cursorBorder = par.cursorBorder
    win.setscreencolors(*par.screenColors, clear=True)
    return win
    
def init_world(win):
    world = World(win)
    return world

#------------Main Loop-----------
def main_loop(win,world):
    prev_xy = (1,1)
    tree1 = G.generator(win,G.plan,initPos=(20,15))
    while True:
        
        if pygame.event.get(pygame.QUIT): 
            pygame.quit()
            sys.exit()
        pygame.event.pump()

        # move up/down by checking for pressed keys
        # and moving the paddle rect in-place
        main_listener(win,pygame.key.get_pressed())
       
        
        # for event in pygame.event.get(): # the event loop
            # main_listener(win,event)
        if (win.x,win.y) != prev_xy:
            win.setscreencolors(*par.screenColors, clear=True)
            world.printScreen()
            prev_xy = (win.x,win.y)
        try:
            next(tree1)
        except StopIteration:
            pass
        
        win.settint(*win.cursorTint,(*win.cursor,1,1))
        win.update()
        win.blittowindow()
        pygame.time.wait(50)
    
    
#---------EVENT HANDLING---------
def main_listener(win,keys):
     if keys[pygame.K_UP]: moveCursor((-1,0))
     if keys[pygame.K_DOWN]: moveCursor((1,0))
     if keys[pygame.K_LEFT]: moveCursor((0,-1))
     if keys[pygame.K_RIGHT]: moveCursor((0,1))
     if keys[pygame.K_d]: win._debugchars()
     for i,b in enumerate(keys):
        if i>=33 and i<127 and b:
            win.putchar(chr(i))
            break
        
def moveCursor(motion):
    win.settint(0,0,0,(*win.cursor,1,1))
    win.cursory += motion[0]
    win.cursorx += motion[1]
    if win.cursorx<=win.cursorBorder:
        win.x+=-1
        win.cursorx+=1            
    if win.cursorx>=win.width-win.cursorBorder:
        win.x+=1
        win.cursorx+=-1            
    if win.cursory<=win.cursorBorder:
        win.y+=-1
        win.cursory+=1            
    if win.cursory>=win.height-win.cursorBorder:
        win.y+=1
        win.cursory+=-1
        
        

if __name__=='__main__' or True:   

    try:
        win = init_win()
        world = init_world(win)
        main_loop(win,world)
        
    except Exception as error:
        traceback.print_exc()
    finally:
        pygame.quit()
        sys.exit()