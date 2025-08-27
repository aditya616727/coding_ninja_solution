## Set Matrix Zeros

### Problem Statement
You are given an N x M integer matrix. Your task is to modify this matrix in place so that if any cell contains the value 0, then all cells in the same row and column as that cell should also be set to 0.

#### Requirements:
- If a cell in the matrix has the value 0, set all other cells in that cell's row and column to 0.
- You should perform this modification in place (without using additional matrices).
- You must do it in place.

---

### Input Format
- The first line contains an integer T, the number of test cases.
- For each test case:
	- The first line contains two integers N and M, the number of rows and columns.
	- The next N lines each contain M integers, representing the matrix.

### Output Format
- For each test case, print the modified matrix, with each row on a new line and elements separated by spaces.

---

### Sample Input 1
```
2
2 3
7 19 3
4 21 0
3 3
1 2 3
4 0 6
7 8 9
```

### Sample Output 1
```
7 19 0
0 0 0
1 0 3
0 0 0
7 0 9
```

#### Explanation
For the first case, the cell (2,3) is zero, so the entire 2nd row and 3rd column are set to zero.
For the second case, the cell (2,2) is zero, so the entire 2nd row and 2nd column are set to zero.

---

### Sample Input 2
```
2
4 2
1 0
2 7
3 0
4 8
3 3
0 2 3
1 0 3
1 2 0
```

### Sample Output 2
```
0 0
2 0
0 0
4 0
0 0 0
0 0 0
0 0 0
```

---
