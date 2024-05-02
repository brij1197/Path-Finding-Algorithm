import pygame
import math
from queue import PriorityQueue
import astar
import mainSearch
import dialogBox
import dijkstra
import argparse
import bellmanford
import breadthfirstsearch

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

parser=argparse.ArgumentParser(description="To Implement Path Finding Algorithm")
parser.add_argument('-o','--option',type=str,required=True,help="Algorithm")
args=parser.parse_args()

# Width and height of the window is going to be that of a square
width = 800
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("Path Finding Algorithm")

def __reconstructPath(cameFrom,current,draw):
    while current in cameFrom:
        if current is None:
            print("Error: Attempted to access a None node in path reconstruction.")
            break
        current.makePath()
        draw()
        current=cameFrom[current]

def makeGrid(rows, width):
    grid = []
    gap = width//rows  # to get width of the cube
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            search = mainSearch.Search(i, j, gap, rows)
            grid[i].append(search)
    return grid


def drawGrid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, Grey, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, Grey, (j*gap, 0), (j*gap, width))


def draw(win, grid, rows, width):  # To draw everything
    win.fill(White)
    # Redrawing everything every frame

    for row in grid:
        for spot in row:
            spot.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()


def getClickedPos(mousepos, rows, width):
    gap = width//rows
    y, x = mousepos

    row = y//gap
    col = x//gap

    return (row, col)


def main(win, width):
    rows = 50
    grid = makeGrid(rows, width)

    start = None
    end = None
    run = True

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                (row, col) = getClickedPos(pos, rows, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.makeStart()
                elif not end and spot != start:
                    end = spot
                    end.makeEnd()

                elif spot != end and spot != start:
                    spot.makeBlockade()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                (row, col) = getClickedPos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    start=None
                    end=None
                    grid=makeGrid(rows,width)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.updateNeighbours(grid)

                    if args.option.lower()=="dijkstra":
                        dijkstra._dAlgorithm(lambda: draw(win, grid, rows, width), grid, start, end)
                    elif args.option.lower()=="astar":
                        astar.__aAlgorithm(lambda: draw(win, grid, rows, width), grid, start, end)                                    
                    elif args.option.lower()=="bellman":
                        bellmanford.__bellmanFordAlgorithm(lambda: draw(win, grid, rows, width), grid, start, end)                                    
                    elif args.option.lower()=="bfs":
                        breadthfirstsearch.__breadthFirstSearch(lambda: draw(win, grid, rows, width), grid, start, end)                                    
                    else:
                        exit(0)
    
    pygame.quit()

if __name__ == "__main__":
    main(win, width)