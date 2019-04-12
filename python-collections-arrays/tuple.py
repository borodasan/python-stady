#A tuple is a collection which is ordered and unchangeable.
#In Python tuples are written with round brackets.

#Create a Tuple
print("Create a Tuple:")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#You can access tuple items by referring to the index number,
#inside square brackets:

#Return the item in position 1
print("Return the item in position 1:")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#!!!Once a tuple is created, you cannot change its values.
#!!!Tuples are unchangeable.!!!

print("Once a tuple is created, you cannot change its values.")
print("!!!Tuples are unchangeable.!!!")
#You cannot change values in a tuple
print("You cannot change values in a tuple:")
thistuple = ("apple", "banana", "cherry")
#thistuple[1] = "blackcurrant" #delete commit '#' for check
# The values will remain the same:
print(thistuple)

#You can loop through the tuple items by using a for loop.
print("You can loop through the tuple items by using a for loop.")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#To determine if a specified item is present in a tuple use the in keyword

#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#To determine how many items a tuple has, use the len() method
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
print("Once a tuple is created, you cannot add items to it. Tuples are unchangeable.")
thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" # This will raise an error
print(thistuple)

#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
print("!!! Tuples are unchangeable !!!")
print("!!! So you cannot remove items from it, but you can delete the tuple completely !!!")

#The del keyword can delete the tuple completely
print("The del keyword can delete the tuple completely:")
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#It is also possible to use the tuple() constructor to make a tuple.
#Using the tuple() method to make a tuple
print("It is also possible to use the tuple() constructor to make a tuple.")
print("Using the tuple() method to make a tuple:")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
