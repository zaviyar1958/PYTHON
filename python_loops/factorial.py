num = int(input("Enter number to find factorial: "))
fact = 1
for i in range(1, num+1) :
    fact *= i
print("Factorial of number ",num ,"is = ",fact)
