usr_input = input("Enter you string: ")
count = usr_input.split(" ")
c = 0
for i in count:
    if i != '':
        c += 1
print("Number of words is = ",c)
