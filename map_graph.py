from queue import PriorityQueue
import numpy as np
import matplotlib.pyplot as plt
import car_utils

class MapGraph:
    def __init__(self, mapping):
        self.edges: dict[tuple, list[tuple]] = {}
        self.mapping = mapping
        minX = 0
        maxX = np.size(self.mapping, 0)
        minY = 0
        maxY = np.size(self.mapping, 1)
        for i in range(maxX):
            for j in range(maxY):
                curr = (i, j)
                left = (i - 1, j)
                right = (i + 1, j)
                up = (i, j + 1)
                down = (i, j - 1)
                if (mapping[i][j] == 1):
                    continue
                elif i == minX and j == minY:
                    self.addEdges(curr, [right, up])
                elif i == minX and j == maxY - 1:
                    self.addEdges(curr, [right, down])
                elif i == maxX - 1 and j == minY:
                    self.addEdges(curr, [left, up])
                elif i == maxX - 1 and j == maxY - 1:
                    self.addEdges(curr, [left, down])
                elif i == minX:
                    self.addEdges(curr, [up, down, right])
                elif i == maxX - 1:
                    self.addEdges(curr, [up, down, left])
                elif j == minY:
                    self.addEdges(curr, [left, right, up])
                elif j == maxY - 1:
                    self.addEdges(curr, [left, right, down])
                elif i > 0 and i < maxX and j > 0 and j < maxY:
                    self.addEdges(curr, [left, right, up, down])

    def addEdges(self, curr, edges) -> None:
        self.edges[curr] = []
        for i in edges:
            if not self.mapping[i[0]][i[1]]:
                self.edges[curr].append(i)
                
    def neighbors(self, id: tuple) -> list[tuple]:
        return self.edges[id]
    
    def a_star(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            # keep changing goal's relative position... or find the goal with the closes euclidean distance to the destination... 
        
            # how to determine current goal node: do a line from start to goal and whichever is furthest on line and still within 100 x 100 is the goal node...
            if current == goal:
                break
    
            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + car_utils.manhattan(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        path = []
        while current != start: 
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()


        car_utils.plot_points(path, "Optimal Path from A* Search", np.size(self.mapping, 0) + 10, np.size(self.mapping, 1) + 10, True)
       
        return path