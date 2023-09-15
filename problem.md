
# 2. Python: Dominant Cells <br>
There is a given list of lists of integers that represent a 2-dimensional grid with n rows and m columns. A cell is called a dominant cell if
it has a strictly greater value than all of its neighbors. Two cells are neighbors when they share a common side or a common corner, so a cell can have up to 8 neighbors. Find the number of dominant cells in the grid.   <br>
## Function Description  <br>
Modify submissionum cells in the editor below.     <br>
numCells has the following parameter(s):    <br>
int grid[n][m]: a 2-dimensional array of integers   <br>
Returns   <br>
int: the number of dominant cells in the grid   <br>
Constraints   <br>
• 1 ≤ n, m≤ 500   <br>
• There are at least 2 cells in the grid.   <br>
• 1 ≤ grid[i][j]≤ 100   <br>
﻿

▾ Input Format Format for Custom Testing   <br>
Input from stdin will be processed as follows and passed to the function.
The first line contains an integer n, the number of rows in the grid.
The second line contains an integer m, the number of columns in the grid.
Next, n lines follow. The i-th of them contains m integers denoting the cells in the i-th row of the grid.

   <br>
   ▼ Sample Case 0   <br>
Sample Input 0   <br>
STDIN  Function    <br>
3→n = 3    <br>
3→m = 3    <br>
1 2 7 → grid = [[1, 2, 7], [4, 5, 6], [8, 8, 9]]   <br>
4 5 6     <br>
8 8 9   <br>

Sample Output 0   <br>
2   <br>
Explanation 0   <br>
There are 3 cells that have strictly greater values than all their neighboring cells. These cells are:   <br>
⚫ the bottom right value, 9, with neighbors of 5, 6 and 8   <br>
⚫ the top right value, 7, with neighbors of 2, 5 and 6   <br>
Notice that the 8 at bottom left is not a dominant cell. It is not strictly greater than the cell to its right with a value of 8.
﻿   <br>

▼ Sample Case 1   <br>
Sample Input 1   <br>
1   <br>
4   <br>
1 2 2 1   <br>
Sample Output 1   <br>
Ө   <br>
Explanation 1   <br>
None of the cells is a dominant cell as each one has one neighbor with a greater or equal value.   <br>
▼ Sample Case 2   <br>
Sample Input 2   <br>
4   <br>
3   <br>
9 1 1   <br>
1 1 9   <br>
9 1 1   <br>
1 1 9   <br>
Sample Output 2   <br>
4   <br>
Explanation 2   <br>
All cells with a value of 9 are dominant. Notice that for each of these cells, all its neighboring cells have value 1 which is strictly smaller than 9. None of the cells with value 1 is a dominant cell.
