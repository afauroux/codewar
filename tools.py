import numpy as np
V = np.array #conveniant shortcut for vectors

class TapeHead(object):
    def __init__(self,initVal):
        self.var = initVal
        self.pos = 0

class TapeMemory(dict):
    
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        self.head = V((0,0))
    def 
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        else:
            return 0 #infinite tape

    def __setitem__(self, key, val):
        if val is '+'
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)