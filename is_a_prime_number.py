from Tests.prime_numbers import prime_numbers
def is_a_prime_number(num: int) -> bool:
    for i in range(2, num):
        sum = str(num / i) 
        check = sum.split(".")[1]
        if len(check) == 1 and check == "0":
            return False
    return True

            
   
for i in prime_numbers:
    x = is_a_prime_number(i)
    if x == False:
        print(f"ERROR at number \"{i}\"")
        break

if x == True:
    print("ALL GOOD")
    