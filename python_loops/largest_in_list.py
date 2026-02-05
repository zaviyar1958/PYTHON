print("Enter numbers separated by spaces:")
lst = [int(x) for x in input().split()]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("Largest number:", largest)
