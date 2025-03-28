def add(n):
    return lambda a : a + n
x=add(10)
print(x(20))