import math
from queue import PriorityQueue
import dialogBox
import main
import pygame
import mainSearch


def _dAlgorithm(draw,grid,start,end):
    count=0
    found=False
    flag=False
    originatedFrom = {}
    set=PriorityQueue()
    set.put((0,count,start))
    dist={spt: float("inf") for row in grid for spt in row}
    dist[start]=0
    visited={start}
    
    while not set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current=set.get()[2]

        if current==end:
            temp=current
            while temp.prev:
                originatedFrom.append(temp.prev)
                temp=temp.prev
            if not flag:
                flag=True
                found=True
                main.__reconstructPath(originatedFrom, end, draw)
                dialogBox._dialogBox("Path Found")

            elif flag:
                continue

        if flag==False:
            for neighbour in current.neighbours:
                temp_dist=dist[start]+1
                if temp_dist < dist[neighbour]:
                    dist[neighbour]=temp_dist
                    originatedFrom[neighbour] = current
                    if neighbour not in visited:
                        count+=1
                        visited.add(neighbour)
                        set.put((dist[neighbour],count,neighbour))
                        neighbour.makeVisited()
            draw()
            if current != start:
                current.makeNotVisited()
    if not found:
        dialogBox._dialogBox("Path Not Found")
        return False