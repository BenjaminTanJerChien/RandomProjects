from player import Human, Computer


class TicTacToe:
    def __init__(self):
        self.board = [[" " for j in range(3)] for i in range(3)]
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row)+ ' |')

    def avaliable(self):
        available = []
        i = -1
        for x in self.board:
            i += 1
            for x, y in enumerate(x):
                if y == " ":
                    available.append([i, x])
        return available
    
    def empty(self):
        for x in self.board:
            for y in x:
                if y == " ":
                    return True
        return False

    def num_empty(self):
        i = 0
        for x in self.board:
            for y in x:
                if y == " ":
                    i += 1
        return i

    def make_move(self, row_v, col_v, letter):
        if self.board[row_v][col_v] == " ":
            self.board[row_v][col_v] = letter
            if self.win(row_v, col_v, letter):
                self.winner = letter
            return True
        return False

    def win(self, row_v, col_v, letter):
        # check rows
        for i in range(0, 2):
            if all(letter == self.board[i][n] for n in range(3)):
                return True
        # check cols
        for i in range(0, 2):
            if all(letter == self.board[n][i] for n in range(3)):
                return True
        # check diagonal
            if ((letter == self.board[0][0]) and (letter == self.board[1][1]) and (letter == self.board[2][2])) or ((letter == self.board[0][2]) and (letter == self.board[1][1]) and (letter == self.board[2][0])):
                return True

def play(game, player_x , player_o, print_text=True):
    if print:
        game.print_board()
    
    letter = 'x'
    while game.empty():
        if letter == 'o':
            row_v, col_v = player_o.get_move(game)
        else:
            row_v, col_v = player_x.get_move(game)
        
        if game.make_move(row_v, col_v , letter):
            print(f"{letter} made a move to {row_v} {col_v}")

        game.print_board()

        if game.winner:
            if print_text:
                print(letter + " won!")
            return letter
        letter = "o" if letter == "x" else "x"
        
        
    if print:
        print("Tie :/")
    return "tie"

if __name__ == '__main__':
    player_x = Human('x')
    player_o = Computer('o')
    t = TicTacToe()
    play(t, player_x, player_o, print_text=True)




