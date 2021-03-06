# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:26:54 2020

@author: straw
"""
import random
import time
import winsound

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
    def __init__(self):
        self.size = int(input('Number of maze\'s hallways ? '))
        self.filename = input('Maze\'s name ? ')
        self.entrance = (0,0)
        self.maze = [[Cell((i,j)) for j in range(0, self.size)] for i in range(0, self.size)]
        
    def __str__(self):
        maze_rows = ['-' *((self.size*2)+1)]
        for y in range(self.size):
            maze_row = ['|']
            for x in range(self.size):
                if self.maze[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.size):
                if self.maze[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        
        maze_rows[1] = maze_rows[1].replace('|', ' ', 1)
        return '\n'.join(maze_rows)

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
        t_vector = [('W', (-1, 0)),
                  ('E', (1, 0)),
                  ('S', (0, 1)),
                  ('N', (0, -1))]
        neighbours = []
        for wall, (tx, ty) in t_vector:
            n_x, n_y = cell.position[0] + tx, cell.position[1] + ty
            if (n_x >= 0 and n_x < self.size) and (n_y >= 0 and n_y < self.size):
                neighbour = self.get_cell((n_x, n_y))
                if neighbour.has_all_walls():
                    neighbours.append((wall, neighbour))
        return neighbours
    
    def build_with_RBT(self):
        """

        Returns
        -------
        None.

        """
        current_cell = self.get_cell(self.entrance)
        stack = []
        visited = 1
        while visited < self.size*self.size:
            neighbours = self.get_neighbours(current_cell)
            if not neighbours:
                current_cell = stack.pop()
                continue
            wall, next_cell = random.choice(neighbours)
            current_cell.break_wall(next_cell, wall)
            stack.append(current_cell)
            current_cell = next_cell
            visited = visited + 1
            
    def save_file(self):
        file = open('{}.txt'.format(self.filename), 'w')	
        file.write(self.__str__())
        file.close()


if __name__ == '__main__':
    maze = Maze()
    print(maze)
    start_time = time.time()
    maze.build_with_RBT()
    end_time = time.time()
    time = end_time - start_time
    print("Generating this maze took %s seconds." % (time))
    winsound.Beep(320,700)
    print(maze)
    maze.save_file()


