'''
Fill Sudoku

Input:
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
Output:
          3 1 6 5 7 8 4 9 2
          5 2 9 1 3 4 7 6 8
          4 8 7 6 2 9 5 3 1
          2 6 3 4 1 5 9 8 7
          9 7 4 8 6 3 1 2 5
          8 5 1 7 9 2 6 4 3
          1 3 8 9 4 7 2 5 6
          6 9 2 3 5 1 8 7 4
          7 4 5 2 8 6 3 1 9
Explanation: Each row, column and 3*3 box of 
the output matrix contains unique numbers.

Input:    
grid = [ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
         [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
         [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
         [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
         [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ];
Output:
           3 1 6 5 7 8 4 9 2 
           5 2 9 1 3 4 7 6 8 
           4 8 7 6 2 9 5 3 1 
           2 6 3 4 1 5 9 8 7 
           9 7 4 8 6 3 1 2 5 
           8 5 1 7 9 2 6 4 3 
           1 3 8 9 4 7 2 5 6 
           6 9 2 3 5 1 8 7 4 
           7 4 5 2 8 6 3 1 9 
Explanation: Each row, column and 3*3 box of 
the output matrix contains unique numbers.
'''
import math
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

n = len(grid)
box_length = int(math.sqrt(n))

rows = [[i for i in range(1,n+1)] for j in range(n)]
columns = [[i for i in range(1,n+1)] for j in range(n)]
missing_pos = []

# Missing element in each row and column
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0 :
            columns[j].remove(grid[i][j])
            rows[i].remove(grid[i][j])
        else:
            missing_pos.append((i,j))
# print(rows)
# print(columns)
# print(missing_pos)

def present_in_row(arr,row,data):
    for i in range(n):
        if arr[row][i] == data:
            return True
    return False

def present_in_column(arr,col,data):
    for i in range(n):
        if arr[i][col] == data:
            return True
    return False

def present_in_box(arr,row,col,data):
    for i in range(box_length):
        for j in range(box_length):
            if arr[row+i][col+j] == data:
                return True
    return False

def is_present(arr,row,col,data):
    if not present_in_row(arr,row,data) and not present_in_column(arr,col,data) and not present_in_box(arr,row-row%box_length,col-col%box_length,data):
        return False
    return True

def find_missing(arr,l):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def print_grid(arr):
    for i in range(n):
        if i % box_length == 0 and i != 0:
            print("-"*20)
        for j in range(n):
            if j % box_length == 0 and j != 0:
                print("| ",end="")
            print(arr[i][j],end=" ")
        print()


def solveSudoku(arr):
    l = [0,0]
    if not find_missing(arr,l):
        return True
    missing_data = set(rows[l[0]] + columns[l[1]])
    for data in missing_data:
        if not is_present(arr,l[0],l[1],data):
            arr[l[0]][l[1]] = data
            if solveSudoku(arr):
                return True
            arr[l[0]][l[1]] = 0
    return False
print("The Unsolved Sudoku grid:")
print_grid(grid)
print("-"*25)
print("The Solved Sudoku grid:")
if solveSudoku(grid):
    print_grid(grid)
else:
    print("No solution for the Sudoku")