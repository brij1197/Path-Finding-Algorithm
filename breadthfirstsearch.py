import pygame
import dialogBox
import main
from collections import deque

def __breadthFirstSearch(draw, grid, start, end):
    queue = deque([start])
    visited = {node: False for row in grid for node in row}
    visited[start] = True
    originatedFrom = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            main.__reconstructPath(originatedFrom, end, draw)
            dialogBox._dialogBox("Path Found")
            return True

        for neighbour in current.neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                originatedFrom[neighbour] = current
                queue.append(neighbour)
                neighbour.makeVisited()
                draw()

        if current != start:
            current.makeNotVisited()

    dialogBox._dialogBox("Path Not Found")
    return False
