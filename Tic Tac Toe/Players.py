import random
import math

class HumanPlayer():
    def __init__(self, letter):
        self.letter = letter
    

    def get_pinp(self, open_slots, null1, null2):
        while True:
            try:
                requested_slot = input("Please enter an available number: ")
                if requested_slot in open_slots:
                    return(self.letter, requested_slot)
            except: 
                pass
        
class RandomPlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_pinp(self, open_slots, null1, null2):
        return(self.letter, random.choice(open_slots))

    
class SmartPlayer():
    def __init__(self, letter):
        self.letter = letter

    def check_win_SP(self, game_board):
        ##Checks rows
        for row in game_board:
            if (row[0] == row[1] and row[0] == row[2]):
                return (row[0])
        ##Checks collumns
        for x in range(3):
            if (game_board[0][x] == game_board[1][x] and game_board[1][x] == game_board[2][x]):
                return(game_board[0][x])
        ##Checks diagonals
        if ((game_board[0][0] == game_board[1][1] and game_board[0][0] == game_board[2][2]) or (game_board[0][2] == game_board[1][1] and game_board[0][2] == game_board[2][0])):
            return(game_board[1][1])
        return("None")

    ##Returns the ammount of open spots
    def num_open_slots_SP(self, game_board):
        op_slots = 0
        for row in game_board:
            for col in row:
                if col in "123456789":
                    op_slots += 1
        return(op_slots)

    def replaceSP(self, num, letter, game_board):
        for ir, row in enumerate(game_board):
            for ic, col in enumerate(row):
                if col == num:
                    game_board[ir][ic] = letter

    def get_pinp(self, open_spots, num_open_spots, game_board):
        if (num_open_spots == 9):
            return([self.letter, "5"])
        else:
            to_take = self.minimax(game_board, self.letter, open_spots)
            return(to_take)

    def minimax(self, game_board, player, possible_moves):
        maxplayer = self.letter
        other_player = "O" if player == "X" else "X"

        if (self.check_win_SP(game_board) == other_player):
            return {"position": None, "score": 1 * (self.num_open_slots_SP(game_board)+ 1) if other_player == maxplayer else  -1 * (self.num_open_slots_SP + 1)} 
        elif (self.num_open_slots_SP(game_board) == 0):
            return {"position": None, "score": 0}

        if (player == maxplayer):
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}
        for possible_move in possible_moves:
            gb = game_board
            self.replaceSP(player, possible_move, gb)
            sim_score = self.minimax(gb, other_player, possible_moves)

            gb = self.replaceSP(possible_move, possible_move, gb)
            sim_score["position"] = possible_move

            if player == maxplayer:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return(best)                       