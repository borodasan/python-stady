#A dictionary is a collection which is unordered, changeable and indexed
#In Python dictionaries are written with curly brackets, and they have keys and values.

#Create and print a dictionary
print("Create and print a dictionary:")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#You can access the items of a dictionary by referring to its key name,
#inside square brackets

print("You can access the items of a dictionary by referring to its key name, inside square brackets:")
print("Get the value of the \"model\" key:")

x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
print("There is also a method called get() that will give you the same result:")
print("Get the value of the \"model\" key:")

y = thisdict.get("model")
print(y)

print("You can change the value of a specific item by referring to its key name:")


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("Change the \"year\" to 2018:")
thisdict["year"] = 2018
print(thisdict)

print("When looping through a dictionary,")
print("the return value are the keys of the dictionary.")
print("Print all key names in the dictionary, one by one:")
for x in thisdict:
  print(x)


print("But there are methods to return the values as well.")
print("Print all values in the dictionary, one by one:")
for x in thisdict:
  print(thisdict[x])

print("You can also use the values() function to return values of a dictionary:")
for x in thisdict.values():
  print(x)

print("Loop through both keys and values, by using the items() function:")
for x, y in thisdict.items():
  print(x, y)
