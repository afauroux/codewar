import re
#from tree import Tree
#from animal import Animal
import random
import numpy as np
from Math import *
V = np.array

class AbstractEntitie:
    root_regex = "(.)"

    def __init__(self,world, initPos, regex_groups):
        self.world = world
        self.coord = np.array(initPos)
        self.regex_groups = regex_groups

    def update(self):
      while c in dna:
        if c == '.':
          yield
        if
class Head(object):
    def __init__(self,animal):
        self.coord = (0,0)
        self.mem = [0]*9
        self.animal = animal
    def __int__()



def spiral(n):
    """ gives the next move for a spiraling cursor on a grid
    noticing than a square spiral is always >v<<^^>>>vvv e.g 112233445566
    n is the flaten position
    return one move
    """
     root = round(sqrt(n))

     return V( n>root**2 and (root%2 and [ 1, 0] or [-1, 0] )
                          or (root%2 and [ 0, 1] or [ 0,-1] ))



class Animal(AbstractEntitie):
    root_regex = '&'
    dna = ',.><[]+-' #positive indices of the tape corespond to spiral outward, negative is storage



    def run(self,cmd):
        if cmd == ',':
            self.head = self.world.getch(*self.head.coord)
        elif cmd=='.'
            self.world.addch(*self.head.coord)





    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.mem[0]


    def update(self):
      while self.alive:
        dirs = [V((i,j)) if i*j==0 else V((0,0)) for i in [-1,1,0] for j in [-1,1,0]]
        newcoord = self.coord + random.choice(dirs)
        yield [
          [' ',self.coord],
          ['&',newcoord]
        ]
        self.coord = newcoord




class Tree(AbstractEntitie):
    root_regex = '({(.)})'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.seed = self.regex_groups[0]




def find_all_entities(world, species = {Tree, Animal}):
    entities = []
    for specie in species:
        results = re.finditer(specie.root_regex,world.string)

        if results:
            for res in results:
                entities.append(specie(world,res.span(),res.groups()))
    return entities

class World(object):
    string = """




                                                          {r}
                  {c}



                                                &




    """

    def update():


if __name__ == '__main__' or True:
    world = World()


    entities = find_all_entities(world)
