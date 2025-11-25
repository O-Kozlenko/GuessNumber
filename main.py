import random
from pkgutil import resolve_name

randnum = random.randint(1,50)
user_input = input()
tries = 0
while True:
    if user_input.isdigit():
        if user_input == randnum:
            print()
            break
        elif user_input>50 or user_input<1:
            print()
        elif user_input!=randnum:
            tries+=1
    else:
        print()