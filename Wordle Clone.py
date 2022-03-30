from Databases.wordle_words import words
import random 

# len(words) == 12972 | We don't bother counting each time as it wastes resources

def wordle_clone(tries=6):
    word = words[random.randint(0, 12971)]
    print(word)

wordle_clone()