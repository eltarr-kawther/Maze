# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:50:26 2020

@author: straw
"""
class Maze:
    def __init__(self, n):
        self.n = n
        self.maze = [[True]*(self.n*2+1)]*(self.n*2+1) 
        
    def building_maze(self):
        self.maze[0][0] = False
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze)):
                if i == 0 and j == 0:
                    pass
                else:
                    print()
    
    def draw_maze(self):
        print(self.maze)
        
m = Maze(2)
m.draw_maze()
