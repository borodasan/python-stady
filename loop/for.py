#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
print("A for loop is used for iterating over a sequence")
print("that is either a list, a tuple, a dictionary, a set, or a string")

print("With the for loop we can execute a set of statements, once for each item")
print("in a list, tuple, set etc.")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("The for loop does not require an indexing variable to set beforehand")

print("Even strings are iterable objects, they contain a sequence of characters:")
for x in "banana":
    print(x)

print("With the break statement we can stop the loop")
print("before it has looped through all the items:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("Exit the loop when x is \"banana\",")
print("but this time the break comes before the print:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


print("With the continue statement we can stop")
print("the current iteration of the loop, and continue with the next:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("To loop through a set of code a specified number of times,")
print("we can use the \'range()\' function.")
print("The \'range()\' function returns a sequence of numbers,")
print("starting from 0 by default, and increments by 1 (by default),")
print("and ends at a specified number.")

print("Using the range() function:")
for x in range(6):
    print(x)
print("Note that range(6) is not the values of 0 to 6, but the values 0 to 5.")

print("The '\range()\' function defaults to 0 as a starting value,")
print("however it is possible to specify the starting value by adding a parameter:")
print("range(2, 6), which means values from 2 to 6 (but not including 6):")
for x in range(2, 6):
    print(x)

print("The \'range()\' function defaults to increment the sequence by 1,")
print("however it is possible to specify the increment value by adding a third parameter:")
print("range(2, 30, 3):")
for x in range(2, 30, 3):
    print(x)

print("The \'else\' keyword in a \'for\' loop specifies a block of code")
print("to be executed when the loop is finished:")

print("Print all numbers from 0 to 5, and print a message when the loop has ended:")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("A nested loop is a loop inside a loop.")
print("The \"inner loop\" will be executed one time")
print("for each iteration of the \"outer loop\":")

print("Print each adjective for every fruit:")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
