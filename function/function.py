print("A function is a block of code which only runs when it is called.")
print("You can pass data, known as parameters, into a function.")
print("A function can return data as a result.")

print("In Python a function is defined using the def keyword:")
def my_function():
    print("Hello from a function")

my_function()

print("The following example has a function with one parameter (fname).")
print("When the function is called, we pass along a first name,")
print("which is used inside the function to print the full name:")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("The following example shows how to use a default parameter value.")
print("If we call the function without parameter, it uses the default value:")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("You can send any data types of parameter to a function")
print("(string, number, list, dictionary etc.),")
print("and it will be treated as the same data type inside the function.")
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print("To let a function return a value, use the return statement:")
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print("Recursion Example")
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-2)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(8)
