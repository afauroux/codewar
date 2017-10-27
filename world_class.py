import params
from params import ascii,ascii_abundance
import numpy as np                       


class World:

    def __init__(self,win):
        self.win = win
        self.dimx = 1000
        self.dimy = 1000
        self.generateWorld()
        
    def generateWorld(self):
        print('generating world')
        np.random.seed(42)
        # Warning numpy choice uses np.str_ as strings
        self.map = np.random.choice(
            ascii, 
            size=(self.dimx,self.dimy),
            p=ascii_abundance
        )
        
        for i in range(5):
            ax = np.random.choice([0,1])
            rep = np.random.choice(4,size=(self.map.shape[ax]))
            self.map = np.repeat(self.map,rep,axis=ax)
            self.dimx,self.dimy = self.map.shape
        
        self.string = '\n'.join([''.join([str(c) for c in row]) for row in self.map])
        with open('worldview.txt','w') as f:
            f.write(self.string)
        print('done')
    
        
    def __str__(self):
        return self.string
    def convert2absolute(coord):
        pass
        
    def setChar(coord,char):
        """add a char at position coord (absolute)"""
        self.map[coord] = char
        
    def printScreen(self):
            
        self.win.putchars(self.string,x=0,y=0, indent=True)
            
     
     def printScreen(self):
        print('print screen')
        win_x = self.win.x
        win_y = self.win.y
        w = self.win.width
        h = self.win.height
        start_x = win_x+self.dim//2
        start_y = win_y+self.dim//2
        
        tab = self.map[start_y:start_y+h,start_x:start_x+w]
        
        s='\n'.join([''.join([str(c) for c in row]) for row in tab])
        self.win.putchars(s,x=0,y=0, indent=True)
            # self.map[start_x:start_x+w,start_y:start_y+h])
        # for i,x in enumerate(range(win_x,win_x+w)):
            # for j,y in enumerate(range(win_y,win_y+h)):
                # self.win.putchar(
                    # str(self.map[x+self.dim//2,y+self.dim//2]),
                    # x=i,
                    # y=j
                # )
        print('done')
     
