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
    
    def has_all_walls(self):
        """
        This function checks if a cell has all of it's walls.
        If a cell has at least one missing wall, return False.

        Returns
        -------
        bool
            has ALL ways.

        """
        if False not in self.walls.values():
            return True
        else:
            return False
        
    def break_wall(self, next_cell, wall):
        """
        Breaks wall between two cells. This function updates cells' walls status from 
        True (not broken) to False (broken)

        Parameters
        ----------
        next_cell : Cell object
            random cell's neighbour.
        wall : str
            which wall to break.

        Returns
        -------
        None.

        """
        wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[wall] = False
        next_cell.walls[wall_pairs[wall]] = False

class Maze:
    def __init__(self, n):
        self.size = n*2+1
        self.entrance = (0,0)
        self.maze = [[Cell((i,j)) for j in range(0,self.size)] for i in range(0, self.size)]

    def get_cell(self, position):
        """
        Get cell object from position

        Parameters
        ----------
        position : tuple
            position in maze.

        Returns
        -------
        Cell object
            cell in position.

        """
        return self.maze[position[0]][position[1]]
        
    def get_neighbours(self, cell):
        """
        

        Parameters
        ----------
        cell : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        t_vector = {'N':(-1, 0), 'S':(1, 0), 'E':(0, 1), 'W': (0, -1)}
        neighbours = []
        for wall in t_vector.keys():
            for (i, j) in t_vector.values():
                row, column = cell.position[0] + i, cell.position[1] + j
                if row >= 0 and row < self.size and column >= 0 and column < self.size:
                    neighbour = self.get_cell((row, column))
                    if neighbour.has_all_walls():
                        neighbours.append((wall, neighbour))
        if len(neighbours) > 0:
            return random.choice(neighbours)
        else:
            return None
    
    def build_with_RBT(self):
        """
        

        Returns
        -------
        None.

        """
        current_cell = self.get_cell(self.entrance)
        stack = []
        visited = 1
        while visited < self.size:
            wall, next_cell = self.get_neighbours(current_cell)
            if next_cell == None:
                current_cell = stack.pop()
            
            stack.append(current_cell)
            current_cell.break_wall(next_cell, wall)
            current_cell = next_cell
            visited = visited + 1

maze = Maze(3)
maze.build_with_RBT()


