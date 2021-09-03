import random
##Dont forget to import Player classes into the TicTacToe file 

class HumanPlayer():
    def __init__(self, letter):
        self.letter = letter
    

    def get_pinp(self, open_slots, game_board):
        while True:
            requested_slot = str(input("Please enter an available number: "))
            if (requested_slot == "Crash"):
                print(0 / 0)
            if requested_slot in open_slots:
                return(self.letter, requested_slot)
        
class RandomPlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_pinp(self, open_slots, game_board):
        return(self.letter, random.choice(open_slots))

class SmartishPlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_pinp(self, open_spots, game_board):
        result = self.check_winnable(open_spots, game_board, self.letter)
        if (result in "123456789"):
            return(self.letter, result)

        if (self.letter == "X"):
            result = self.check_winnable(open_spots, game_board, "O")
        else:
            result = self.check_winnable(open_spots, game_board, "X")

        if (result in "123456789"):
            return(self.letter, result)
        return(self.letter, random.choice(open_spots))

    def check_winnable(self, open_slots, gb, lt):
        letter = ""
        if (lt == "X"):
            letter = "X"
        else:
            letter = "O"
        for op_slot in open_slots:
            for ir, row in enumerate(gb):
                for ic, col in enumerate(row):
                    if col == op_slot:
                        gb[ir][ic] = letter
                        if (self.check_win_state(gb)):
                            gb[ir][ic] = op_slot
                            return(op_slot)
                        gb[ir][ic] = op_slot
        return("None")
        
    
    def check_win_state(self, game_board):
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

    
class BasePlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_pinp(self, open_spots, game_board): #Return(self.letter, chosen number)
        pass 