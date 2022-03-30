import random

def play():
    user_input = input("Rock (r), Paper (p), Scissors (s): ")
    comp_input = random.choice(["r", "p", "s"])

    if user_input == comp_input:
        return "It's a tie :/"
    elif (user_input == "r" and comp_input == "p") or (user_input == "p" and comp_input == "s") or (user_input == "s" and comp_input == "r"):
        return "You lost :("
    else:
        return "You won!"

while True:
    print(play())