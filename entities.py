import re
#from tree import Tree
#from animal import Animal
from numpy.lib.stride_tricks import as_strided

class AbstractEntitie:
    root_regex = "(.)"
    
    def __init__(self,world, initPos, regex_groups):
        self.world = world
        self.coord = initPos
        self.regex_groups = regex_groups
    

class Animal(AbstractEntitie):
    root_regex = '&'
    pass
    
class Tree(AbstractEntitie):
    root_regex = '{(.)}'
    
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
if __name__ == '__main__' or True:           
    world = lambda : None
    world.string = """
                                                                                         
                                                                                         
                                                                                         
                                                                                         
                                                          {r}                               
                  {c}                                                                       
                                                                                         
                                                                                         
                                                                                         
                                                &                                         
                                                                                         
                                                                                         
                                                                                         
                                                                                         
    """

    entities = find_all_entities(world)
