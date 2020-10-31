import math
from queue import PriorityQueue
import dialogBox
import main
import pygame
import mainSearch


def heurestic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2)+abs(y1-y2)


def __aAlgorithm(draw, grid, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    originatedFrom = {}
    g_score = {point: float("inf") for row in grid for point in row}
    g_score[start] = 0
    f_score = {point: float("inf") for row in grid for point in row}
    f_score[start] = heurestic(start.get_pos(), end.get_pos())
    openSet_hash = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # openset will store f-score,count and node and we just require the node
        current = openSet.get()[2]
        openSet_hash.remove(current)

        if current == end:
            main.__reconstructPath(originatedFrom, end, draw)
            dialogBox._dialogBox("Path Found")
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current]+1
            if temp_g_score < g_score[neighbour]:
                originatedFrom[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + \
                    heurestic(neighbour.get_pos(), end.get_pos())
                if neighbour not in openSet_hash:
                    count += 1
                    openSet.put((f_score[neighbour], count, neighbour))
                    openSet_hash.add(neighbour)
                    neighbour.makeVisited()
        draw()
        if current != start:
            current.makeNotVisited()
    dialogBox._dialogBox("Path Not Found")
    return False
