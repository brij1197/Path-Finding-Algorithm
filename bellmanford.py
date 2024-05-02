import pygame
import dialogBox
import main

def __bellmanFordAlgorithm(draw, grid, start,end):
    dist = {node: float('inf') for row in grid for node in row}
    dist[start] = 0
    originatedFrom = {}

    num_nodes = len(grid) * len(grid[0])  # Total number of nodes

    for _ in range(num_nodes - 1):
        for row in grid:
            for node in row:
                if dist[node] != float('inf'):
                    for neighbour in node.neighbours:
                        if dist[node] + 1 < dist[neighbour]:  # Assuming edge weight is 1
                            dist[neighbour] = dist[node] + 1
                            originatedFrom[neighbour] = node
                            neighbour.makeVisited()
                            draw()

    for row in grid:
        for node in row:
            if dist[node] != float('inf'):
                for neighbour in node.neighbours:
                    if dist[node] + 1 < dist[neighbour]:
                        dialogBox._dialogBox("Graph contains negative weight cycle")
                        return False

    if dist[end] != float('inf'):
        main.__reconstructPath(originatedFrom, end, draw)
        dialogBox._dialogBox("Path Found")
        return True

    dialogBox._dialogBox("No negative weight cycle")
    return True

