# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:13:29 2020

@author: straw
"""
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.set_value = None
        self.walls =  {'N': True, 'S': True, 'E': True, 'W': True}
        
    def break_wall(self, next_cell, wall):
        wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[wall] = False
        next_cell.walls[wall_pairs[wall]] = False


class Maze:
    def __init__(self, size=3):
        self.size = size
        self.board = self.create_board()
        
    def create_board(self):     
        board = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                board.append(Cell(i,j))
        return board
            
        
    def build_with_Kruskal(self):
        return 0
