x, y, z = map(int, input("Enter three numbers : ").split())
if (x >= y and x >= z):
    print("greater : ",x)
elif(y >= x and y >= z):
    print("greater : ",y)
else:
    print("greater : ",z)
