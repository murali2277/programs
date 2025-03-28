lst=[10,30,20,50,60,100]
x=iter(lst)
print(x) # return object
print(next(x))
print(next(x))
while True:
    try:
        print(next(x))
    except StopIteration:
        print("End of iteration")
        break
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))