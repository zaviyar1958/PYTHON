# Program to check whether an IP address is private or public

a, b, c, d = map(int, input("Enter the IP address: ").split("."))

if a == 10:
    print("It is a private network.")
elif a == 172 and 16 <= b <= 31:
    print("It is a private network.")
elif a == 192 and b == 168:
    print("It is a private network.")
else:
    print("It is a public network.")
