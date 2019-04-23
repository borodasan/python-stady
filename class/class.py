print("Python is an object oriented programming language.")

print("\nAlmost everything in Python is an object, with its properties and methods.")

print("\nA Class is like an object constructor, or a \"blueprint\" for creating objects.")

print("\n\nTo create a class, use the keyword class:")
print("Create a class named MyClass, with a property named \'x\':")
class MyClass:
  x = 5

print(MyClass)

print("\n\nNow we can use the class named myClass to create objects:")
print("Create an object named \'p1\', and print the value of \'x\':")
p1 = MyClass()
print(p1.x)

print("\n\nThe \'__init__()\' Function")
print("\nAll classes have a function called \'__init__()\',")
print("which is always executed when the class is being initiated.")

print("\nUse the \'__init__()\' function to assign values to object properties,")
print("or other operations that are necessary to do when the object is being created.")

print("\nCreate a class named Person, use the \'__init__()\'")
print("function to assign values for name and age:")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("\nThe \'__init__()\' function is called automatically every time")
print("the class is being used to create a new object.")

print("\n\nObject Methods")
print("\nObjects can also contain methods.")
print("Methods in objects are functions that belongs to the object.")

print("\nLet us create a method in the Person class.")
print("Insert a function that prints a greeting, and execute it on the p1 object:")
print("\n")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 34)
p1.myfunc()


print("\n\nThe self Parameter")

print("\nThe \'self\' parameter is a reference to the current instance of the class,")
print("and is used to access variables that belongs to the class.")

print("It does not have to be named \'self\',")
print("you can call it whatever you like,")
print("but it has to be the first parameter of any function in the class:")

print("Use the words \'mysillyobject\' and \'abc\' instead of self:")
print("\n")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print("\n\nModify Object Properties")
print(p1.age)
print("You can modify properties on objects like this:")

print("\nSet the age of p1 to 40:")
p1.age = 40
print(p1.age)

print("\nYou can delete properties on objects by using the \'del\' keyword:")
print("Delete the age property from the p1 object:")

print(p1.age)
#del p1.age
print(p1.age)

print("\nYou can delete objects by using the \'del\' keyword:")
print("Delete the \'p1\' object")
#del p1
print(p1)
