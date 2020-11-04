# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:50:26 2020

@author: straw
"""
import random

class Cell:
    def __init__(self, position):
        self.position = position
        self.walls =  {'N': True, 'S': True, 'E': True, 'W': True}
        self.wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    
    def has_all_walls(self):
        if False not in self.walls.values():
            return True
        else:
            return False
        
    def knock_down_wall(self, wall, next_cell):
        self.walls[wall] = False
        next_cell.walls[self.wall_pairs[wall]] = False

class Maze:
    def __init__(self, n):
        self.size = n*2+1
        self.entrance = (0,0)
        self.maze = [[Cell((i,j)) for j in range(0,self.size)] for i in range(0, self.size)]

    def get_cell(self, position):
        return self.maze[position[0]][position[1]]
        
    def get_neighbours(self, cell):
        vector = {'N':(-1, 0), 'S':(1, 0), 'E':(0, 1), 'W': (0, -1)}
        neighbours = []
        for wall in vector.keys():
            for (i, j) in vector.values():
                row, column = cell.position[0] + i, cell.position[1] + j
                if row >= 0 and row < self.size and column >= 0 and column < self.size:
                    neighbour = self.get_cell((row, column))
                    if neighbour.has_all_walls():
                        neighbours.append((wall, neighbour))
        if neighbours:
            next_cell = random.choice(neighbours)
            return next_cell
        else:
            return None
    
    def build_maze(self):
        current_cell = self.get_cell(self.entrance)


m = Maze(3)
next_cell = m.get_neighbours(m.maze[0][0])


