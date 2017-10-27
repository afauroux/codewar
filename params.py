import pygcurse, pygame, sys
from pygame.locals import *


#-----------WIN-INIT-------------
win_width  = 50
win_height = 30
screenColors = ('black','white')
cursorTint =  (-50, -50, -50)
cursorBorder = 5


#----------OTHER-PARAMS-----------



ascii = [chr(i) for i in range(32,127)]
 
#0         10    16       25     32                        58     65                       90  94
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#snahrrrannnrananrrrrrrrrrranaaarrllllllllllllllllllllllllllnnnnnnllllllllllllllllllllllllllnnnr
colors = ['yellow', 'fuchsia', 'red', 'silver', 'gray', 'olive', 'purple', 'maroon', 'aqua', 'lime', 'teal', 'green', 'blue', 'navy', 'black']
    
r = 0.01
a = 10
n = 0.25
l = 0.1
s = 1000
h = 500
ascii_abundance = [s,n,a,a,r,r,r,a,n,n,n,r,a,n,a,n,r,r,r,r,r,r,r,r,r,r,a,n,a,a,a,r,r,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,n,n,n,n,n,n,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,n,n,n,r]
ascii_abundance = [x/sum(ascii_abundance) for x in ascii_abundance]
ascii_abundance = ascii_abundance[:-1]+[1-sum(ascii_abundance[:-1])]