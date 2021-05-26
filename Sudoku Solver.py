import numpy as np
grid = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
def validMove(grid,y,x,i):
    a,b = y//3*1, x//3*1
    for k in range(9):
        if grid[k][x] == i or grid[y][k] == i:
            return False 
        for j in range(9):
            if k//3*1 == a and j//3*1 == b:
                if grid[k][j] == i:
                    return False
    return True

def sudokuSolver(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for i in range(1,10):
                    if validMove(grid,y,x,i):
                        grid[y][x] = i
                        sudokuSolver(grid)
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

sudokuSolver(grid)





