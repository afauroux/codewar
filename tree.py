import json
import numpy as np
from entities import AbstractEntitie

class Tree:
    root_regex = '{(.)}'
    plan="""
    {
        "tree": {
            "chars":"|/\\",
            "root":"|",
            "rules":{
                "|":  [["\\ /", [-1, -1],0.8], ["|",[-1,0],0.2]],                
                "/":  [["/",    [ -1, 1],0.8], ["|",[-1,0],0.2]],
                "\\": [["\\",   [-1, -1],0.8], ["|",[-1,0],0.2]]
               
            }
        }
    }
    """
    
    def generator(win, plan, total_s={}, prev_s={}, initPos=(0,0), ticks=1):
        """ new_s is the previous created char, only those will be generating in this iteration"""
        if not total_s:
            new_s = {initPos : plan["root"]}
         
        else:
            for i in range(ticks+len(total_s)**2): #delay between updates
                for k,v in total_s.items():
                    win.putchar('c',x=k[1]-win.x,y=k[0]-win.y)
                yield 
                # if len(total_s)>20:
                    # return 
            new_s={}
            for coord,char in prev_s.items():
                if char is ' ': continue #no need to draw spaces
                
                rules = plan["rules"][char]
                rule = rules[np.random.choice(len(rules),p=[r[2] for r in rules])]
                
                for i,c in enumerate(rule[0]):
                    new_coord = (coord[0]+rule[1][0],coord[1]+rule[1][1]+i)
                    new_s[new_coord] = c
        
      
        
        total_s.update(new_s)
        yield from generator(win,plan,total_s ,new_s)