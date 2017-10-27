import json
import numpy as np

plan = json.load(open('generator.json','r'))
plan = plan["tree"]

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

def toString(scheme):
    scheme = scheme.copy()
    s=scheme.pop(0,0)
    coords = sorted(scheme.keys())
    
    for coord in coords:
        pass

def print_fig(scheme,whiteboard):
    min=[1000,1000]
    max=[-1000,-1000]

    for coord in scheme:
        for i in [0,1]:
            min[i] = coord[i] if coord[i]<min[i] else min[i]   
            max[i] = coord[i] if coord[i]>max[i] else max[i] 
   
    width = (max[0]-min[0]+1)//2*2+1
    height = max[1]-min[1]+1
    out = np.empty((width,height),dtype=str)
    print(out)
    print(min,max)
    for row in range(len(out))[::-1]:
       
        for coord,char in scheme.items():
            coord = (len(out)-coord[1]-1,len(out[0])//2-coord[0])
            print(coord) 
            out[coord] = char
        
    print('\n'.join([' '.join([str(c) for c in row]) for row in out]))


# for scheme in generator(plan,None):
    # print(scheme)
    # print_fig(scheme)
    # c=input()
    # if c is'n':
        # break