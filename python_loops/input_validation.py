guessing_number = 13

while True:
    guessed_number = int(input("Enter guessed number between 1-20: "))

    if guessed_number < 1 or guessed_number > 20:
        print("Please enter a number between 1 and 20.")
    elif guessed_number != guessing_number:
        print("Wrong guess. Guess again...")
    else:
        print("You guessed it right.")
        break
