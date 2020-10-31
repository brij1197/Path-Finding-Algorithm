import pygame

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (128, 128, 128)
Aqua = (0, 255, 255)
Purple = (128, 0, 128)
Orange = (255, 165, 0)

visited=[]

class Search:
    def __init__(self, row=0, col=0, width=0, all_rows=0,prev=0):
        self.width = width
        self.x = row*width
        self.y = col*width
        self.row = row
        self.prev=prev
        self.col = col
        self.visited=False
        self.all_rows = all_rows
        self.color = White  # All cubes will be white at starting
        self.neighbours = []

    def get_pos(self):
        return self.row, self.col

    def isReset(self):
        return self.color == White

    def isStart(self):
        return self.color == Aqua

    def isEnd(self):
        return self.color == Orange

    def isVisited(self):
        return self.color == Red

    def isNotVisited(self):
        return self.color == Green

    def isBlockade(self):
        return self.color == Black

    def reset(self):
        self.color = White

    def makeVisited(self):
        self.color = Red

    def makeNotVisited(self):
        self.color = Green

    def makePath(self):
        self.color = Purple

    def makeStart(self):
        self.color = Aqua

    def makeEnd(self):
        self.color = Orange

    def makeBlockade(self):
        self.color = Black

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbours(self, grid):
        self.neighbours = []
        # To go down a row
        if self.row < self.all_rows-1 and not grid[self.row+1][self.col].isBlockade():
            self.neighbours.append(grid[self.row+1][self.col])
        # To go up a row
        if self.row > 0 and not grid[self.row-1][self.col].isBlockade():
            self.neighbours.append(grid[self.row-1][self.col])
        # To go left
        if self.col > 0 and not grid[self.row][self.col-1].isBlockade():
            self.neighbours.append(grid[self.row][self.col-1])
        # To go right
        if self.col < self.all_rows-1 and not grid[self.row][self.col+1].isBlockade():
            self.neighbours.append(grid[self.row][self.col+1])

    def __lt__(self, other):
        return False
