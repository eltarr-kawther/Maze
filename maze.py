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

#class Maze:
    #def __init__(self, n):
        #self.n = n
        #self.maze = [[True]*(self.n*2+1)]*(self.n*2+1) 
        
    #def building_maze(self):
        #self.maze[0][0] = False
        #for i in range(0, len(self.maze)):
            #for j in range(0, len(self.maze)):
                #if i == 0 and j == 0:
                    #pass
                #else:
                    #print()
