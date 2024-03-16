import math
import random

class Player:
    def __init__(self, letter ) -> None:
        #Letter is x or o for this player
        self.letter = letter
        
    #WAnt players to get their next move in the game
    
    def get_move(self, game):
        
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + 's turn. Input move (0 - 8):')
            #Checkj that this is a correc tvalue by casting to integer, and if not then say its invalid, also if its not available spot, then we dont allow the input
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val