#print("hi")

#    0 1 2  3   4   5   6  7
from itertools import tee
from re import I


a = [1,2,3,'x','y','z','d','x']
# c = "x"
# b = ['f','g']

# a.pop(3)
# a.pop(5)
#a.remove('x')
# a.extend(c)
#print(a)
#print(dir(a))
count = 0
for item in a:
    #count = count + 1
    if item == 'x':
        a.pop(count)
    count += 1
    # a.append(item)

print(a)
