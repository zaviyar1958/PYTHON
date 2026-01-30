password = input("Enter your password: ")

digit_found = False
alpha_found = False
special_found = False

for char in password:
    if char.isdigit():
        digit_found = True
    elif char.isalpha():
        alpha_found = True
    elif not char.isalnum():
        special_found = True

if len(password) >= 8 and digit_found and alpha_found and special_found:
    print("Strong password")
elif len(password) >= 6 and (
        (digit_found and alpha_found) or
        (alpha_found and special_found) or
        (digit_found and special_found)):
    print("Moderate password")
else:
    print("Weak password")
