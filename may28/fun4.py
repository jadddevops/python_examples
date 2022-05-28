
def add(a,b,*args,**kwargs):
    print(args)
    print(kwargs)
    c = a + b
    return c


val1 = add(10,20,1,2,3,z=20,b1=30,b2=30)
print(val1)