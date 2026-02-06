print("Prime number between 1 to 50.")
for i in range (2, 51):
    isprime = True
    for j in range (2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime == True:
        print(i)
