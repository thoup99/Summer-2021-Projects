game_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

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

    def replace(self, letter_num): #Replaces the selected spot with a letter
        global game_board
        letter = letter_num[0]
        num = letter_num[1]
        for ir, row in enumerate(game_board):
            for ic, col in enumerate(row):
                if col == num:
                    game_board[ir][ic] = letter

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
            self.replace(self.x_player.get_pinp(op_slots, game_board))
        else:
            self.replace(self.o_player.get_pinp(op_slots, game_board))
