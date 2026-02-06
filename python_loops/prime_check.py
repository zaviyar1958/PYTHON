n = int(input("Enter a number: "))
if(n < 2):
    print("Not a prime number.")
elif(n == 2):
    print("it is a prime number.")
else:
    for i in range (2, int(n**0.5)+1):
        if n % i == 0 :
            print("Not a prime number.")
            break
    else: 
        print("It is a prime number.")
