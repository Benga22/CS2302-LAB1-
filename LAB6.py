# Course Name: CS2302
# Author: Olugbenga Iyiola ID:80638542
# Assignment 6
# Instructor: Olac Fuentes
# T.A.: Nath Anindita / Maliheh Zargaran
# Date of last modification: 04/12/2019
# Purpose of program: Binary Search Trees

# Importing packages needed for disjoint set forest
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# This method is used to draw a maze
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)
    plt.show()  # Displaying the the circles

# This method is used to create a list of lists
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

# This is method is used to count the number of sets.
def NumSets(S):
    Counter = 0
    for i in range(len(S)):
        if S[i] <0:  # Checking the number of roots i.e -1
            Counter +=1  # counting number of root
    return Counter

# This method is used check if 2 cells belong to the same set
def InSameSet(S,a,b):
    Pa =find(S,a)  # Finding the root of a
    Pb = find(S,b)  # Finding the root of b
    if Pa == Pb:  # checking if root of a is same as b
        return True
    else:
        return False

# simple find with recursion
def find(S, i):
    # Returns root of tree that i belongs to
    if S[i] < 0:
        return i
    return find(S, S[i])  # Recursive call to parent of i

# Find method with compression
def find_c(S,i):
    if S[i]<0:  # checking if cell is a root
        return i
    r = find_c(S, S[i])  # Recursive call to parent of i
    S[i] = r  # connecting each subsequent parents of i to the root
    return r

# This method is used to join two roots together
def union(S, i, j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S, i)  # finding root of i
    rj = find(S, j)  # finding root of j
    if ri != rj:  # Do nothing if i and j belong to the same set
        S[rj] = ri  # Make j's root point to i's root

# Joining smaller tree to root of larger tree
def union_by_size(S, i, j):
    ri = find_c(S, i)  # finding root of i
    rj = find_c(S, j)  # finding root of j
    if ri != rj:  # if i and j do not belong to the same set
        if S[ri]>S[rj]:  # Checking if the tree with root i is more than that of j
            S[rj]+=S[ri]
            S[ri]=rj  # pointing i to root j
        else:
            S[ri]+=S[rj]
            S[rj]=ri  # pointing j to root i

# This is method is used to create maze with simple paths using standard union
def BuildMazeUnionStd(Wall, S):
    while NumSets(S)>1:  # Checking if number of sets in maze more than 1
        rand = random.randint(0,len(Wall)-1)  # Creating a random number from 0 to last cell number
        if InSameSet(S, Wall[rand][0], Wall[rand][1])== False:  # checking if cells with random number are in same set
            union(S,Wall[rand][0], Wall[rand][1])  # uniting the cells if they are in different sets
            Wall.pop(rand)  # Removing the list from the maze
    return Wall

# This is method is used to create maze with simple paths using union-by-size
def BuildMazeUnionStd(Wall, S):
    while NumSets(S)>1:  # Checking if number of sets in maze more than 1
        rand = random.randint(0,len(Wall)-1)  # Creating a random number from 0 to last cell number
        if InSameSet(S, Wall[rand][0], Wall[rand][1])== False:  # checking if cells with random number are in same set
            union_by_size(S,Wall[rand][0], Wall[rand][1])  # uniting the cells if they are in different sets
            Wall.pop(rand)  # Removing the list from the maze
    return Wall


plt.close("all")

maze_rows = 15  # Number of rows in maze
maze_cols = 15  # Number of columns in maze

#  Calling of Methods to create Maze
walls = wall_list(maze_rows,maze_cols)  # Table with list of integers
S = np.zeros(maze_rows*maze_cols, dtype=np.int) - 1  # Disjoint set
print('Building maze using standard union')
start = time.perf_counter_ns()  # Start time of creating maze using standard union
newMaze = BuildMazeUnionStd(walls, S)  # Maze with simple path using standard union
end = time.perf_counter_ns()  # End time of creating maze using standard union
print('Running time for mace construction: ', end - start, ' nanoseconds')
draw_maze(newMaze,maze_rows,maze_cols)  # Displaying maze
print('*****************************************')
print('*****************************************')
walls2 = wall_list(maze_rows,maze_cols)  # Table with list of integers
S2 = np.zeros(maze_rows*maze_cols, dtype=np.int) - 1  # Disjoint set
print('Building maze using union-by-size')
start2 = time.perf_counter_ns()  # Start time of creating maze using union-by-size
newMaze2 = BuildMazeUnionStd(walls2, S2)  # Maze with simple path using union-by-size
end2 = time.perf_counter_ns()  # End time of creating maze using union-by-size
print('Running time for mace construction: ', end2 - start2, ' nanoseconds')
draw_maze(newMaze2,maze_rows,maze_cols)  # Displaying maze


