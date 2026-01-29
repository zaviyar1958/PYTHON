number = float(input("Enter a number: "))
if (number % 2 == 0 and number > 0):
    print ("Number is positive even.")
elif (number % 2 != 0 and number > 0):
    print ("Number is positive odd.")
elif (number % 2 == 0 and number < 0):
    print("Number is negative even.")
elif (number % 2 != 0 and number < 0): 
    print("Number is negative odd.")
else:
    print("Number is zero.")
