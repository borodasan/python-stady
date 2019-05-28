# Which line of the following Python program will never execute?

def stuff() :
    print("Hello")
    return
    print("World")

stuff()

print("Space")


def addtwo(a, b) :
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
