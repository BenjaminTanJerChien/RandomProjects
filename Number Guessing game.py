from ctypes.wintypes import WORD
import random

def guess_num(max_num=10, tries=5):
    number = random.randint(1, max_num)
    while tries > 0:
        my_guess = input("Your Guess: ")
        try:
            my_guess = int(my_guess)
        except:
            print("Use a number please")
            continue
        if number < my_guess:
            print("Too high!")
        elif number > my_guess:
            print("Too low!")
        else:
            break
        tries -= 1
    if tries <= 0:
        print("Better luck next time")
    else: 
        print(f'Congats! The number is indeed {number}')

guess_num()