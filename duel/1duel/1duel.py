def p(p):
    for i in range(0,5,2):  #The range() function defaults to increment the sequence by 1,
                            #however it is possible to specify the increment
                            #value by adding a third parameter: range(0, 5, 2)
             #Assignment operators are used to assign values to variables:
        p+=i #p += i --> p = p + i
    p-=2     #p -= 2 --> p = p - 2
    print(p)
p(2)

print("\nExample Range")
for x in range (0,5,2):
    print(x)
