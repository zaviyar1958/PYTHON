n = int(input("print number of terms for fibonacci: "))
x1 = 0 
x2 = 1
print(x1,  x2  , end = " ")
for i in range(n-2):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print(x3  ,end =" ")
