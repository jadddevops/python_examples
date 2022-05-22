
a = {'name': 'max','age': 40}
print(id(a))
b = a.copy()
#b = a
b['mmm'] = 'u'
print(id(b))
print(a)
print(b)
print(dir(a))