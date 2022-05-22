#print("hi")

#    0 1 2  3   4   5   6  7
from itertools import tee
from re import I


a = [1,2,3,'x','y','z','d','x']
count = 0
for item in a:
    if item == 'x':
        count += 1
        #print(count)

print(count)
