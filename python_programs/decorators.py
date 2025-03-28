def dec(func):
    def inner():
        print("In dec")
        func()
        print("Out dec")
    return inner
# @dec
def main():
    print("Orginal")
x=dec(main)
x()