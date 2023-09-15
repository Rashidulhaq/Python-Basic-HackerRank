#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    n = len(grid)
    m = len(grid[0])

    # Define the neighbors' relative coordinates
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    dominant_count = 0

    for i in range(n):
        for j in range(m):
            current_cell_value = grid[i][j]
            is_dominant = True

            for dx, dy in neighbors:
                ni, nj = i + dx, j + dy

                if 0 <= ni < n and 0 <= nj < m:
                    neighbor_value = grid[ni][nj]

                    if neighbor_value >= current_cell_value:
                        is_dominant = False
                        break

            if is_dominant:
                dominant_count += 1

    return dominant_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
