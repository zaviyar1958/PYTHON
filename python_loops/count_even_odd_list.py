print("Enter numbers separated by spaces:")
lst = [int(x) for x in input().split()]
counteven = countodd = 0
for i in lst:
    if i % 2 == 0:
        counteven += 1
    else:
        countodd += 1
print("Number of even numbers:", counteven)
print("Number of odd numbers:", countodd)
