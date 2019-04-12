#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.

print("A set is a collection which is")
print("unordered and unindexed".upper())
print("In Python sets are written with curly brackets.")

#Create a Set
print("Create a Set:")
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("Sets are unordered, so the items will appear in a random order.")

print("You cannot access items in a set by referring to an index,")
print("since sets are unordered the items has no index.")
print("But you can loop through the set items using a")
print("for".upper())
print("loop,")
print("or ask if a specified value is present")
print("in".upper())
print("a set, by using the in keyword.")
print("Loop through the set, and print the values:")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
print("Check if \"banana\" is present in the set:")
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

print("To add one item to a set use the add() method.")
print("To add more than one item to a set use the update() method.")
print("Add an item to a set, using the add() method:")

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("Add multiple items to a set, using the update() method:")
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
