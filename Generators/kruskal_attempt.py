# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:13:29 2020

@author: straw
"""
import random
from itertools import chain
from itertools import groupby
import time
import winsound

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.walls =  {'N': True, 'S': True, 'E': True, 'W': True}
        self.excluded = False
                
    def break_wall(self, next_cell, wall):
        wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[wall] = False
        next_cell.walls[wall_pairs[wall]] = False
        
    def exclude_cell(self):
        self.excluded = True

class Maze:
    def __init__(self, size):
        self.size = int(input('Number of maze\'s hallways ? '))
        self.size = size
        self.max_wall = self.size**2-1
        self.filename = input('Maze\'s name ? ')
        self.board = self.create_board()
        
    def __str__(self):
        maze_rows = ['-' *((self.size*2)+1)]
        for y in range(self.size):
            maze_row = ['|']
            for x in range(self.size):
                if self.board[x][y].walls['E']:
                    maze_row.append('{}|'.format(self.board[x][y].value))
                else:
                    maze_row.append('{} '.format(self.board[x][y].value))
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
    
    def get_cell(self, x, y):
        return self.board[x][y]
        
    def all_equal(self):
        values = [self.board[i][j].value for j in range(0, self.size) for i in range(0, self.size)]
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
                    neighbours.append((wall, neighbour))
        return neighbours
    
    def same_value_cells(self, value):
        hall = []
        for cells in self.board:
            for c in cells:
                if c.value == value:
                    hall.append(c)
        return hall
    
    def spread_values(self, current_cell, next_cell):        
        if (current_cell.value < next_cell.value):
            spread = current_cell.value
            hall2 = self.same_value_cells(next_cell.value)
            next_cell.value = spread
            for c in hall2:
                c.value = spread
            del hall2
        else:
            spread = next_cell.value
            hall1 = self.same_value_cells(current_cell.value)
            current_cell.value = spread
            for c in hall1:
                c.value = spread
            del hall1
        
    def build_with_Kruskal(self):
        n = 0
        while n < self.max_wall :
            current_cell = random.choice([c for c in list(chain(*self.board)) if c.excluded == False])
            neighbours = self.get_neighbours(current_cell)
            if not neighbours:
                current_cell.exclude_cell()
            else:
                wall, next_cell = random.choice(neighbours)
                current_cell.break_wall(next_cell, wall)
                n = n + 1
                self.spread_values(current_cell, next_cell)
                
    def save_file(self):
        file = open('{}.txt'.format(self.filename), 'w')
        file.write(self.__str__())
        file.close()
 
if __name__ == '__main__':
    maze = Maze()
    start_time = time.time()
    maze.build_with_Kruskal()
    end_time = time.time()
    time = end_time - start_time
    print("Generating this maze took %s seconds." % (time))
    winsound.Beep(320, 700)
    print(maze)
    maze.save_file()




