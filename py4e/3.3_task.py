# Input user Hours and Rate

score = input("Enter Score between 0.0 and 1.0: ")

try :
    grade = float(score)
except :
    print("Error, error!")
    print("Please enter score between 0.0 and 1.0")
    quit()

if grade >= 0.9 and grade <= 1 :
    # Grade is A
    result =print("You grade is A")
elif grade >= 0.8 and grade < 0.9 :
    # Grade is B
    result = print("You grade is B")
elif grade >= 0.7 and grade < 0.8 :
        # Grade is C
        result = print("You grade is C")
elif grade >= 0.6 and grade < 0.7 :
        # Grade is D
        result = print("You grade is D")
elif grade >= 0.0 and grade < 0.6 :
        # Grade is F
        result = print("You grade is F")
else :
    # You Died
    result = print("This in NOT correct grade!")
