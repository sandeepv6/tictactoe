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

class UnbeatableAIPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game,self.letter)['position']
            
        return square
    
    def minimax(self,state,player):
        max_player = self.letter #Player that is playing
        other_player = 'O' if player == 'X' else 'X'

        #First check if previous move is a winner, this is the base case of recursive case
        if state.current_winner == other_player:
            #Return position and score, need this in order to use the minmax algorithm
            return{'position': None,
                   'score': 1 *(state.num_empty_squares()+ 1) if other_player == max_player else (-1 * (state.num_empty_squares() + 1))
            }
        elif not state.empty_squares(): #If theres no empty squares left, game is drawn
            return {'position': None, 'score': 0}
        
        if player == max_player: 
            best = {'position':None, 'score': -math.inf} #Every iteration, should maximize this value, start from lowest possible -inf
        else:
            best = {'position':None, 'score': math.inf} #If Player isnt max player, than we want to minimize, so start from highest possible which is inf

        for move in state.available_moves():
            #Make a move and try the spot
            state.make_move(move, player)
            #Recurse using this algorithm to simulate the game after playing that move
            simscore = self.minimax(state,other_player) #Alternate players
            #Reset and undo the move
            state.board[move] = ' '
            state.current_winner = None
            simscore['position'] = move

            #Update the dictionary as needed
            if player == max_player: #Maximize for  the max player
                if simscore['score'] > best['score']:
                    best = simscore #Replace here
            else: #But minimize for the other
                if simscore['score'] < best['score']:
                    best = simscore #Replace here

        return best

   