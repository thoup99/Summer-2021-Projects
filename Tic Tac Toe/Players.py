import random

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

    def get_pinp(self, open_spots, num_open_spots, game_board):
        pass                  
