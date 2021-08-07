from Players import HumanPlayer, RandomPlayer, SmartPlayer

game_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def replace(letter_num): #Replaces the selected spot with a letter
    letter = letter_num[0]
    num = letter_num[1]
    for ir, row in enumerate(game_board):
        for ic, col in enumerate(row):
            if col == num:
                game_board[ir][ic] = letter

def num_open_slots(): #Finds out how many playable spots there are
    op_slots = 0
    for row in game_board:
        for col in row:
            if col in "123456789":
                op_slots += 1
    return(op_slots)

    

class Game():
    def __init__(self, x_player, o_player):
        self.x_player = x_player
        self.o_player = o_player


    def draw_board(self):
        i = 0
        it = 0 
        while i < 5:
            to_draw = ""       
            if (i % 2 == 0):
                for x in range(3):
                    to_draw = to_draw + " "+game_board[it][x] + " |"
                it += 1
                print(to_draw)
            else:
                print("---+---+---")
            i += 1

    def check_win(self):
        ##Checks rows
        for row in game_board:
            if all(x == row[0] for x in row):
                return (True)
        ##Checks collumns
        for x in range(3):
            if (game_board[0][x] == game_board[1][x] and game_board[1][x] == game_board[2][x]):
                return(True)
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

    ## gets the input from whichever class is the X/O player
    def get_inp(self, letter, op_slots):
        if (letter == "X"):
            replace(self.x_player.get_pinp(op_slots, num_open_slots(), game_board))
        else:
            replace(self.o_player.get_pinp(op_slots, num_open_slots(), game_board))

##can change X/O to HumanPlayer, RandomPlayer, or SmartPlayer
game = Game(RandomPlayer("X") , RandomPlayer("O"))

def play(): #Runs the whole game.Can be run with simulations in this way
    turn = "X"
    while (num_open_slots() != 0):
        game.draw_board()
        print("It is "+turn+"'s turn!")
        game.get_inp(turn, game.open_spots())
        if game.check_win() == True:
            game.draw_board()
            print(turn+" Won the Game!")
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    if (game.check_win() == False):
        game.draw_board()
        print("The game ended in a tie!")

play()