import player
import time

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] #The 3x3 board
        self.current_winner = None #Who the winner is of this game

    def print_board(self):
        #For each row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc
        numboard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numboard:
            print(' | ' + ' | '.join(row) + ' |')
        
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board): # ['x','x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
            if spot == ' ':
                moves.append(i)

        return moves #This just gives all the empty spots in the board as available moves
        
    def empty_squares(self):
        return ' ' in self.board
        
    def num_empty_squares(self):
        return self.board.count(' ')
        
    def make_move(self,square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
        
    def winner(self, square, letter):
        #Winner is 3 in any column,row, diagonal
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
            
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True
            
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
        

def play(game, xplayer, oplayer, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #Starting letter
    #Iterate while game has empty squares. We dont stop until all squares are filled
    
    while game.empty_squares():
        if letter == 'O':
            square = oplayer.get_move(game)
        else:
            square = xplayer.get_move(game)

        #Make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.8)

            
    if print_game:
        print("It is a tie!")
        

if __name__ == '__main__':
    xplayer = player.HumanPlayer('X')
    oplayer = player.RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, xplayer,oplayer, print_game=True)

        


