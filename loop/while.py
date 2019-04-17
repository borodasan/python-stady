
print("Python has two primitive loop commands:")
print("1) while loops")
print("2) for loops")

print("With the while loop we can execute a set of statements as long as a condition is true.")

print("Print i as long as i is less than 6:")
i = 1
while i < 6:
  print(i)
  i += 1

print("With the break statement we can stop the loop even if the while condition is true:")
print("Exit the loop when \'a\' is 3:")
a = 1
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1

print("With the continue statement we can stop the current iteration, and continue with the next:")
print("Continue to the next iteration if \'i\' is 3:")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
