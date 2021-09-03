from Players import HumanPlayer, RandomPlayer, SmartishPlayer
from Game import Game

##can change X/O to Player from the Players.py file
game = Game(HumanPlayer("X") , SmartishPlayer("O"))

def play(): #Runs the whole game
    turn = "X"
    while (len(game.open_spots()) != 0):
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

if __name__ == "__main__":
    play()