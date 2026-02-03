print("sum of N numbers")
N = int(input("Enter the value of N: "))
sum = 0
for i in range(1, N + 1):
    sum += i 
print(f"The total sum of first {N} numbers is {sum}")
