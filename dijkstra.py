import pygame
import dialogBox
import main
from queue import PriorityQueue

def _dAlgorithm(draw, grid, start, end):
    count = 0
    originatedFrom = {}
    pq = PriorityQueue()
    pq.put((0, count, start))
    dist = {node: float("inf") for row in grid for node in row}
    dist[start] = 0
    visited = set([start])

    while not pq.empty():
        current_distance, _, current = pq.get()

        if current in visited and current != start:
            continue

        visited.add(current)
        
        if current == end:
            main.__reconstructPath(originatedFrom, end, draw)
            dialogBox._dialogBox("Path Found")
            return True

        for neighbour in current.neighbours:
            temp_dist = current_distance + 1  # Assuming edge weight is 1
            if temp_dist < dist[neighbour]:
                dist[neighbour] = temp_dist
                originatedFrom[neighbour] = current
                pq.put((temp_dist, count, neighbour))
                neighbour.makeVisited()
                count += 1
        draw()

        if current != start:
            current.makeNotVisited()

    dialogBox._dialogBox("Path Not Found")
    return False
