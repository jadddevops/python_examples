
def sum(*args):
    print(args)
    c = 0     #   0 1  3 6 
    for i in args:
        c = c + i
    return c


def mul(*args):
    print(args)
    c = 1     #   0 1  3 6 
    for i in args:
        c = c * i
    return c

val1 = mul(1,2,3,4,5,6,7,8)
print(val1)