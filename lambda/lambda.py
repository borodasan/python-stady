print("The expression is executed and the result is returned:")

print("A lambda function that adds 10 to the number passed in as an argument,")
print("and print the result:")
x = lambda a : a + 10
print(x(5))

print("\nA lambda function that multiplies")
print("argument \'a\' with argument \'b\' and print the result:")
x = lambda a, b : a * b
print(x(5, 6))

print("\nA lambda function that sums argument")
print("\'a\', \'b\', and \'c\' and print the result:")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("\nUse that function definition to make a function")
print("that always doubles the number you send in:")
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print("\nOr, use the same function definition to make a function")
print("that always triples the number you send in:")
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print("\nOr, use the same function definition")
print("to make both functions, in the same program:")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print("\nUse lambda functions when an anonymous function")
print("is required for a short period of time.")
