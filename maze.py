# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:50:26 2020

@author: straw
"""
import random
import numpy as np

class Cell:
    def __init__(self, position):
        self.position = position
        self.walls =  {'N': True, 'S': True, 'E': True, 'W': True}
    
    def  __str__(self):
        return self.display
        
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
        #self.filename = input('Maze\'s name ? ')
        self.entrance = (0,0)
        self.maze = [[Cell((i,j)) for j in range(0,self.size)] for i in range(0, self.size)]
        
    def link(self, x, y):     
        if x % 2 == 0:
            x = x//self.size
        else:
            x = round(x/self.size)
        if y % 2 == 0:
            y = y//self.size
        else:
            y = round(y/self.size)
        return x, y
    
        # M[i + 1][j] = self.maze[x][y]
            # for j in range(0, (self.size)*2, 2):
            #     if i != 0 and i%2 != 0: 
            #         #print(i, j+2)
            #         x, y = self.link(i, j+2)
            #         print(i,j+2,'--->',x,y)
            #         if self.maze[x][y].walls['E']:
            #             M[i][j] = M[i][j] + 1
            #         l.append((i,j+2))
                    
            # for j in range(1, (self.size)*2, 2):
            #     if i != 0 and i%2 == 0:
            #         #print(i, j)
            #         x, y = self.link(i, j)
            #         print(i,j,'--->',x,y)
            #         l.append((i,j))

        #  if i == 0:
        #         print('.'+'#'*((self.size)*2))
            
        # if i == self.size*2:
        #     print('#'*((self.size)*2)+'.')        
    
    def initmatrice(self):
        M = []
        fulls = (self.size * 2)
        for i in range(0, fulls):
             M.append([])
             for j in range(0, fulls):
                 M[i].append(0)
        return (M)
    
    def draw2(self):
        M = np.zeros((self.size*2+1,self.size*2+1), dtype=int).astype(str)
        for i in range(0, self.size*2+1):
            if i == 0:
                M[i][:] = ['.']+['#']*(self.size*2)
            else:
                for j in range(0, self.size*2, 2):
                    if i % 2 == 0 and i != 0:
                        print(i, j+2)
                        x, y = self.link(i, j+2)
                        print(i,j+2,'--->',x,y)
                        if self.maze[x][y].walls['E']:
                             M[i][j] = '#'
                        # else:
                        #     M[i][j] = '.'
                        # if self.maze[x][y].walls['S']: 
                        #     M[i][j] = '#'
                        # else:
                        #     M[i][j] = '.'
                            
        for m in M:
            print(m)
        
    def temp(self):
        M = self.initmatrice()
        for i in range(0, self.size):
            for j in range(0, (self.size)):
                x = i * 2
                y = j * 2
                M[x][y] = '.'
                M[x + 1][y] = self.maze[i][j].walls['E']
                M[x][y + 1] = self.maze[i][j].walls['S']
                M[x + 1][y + 1] = True
        
        for m in M:
            print(m)
            
        #M = [[0]*((self.size*2)+1)]*((self.size*2)+1)                 
        #for j in range(0, self.size*2+1):       
            #for i in range(0, self.size*2+1):
                #if i == 0:
                    #print('.#'*((self.size)+1))
                #if i % 2 == 0 and i != 0:
                    #print('#'+'.#'*self.size)
                #if i % 2 != 0 and i != 0:
                    #x, y = self.link(i, j)
                    #print(i,j,'---->',x,y)
                    #print(M)
                    #print()
                    #if self.maze[x][y].walls['E']:
                        #M[i][j] = M[i][j] + 1
                    #if self.maze[x][y].walls['S']:
                        #M[i][j] = M[i][j] + 1
                #else:
                    #print('#'*((self.size*2)+1))       
                    
    def draw(self):
        M = []
        for i in range(0, self.size*2+1):
            if i == 0:
                #print('.'+'.'+'#'*(((self.size)*2)-1))
                M.append(list('.'+'.'+'#'*(((self.size)*2)-1)))
            if i % 2 == 0 and i!=0 and i != self.size*2:
                #print('#'*((self.size*2)+1))
                M.append(list('#'*((self.size*2)+1)))
            if i % 2 != 0 and i!=0:
                #print('#'+'.#'*self.size)
                M.append(list('#'+'.#'*self.size))
            if i == self.size*2-1:
                #print('#'*(((self.size)*2)-1)+'.'+'.') 
                M.append(list('#'*(((self.size)*2)-1)+'.'+'.'))
        
        # for m in M:
        #     print(m)
            
        return M
    
    def update(self):
        M = self.draw()
        for i in range(0, self.size):
            for j in range(0, (self.size)):
                x = i * 2
                y = j * 2
                M[x][y+1] = self.maze[i][j].walls['E']
                M[x+1][y] = self.maze[i][j].walls['S']
                #M[x-1][y] = self.maze[i][j].walls['N']
                #M[x][y-1] = self.maze[i][j].walls['W']
    
        # for m in M:
        #     for e in m:
        #         if e == True:
        #             e = '#'
        #         else:
        #             e = '.'
        
        for m in M:
            print(m)
        
                
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

maze = Maze()
maze.temp()
#maze.build_with_RBT()
#maze.update()
#maze.draw()

