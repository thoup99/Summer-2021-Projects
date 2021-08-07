import random

game_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

X_wins = 0
O_wins = 0
Ties = 0

def fix_board():
    global game_board
    game_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

class RandomPlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_pinp(self, open_slots):
        return(self.letter, random.choice(open_slots))

class Game():
    def __init__(self, x_player, o_player):
        self.x_player = x_player
        self.o_player = o_player

    def check_win(self):
        ##Checks rows
        for row in game_board:
            if all(x == row[0] for x in row):
                return (True)
        ##Checks collumns
        for x in range(3):
            if (game_board[0][x] == game_board[1][x] and game_board[1][x] == game_board[2][x]):
                return (True)
        ##Checks diagonals
        if ((game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2]) or (game_board[0][2] == game_board[1][1] and game_board[0][2] == game_board[2][0])):
            return(True)
        return(False)

    ##Creates a list with every available spot
    def open_spots(self):
        op_spots = []
        for row in game_board:
            for item in row:
                if item in "123456789":
                    op_spots.append(item)
        return(op_spots)

    def num_open_slots(self): #Finds out how many playable spots there are
        op_slots = 0
        for row in game_board:
            for col in row:
                if col in "123456789":
                    op_slots += 1
        return(op_slots)

    def replace(self, letter_num): #Replaces the selected spot with a letter
        letter = letter_num[0]
        num = letter_num[1]
        for ir, row in enumerate(game_board):
            for ic, col in enumerate(row):
                if col == num:
                    game_board[ir][ic] = letter

    ## gets the input from whichever class is the X/O player
    def get_inp(self, letter, op_slots):
        if (letter == "X"):
            self.replace(self.x_player.get_pinp(op_slots))
        else:
            self.replace(self.o_player.get_pinp(op_slots))

##sets the Random player class to either X or O
game = Game(RandomPlayer("X") , RandomPlayer("O"))

def play(): #Runs the whole game.Can be run with simulations in this way
    global X_wins, O_wins, Ties
    turn = "X"
    while (game.num_open_slots() != 0):
        game.get_inp(turn, game.open_spots())
        if game.check_win() == True:
            if turn == "X":
                X_wins +=1
            else:
                O_wins +=1
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    if (game.check_win() == False):
        Ties += 1

sims = int(input("How many times would you like to run the simulation: "))
for x in range(sims):
    fix_board()
    play()

print("The simulation ended with the following results:\nX wins: "+str(X_wins)+"\nO wins: "+str(O_wins)+"\nTies: "+str(Ties))
print("Percents:\nX: "+"{:.3f}".format(X_wins / sims * 100)+"\nO: "+"{:.3f}".format(O_wins / sims * 100)+"\nTies: "+"{:.3f}".format(Ties / sims * 100))
input("Press Enter to close")
