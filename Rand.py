import random
from random import seed
from random import randint
# seed random number generator
seed(1)
global z
z = 0
x = []
# generate some integers
while z <= 100:
    z += 1
    if z <= 10:
        y = randint(0,242)
    else:
        y = randint(0,242)
        x.append(y)
    print x
