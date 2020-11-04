# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:50:26 2020

@author: straw
"""

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
        self.entry = (0,0)
        self.maze = [[Cell((i,j)) for j in range(0,self.size)] for i in range(0, self.size)]

    def find_cell(self, position):
        return self.maze[position[0]][position[1]]
        
    #def building_maze(self):
        #self.maze[0][0] = False
        #for i in range(0, len(self.maze)):
            #for j in range(0, len(self.maze)):
                #if i == 0 and j == 0:
                    #pass
                #else:
                    #print()

m = Maze(3)

