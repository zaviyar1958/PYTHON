x = float(input("Enter a number : "))
if (x % 2 == 0) and (x > 0):
    print("The number is positive even")
elif (x % 2 != 0) and (x > 0):
    print("The number is positive odd")
elif (x % 2 == 0) and (x < 0):
    print("The number is negative even")
elif (x % 2 != 0) and (x < 0):
    print("The number is negative odd")
else:
    print("The number is zero")
