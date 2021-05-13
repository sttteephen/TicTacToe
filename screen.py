import pygame
from pygame.locals import *
from sys import exit
from board import Board
from player import Player

# setup constants
screenColour = (87,186,172)
lineColour = (50,50,50)
noughtsColour = (84,84,84)
crossColour = (241,235,213)
screenWidth = (500,550)
rectWidth = (95,95)

# represents a square on the screen
class BoardSquare:

    def __init__(self, rect, circlexy, crossxy, pos):
        self.rect = rect    # rectangle the square occupies on screen   
        self.circlexy = circlexy    # coordinate for drawing a cirlce in this square
        self.crossxy = crossxy  # coordinate for drawing a cross in this square
        self.pos = pos  # row and column position of square on board
        self.occupied = False   # true if a piece has been placed here

    # draws a cross in this square on screen 
    def drawCross(self, screen):
        pygame.draw.line(screen, crossColour, (self.crossxy), (self.crossxy[0]+95,self.crossxy[1]+95), width=10)
        pygame.draw.line(screen, crossColour, (self.crossxy[0]+95,self.crossxy[1]), (self.crossxy[0],self.crossxy[1]+95), width=10)
        self.occupied = True

    # draws a circle in this square on screen
    def drawCircle(self, screen):
        pygame.draw.circle(screen, noughtsColour, (self.circlexy), 50, width=5)
        self.occupied = True

# represents the screen display
class Display:

    def __init__(self):

        # setup the screen
        pygame.init()
        self.screen = pygame.display.set_mode(screenWidth)
        pygame.display.set_caption('Tic Tac Toe')

        self.dialougeBox = Rect((0,480),(500,80))
        self.font = pygame.font.SysFont('arial', 50)

        # create square objects
        self.square00 = BoardSquare(Rect((55,55),rectWidth), (100,100), (55,55), (0,0))
        self.square01 = BoardSquare(Rect((200,55),rectWidth), (250,100), (200,55), (0,1))
        self.square02 = BoardSquare(Rect((350,55),rectWidth), (400,100), (350,55), (0,2))
        self.square10 = BoardSquare(Rect((55,200),rectWidth), (100,250), (55,200), (1,0))
        self.square11 = BoardSquare(Rect((200,200),rectWidth), (250,250), (200,200), (1,1))
        self.square12 = BoardSquare(Rect((350,200),rectWidth), (400,250), (350,200), (1,2))
        self.square20 = BoardSquare(Rect((55,350),rectWidth), (100,400), (55,350), (2,0))
        self.square21 = BoardSquare(Rect((200,350),rectWidth), (250,400), (200,350), (2,1))
        self.square22 = BoardSquare(Rect((350,350),rectWidth), (400,400), (350,350), (2,2))

        # list of square objects
        self.squares = [ 
            self.square00, 
            self.square01, 
            self.square02,
            self.square10,
            self.square11,
            self.square12,
            self.square20,
            self.square21,
            self.square22,
            ]

    def resetSquares(self):
        for square in self.squares:
            square.occupied = False

    # clears the screen and draws board lines
    def screenSetup(self):
        self.screen.fill((87,186,172))
        # vertical lines
        pygame.draw.line(self.screen, lineColour, (170,40), (170,460), width=4)
        pygame.draw.line(self.screen, lineColour, (331,40), (331,460), width=4)
        # horizontal lines
        pygame.draw.line(self.screen, lineColour, (40,170), (460,170), width=4)
        pygame.draw.line(self.screen, lineColour, (40,331), (460,331), width=4)
        pygame.display.update()

    def updateDialouge(self, message, colour):
        self.screen.fill(screenColour, self.dialougeBox)
        message_surf = self.font.render(message, True, colour, None)
        self.screen.blit(message_surf, (185,480))

    def drawCircle(self, square):
        square.drawCircle(self.screen)

    def drawCross(self, square):
        square.drawCross(self.screen)

display = Display()
player1 = Player(1)
player2 = Player(2)
board = Board()


# creates a new game
running = True
while running:

    display.screenSetup()
    board = Board()
    currentPlayer = player1
    display.resetSquares()
    display.updateDialouge("O's Turn", noughtsColour)
    draw = False

    # main game loop
    game_over = False
    while not game_over:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()
                for square in display.squares:
                    
                    # check player has clicked in an unoccupied square
                    if square.rect.collidepoint((x,y)):
                        if not square.occupied:

                            display.drawCircle(square) if currentPlayer == player1 else display.drawCross(square)

                            #print(square.pos)
                            if board.dropPiece(currentPlayer.piece, square.pos):
                                game_over = True
                            
                            if board.checkDraw():
                                game_over = True
                                draw = True

                            if currentPlayer == player1:
                                display.updateDialouge("X's Turn", crossColour)
                                currentPlayer = player2 
                            else: 
                                display.updateDialouge("O's Turn", noughtsColour)
                                currentPlayer = player1

                        break


        pygame.display.update()

    if draw:
        display.updateDialouge("  Draw", lineColour)
    elif currentPlayer == player1:
        display.updateDialouge(" X Wins", crossColour)
    else: 
        display.updateDialouge(" O Wins", noughtsColour)
    pygame.display.update()
    
    paused = True
    while paused:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                paused = False
                break
