#A list is a collection which is ordered and changeable
#In Python lists are written with square brackets

thislist = ["apple", "banana", "cherry"]
print(thislist)

#You access the list items by referring to the index number:
print("You access the list items by referring to the index number:")
print(thislist[1])

#To change the value of a specific item, refer to the index number
print("To change the value of a specific item, refer to the index number:")
thislist[1] = "blackcurrant"
print(thislist)

#You can loop through the list items by using a for loop
print("You can loop through the list items by using a for loop:")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#To determine if a specified item is present in a list use the in keyword
print("To determine if a specified item is present in a list use the in keyword:")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#To determine how many items a list has, use the len() method
print("To determine how many items a list has, use the len() method:")
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#To add an item to the end of the list, use the append() method
print("To add an item to the end of the list, use the append() method:")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method
print("To add an item at the specified index, use the insert() method:")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#There are several methods to remove items from a list
#The remove() method removes the specified item:
print("The remove() method removes the specified item:")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index,
# (or the last item if index is not specified):
print("The pop() method removes the specified index, (or the last item if index is not specified):")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword removes the specified index
print("The del keyword removes the specified index:")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely
print("The del keyword can also delete the list completely:")
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list
print("The clear() method empties the list:")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("Copy List")
print("Copy List")
print("Copy List")

""" You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2."""

#Make a copy of a list with the copy() method
print("Make a copy of a list with the copy() method:")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list()
print("Make a copy of a list with the list() method")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
