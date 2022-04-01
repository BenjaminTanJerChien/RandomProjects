import math 
import random 

class Player:
    def __init__(self, letter):
        self.letter = letter # x or o 

    def get_move(self, game):
        pass

class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        choice = random.choice(game.avaliable())
        return choice

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid = False 
        while not valid:
            choice = input(f"{self.letter}'s turn. Input move row (0-2) by column (0-2): ")
            try:
                value = choice.split()
                row_v, col_v  = int(value[0]), int(value[1])
                if [row_v, col_v] not in game.avaliable():
                    raise ValueError
                valid = True
            except: 
                print("Invalid input")


        return [row_v, col_v]

    