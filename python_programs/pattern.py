n=int(input())
for i in range(n*2):
    print("*",end=' ')
for i in range(n):
    for j in range(n*2):
        if j==i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
        