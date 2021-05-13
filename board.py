
# board class on which the players moves are made
class Board:

    def __init__(self):
        self.resetBoard()

    def __str__(self):
        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
        return ''
    
    # clear the board grid and set moves to one
    def resetBoard(self):
        self.grid = [[0 for i in range(3)] for j in range(3)]
        self.moves = 0

    # places a piece on the board
    def dropPiece(self, piece, position):
        self.grid[position[0]][position[1]] = piece
        self.moves += 1
        return self.checkWin(piece, position)

    # checks if there is a winning position
    def checkWin(self, piece, position):

        won = False

        # check row
        if self.grid[position[0]][0] == piece and self.grid[position[0]][1] == piece and self.grid[position[0]][2] == piece:
            #print('row ' + str(position[0]) + ' win')
            won = True  
        # check column
        elif self.grid[0][position[1]] == piece and self.grid[1][position[1]] == piece and self.grid[2][position[1]] == piece:
            #print('column ' + str(position[1]) + ' win')
            won = True  
        # check diagonals
        elif self.grid[1][1] == piece:
            # check right diagonal 
            if self.grid[0][2] == piece and self.grid[2][0] == piece:
                #print('right diagonal win')
                won = True  
            # check left diagonal
            elif self.grid[0][0] == piece and self.grid[2][2] == piece:
                #print('left diagonal win')
                won = True  
        
        return won

    def checkDraw(self):
        return True if self.moves == 9 else False

