print("Python does not have built-in support for Arrays,")
print("but Python Lists can be used instead.")

print("\nArrays are used to store multiple values in one single variable.")
print("Create an array containing car names:")
cars = ["Ford", "Volvo", "BMW"]

print("\nAn array is a special variable,")
print("which can hold more than one value at a time.")
print(cars)

print("\nAn array can hold many values under a single name,")
print("and you can access the values by referring to an index number.")
print("You refer to an array element by referring to the index number.")

print("\nGet the value of the first array item:")
x = cars[0]
print(x)

print("\nModify the value of the first array item:")
print(cars)
cars[0] = "Toyota"
print(cars)

print("\nUse the \'len()\' method to return the length")
print("of an array (the number of elements in an array).")
print("Return the number of elements in the cars array:")
x = len(cars)
print(x)

print("\nThe length of an array is always one more")
print("than the highest array index.")

print("\nYou can use the \'for\' in loop")
print("to loop through all the elements of an array.")
for x in cars:
    print(x)

print("\nYou can use the \'append()\' method to add an element to an array.")
print("Add one more element to the cars array:")
cars.append("Honda")
print(cars)

print("\nYou can use the \'pop()\' method to remove an element from the array.")
print(cars)
print("Delete the second (Volvo) element of the cars array:")
cars.pop(1)
print(cars)

print("\nYou can also use the \'remove()\' method")
print("to remove an element from the array.")
print(cars)
print("Delete the element that has the value \'Honds\':")
cars.remove("Honda")
print(cars)

print("\nThe remove() method only removes the first occurrence of the specified value.")
