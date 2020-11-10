# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:24:30 2020

@author: straw
"""
import random 

cell_width = 40
x = 0
y = 0

grid = [] 
stack_list = []
closed_list = []

path = {}
def Maze(x, y):
    stack_list.append((x,y))
    closed_list.append((x,y))
    

    while len(stack_list) > 0:
        cell = []

        if(x + cell_width, y) not in closed_list and (x + cell_width, y) in grid:
            cell.append("East")

        if (x - cell_width, y) not in closed_list and (x - cell_width, y) in grid:
            cell.append("West")

        if (x , y + cell_width) not in closed_list and (x , y + cell_width) in grid:
            cell.append("South")

        if (x, y - cell_width) not in closed_list and (x , y - cell_width) in grid:
            cell.append("North") 

        if len(cell) > 0:
            current_cell = (random.choice(cell))

            if current_cell == "East":
                path[(x + cell_width, y)] = x, y
                x = x + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "West":
                path[(x - cell_width, y)] = x, y
                x = x - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "North":
                path[(x , y - cell_width)] = x, y
                y = y - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "South":
                path[(x , y + cell_width)] = x, y
                y = y + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

        else:
            x, y = stack_list.pop()

def path_tracer(x, y):
    while (x, y) != (40, 40):
        x, y = path[x, y]
        

x, y = 40, 40
Maze(x, y)
path_tracer(400, 400)

        
        
