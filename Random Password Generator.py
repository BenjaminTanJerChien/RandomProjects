# random string password generator 

import random as rn 

print("===Password Generator===")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstovwxys0123456789!@#$%^&*()_+=-<>,.?:;'"

numPass = int(input("Number of passwords: "))
lenPass = int(input("Length of password: "))
print("\nGenerating passwords...\n")

for pwd in range(numPass):
    password = ''
    for c in range(lenPass):
        password += rn.choice(chars)
    print(password)


    