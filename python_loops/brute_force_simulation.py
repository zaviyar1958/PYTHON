common_passwords = ["123456","password","123456789","12345","12345678","qwerty","111111","123123","abc123","password1","admin","admin123","letmein","welcome","iloveyou","monkey","dragon","football","sunshine","princess","login","master","hello","freedom","whatever","qazwsx","trustno1","starwars","654321","superman","batman","shadow","asdfgh","zxcvbn","michael","jordan","killer","computer","secret","password123","admin@123","root","root123","user","user123","test","test123","pass123","love","000000"]
entered_password = str(input('Please enter your password: '))
attempts = 0
found = False
for password in common_passwords:
    if entered_password == password :
        attempts += 1
        print('Weak password')
        print(f'Your password cracked in {attempts} attempt(s).')
        found = True
        break
    else:
        attempts += 1
if not found:
    print('Yay your password is strong.')
