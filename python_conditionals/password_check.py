# Simple user authentication program

username = "zaviyar"
password = "1958"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login successful.")
else:
    print("Invalid username or password")
