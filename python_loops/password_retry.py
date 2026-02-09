password = 'weakpassword'
for i in range(3, 0, -1):
    passs = input("Welcome. Please Enter you password: ")
    if passs == password:
        print("Hey you successfully logged in.")
        break
    elif i-1 == 0:
        print('Wrong password.')
        print('Your account is locked.')
    else:
        print(f"Wrong password. Your account will be locked after {i-1} attempt.")
        print("Please try again: ")
        
