# Simplified BSD License, Copyright 2011 Al Sweigart

import pygcurse, pygame, sys
from pygame.locals import *
import random
#---------PARAMETERS----------
w = 40
h = 25
win = pygcurse.PygcurseWindow(w,h)
win.autoblit = False
pygame.key.set_repeat(1,1)
screenColors = ('black','white')


#--------OBJECTS------------
class Entity:
    def __init__(self,char='@',x=w//2,y=h//2):
        self.x = x
        self.y = y
        self.char=char
    def pilot(self,event):
        prev = self.x,self.y
        if event.key == K_UP:
            self.move(prev,(0,1))
        elif event.key == K_DOWN:
            self.move(prev,(0,-1))
        elif event.key == K_LEFT:
            self.move(prev,(-1,0))
        elif event.key == K_RIGHT:
            self.move(prev,(1,0))
        
    def move(self,prev,shift):
        self.x=(self.x+shift[0])%w
        self.y=(self.y+shift[1])%h
        win.putchars(self.char,x=self.x,y=self.y)
        win.putchars(win.world.screen[prev],prev[0],prev[1])


#------------INIT----------------
mousex = mousey = 0
win.setscreencolors(*screenColors, clear=True)
bob =Entity() 
world = World(win)
world.generateScreen()
world.printScreen()
#------------Main Loop-----------
while True:
    for event in pygame.event.get(): # the event loop
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_p:
                win.fullscreen = not win.fullscreen
            elif event.key == K_d:
                win._debugchars()
            else:
                bob.pilot(event)
                
        elif event.type == MOUSEMOTION:
            mousex, mousey = win.getcoordinatesatpixel(event.pos)
   
    if world.moveScreen(mousex, mousey):
       world.generateScreen()
       world.printScreen()
    
  
    
    #win.setscreencolors(*screenColors, clear=True)
    #win.fill(bgcolor='red', region=(15, 10, 5, 5))
    #win.addshadow(51, (15, 10, 5, 5), bob.x=bob.x, bob.y=bob.y)

    #win.drawline((6,6), (mousex, mousey), bgcolor='red')
    #win.drawline((6,6), (mousex, mousey), char='+', fgcolor='yellow', bgcolor='green')

   # win.cursor = 0, win.height-3
    #win.write('Use mouse to move line, arrow keys to move shadow, p to switch to fullscreen.')
    #win.cursor = 0, win.height-1
    

    win.blittowindow()
    pygame.time.wait(50)