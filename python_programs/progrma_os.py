import os
from os import path
# print(os.listdir(r"E:\git\vulnerabality-scanner"))
# os.chdir(r"E:\python_programs")
# os.mkdir("sample.txt")
# print(os.getcwd())
# print(os.listdir())
# os.rmdir("sample.txt")
# print(os.listdir())
# print(os.stat("main.py").st_size)
# x=os.system("dir")
# print(x)
# print(os.getcwd())
x=os.walk(os.getcwd())
# print(x)
# print(next(x))
for i in x:
    print(i)
# print(next(os.walk(os.getcwd())))
os.chdir(r"C:\Users\mural\OneDrive\Documents\robotics")
file=os.listdir()
for i in file:
    if not path.isdir("i"):
        print("Yes")
os.chdir(r"E:\python_programs")
print(os.listdir())
print(os.path.split("func.py"))
print(os.path.splitext("func.py"))