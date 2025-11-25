import random
randnum = random.randint(1,50)
tries = 0
print("Welcome to GuessNumber!")
print("What is your guess?(1-50):")
while True:
    user_input = input()
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == randnum:
            while True:
                print("You guessed! GG")
                print("Your tries:", tries)
                print("Try again?")
                print("Yes/No")
                user_input = input()
                if user_input == "Yes" or user_input == "yes":
                    tries = 0
                    randnum = random.randint(1, 50)
                    print("Difficulty:")
                    print("Easy/Normal")
                    difficulty = input()
                    print("What is your guess?(1-50):")

                elif user_input == "No" or user_input == "no":
                    break
                else:
                    print("Type Yes or No")
        elif user_input > 50 or user_input < 1:
            print("Error 1")
            print("Try writing number from 1 to 50")
        elif user_input != randnum:
            if user_input > randnum:
                print("Try lower number")
            elif user_input < randnum:
                print("Try higher number")
            tries += 1
    else:
        print("That's not number")