# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:13:29 2020

@author: straw
"""
import random
import numpy as np
from itertools import chain
from itertools import groupby

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.walls =  {'N': True, 'S': True, 'E': True, 'W': True}
        self.excluded = False
        
    def spread_value(self, next_cell):
        v = min(self.value, next_cell.value)
        next_cell.value = v
        self.value = v
        
    def break_wall(self, next_cell, wall):
        wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[wall] = False
        next_cell.walls[wall_pairs[wall]] = False
        
    def exclude_cell(self):
        self.excluded = True

class Maze:
    def __init__(self, size=3):
        self.size = size
        self.board = self.create_board()
        #self.placements = []
        self.bag = []
        # self.halls = {
        #                 'value' : [i for i in range(self.size*self.size)],
        #                 'cell': [[None]]*self.size*self.size
        #               }
        
    def __str__(self):
        maze_rows = ['-' *((self.size*2)+1)]
        for y in range(self.size):
            maze_row = ['|']
            for x in range(self.size):
                if self.board[x][y].walls['E']:
                    maze_row.append('{}|'.format(self.get_cell(x, y).value))
                else:
                    maze_row.append('{} '.format(self.get_cell(x, y).value))
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.size):
                if self.board[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        
        maze_rows[1] = maze_rows[1].replace('|', ' ', 1)
        
        return '\n'.join(maze_rows)
    
    def create_board(self):     
        board = [[Cell(i,j) for j in range(0, self.size)] for i in range(0, self.size)]
        v = 0
        for cells in board:
            for c in cells:
                c.value = v
                v = v + 1
        return board
    
    # def update_halls(self):
    #     placements = []
    #     for cells in self.board:
    #         for c in cells:
    #             placements.append((c, c.value))
    #     self.placements = placements
        
    def same_value_cells(self, value):
        hall = []
        for cells in self.board:
            for c in cells:
                if c.value == value:
                    hall.append(c)
        return hall
    
    def get_cell(self, x, y):
        return self.board[x][y]
        
    def all_equal(self):
        values = []
        for cells in self.board:
            for c in cells:
                values.append(c.value)
        g = groupby(values)
        return next(g, True) and not next(g, False)
    
    def get_neighbours(self, cell):
        t_vector = [('W', (-1, 0)),
                   ('E', (1, 0)),
                   ('S', (0, 1)),
                   ('N', (0, -1))]
        neighbours = []
        for wall, (tx, ty) in t_vector:
            n_x, n_y = cell.x + tx, cell.y + ty
            if (n_x >= 0 and n_x < self.size) and (n_y >= 0 and n_y < self.size):
                neighbour = self.get_cell(n_x, n_y)
                if neighbour.value != cell.value:
                    hall = self.same_value_cells(neighbour.value)
                    neighbours.append((wall, neighbour, hall))
        return neighbours
        
    def build_with_Kruskal(self):
        while not self.all_equal():
            current_cell = random.choice([c for c in list(chain(*self.board)) if c not in self.bag])
            neighbours = self.get_neighbours(current_cell)
            if not neighbours:
                current_cell.exclude_cell()
                self.bag.append(current_cell)    
            else:
                #print(self.placements)
                print(self.__str__())
                input()
                wall, next_cell, hall = random.choice(neighbours)
                current_cell.break_wall(next_cell, wall)
                current_cell.spread_value(next_cell)
                for c in hall:
                    print((c.x, c.y), c.value)
                    c.value = next_cell.value
                    
maze = Maze(3)
maze.build_with_Kruskal()
print(maze)

