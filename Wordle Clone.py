from Databases.wordle_words import words
import random 

# colors 
yellow = '\033[93m'
green = '\033[92m'
red = '\033[91m'
end = '\033[0m'
# len(words) == 12972 | We don't bother counting each time as it wastes resources

def wordle_clone(tries=6):
    master = []
    used = []
    word = words[random.randint(0, 12971)].upper()
    word = list(word)
    print(word)
    while tries > 0:
        user_input = input("Your guess: ").upper()
        if len(user_input) != 5:
            print("Words are 5 Charaters Long!")
            continue
        ans = []
        n = 0 
        for i in user_input:
            if i == word[n]:
                ans.append([i, 1])
            elif i in word:
                ans.append([i, 2])
            else:
                ans.append([i, 0])
                if i not in used:
                    used.append(i)
            n += 1
        master.append(ans)
        for j in master:
            for k in j:
                if k[1] == 1:
                    print(f"{green}{k[0]}{end}",end="")
                elif k[1] == 2:
                    print(f"{yellow}{k[0]}{end}", end="")
                else:
                    print(k[0], end="")
            print(" ")
        if list(user_input) == word:
            break
        used.sort()
        print("Invalid Characters: " + " ".join(used) + "\n")
        tries -= 1


    if tries == 0:
        print(f"{red}Too bad, try again next time :/ {end}")     
    else: 
        print(f"{green}Good job, you got it {len(master)} tries!{end}") 
        	
wordle_clone()