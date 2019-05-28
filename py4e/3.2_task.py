# Input user Hours and Rate
hrs = input("Enter Hours: ")
rt = input("Enter Rate: ")
try :
    hours = float(hrs)
    rate = float(rt)
except :
    print("Error, please enter numeric input")
    quit()

if hours > 40 :
    # print("Overtime")
    reg = rate * hours
    otp = (hours - 40.0) * (rate * 0.5)
    # print(reg,otp)
    sum = reg + otp
else :
    # print("Regular")
    sum = rate * hours
print(sum)
