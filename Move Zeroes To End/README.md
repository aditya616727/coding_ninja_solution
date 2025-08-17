
# Move Zeroes To End

## Problem Statement

Given an unsorted array of integers, move all zeroes to the end of the array while maintaining the order of non-zero elements. The operation should be performed in-place with O(n) time complexity and O(1) space complexity.

### Example

**Input:**  
`[0, 1, -2, 3, 4, 0, 5, -27, 9, 0]`

**Output:**  
`[1, -2, 3, 4, 5, -27, 9, 0, 0, 0]`

---

## Input/Output Format

- The first line contains an integer `T`, the number of test cases.
- For each test case:
	- The first line contains an integer `N`, the size of the array.
	- The second line contains `N` space-separated integers (the array elements).

### Sample Input 1

```
2
7
2 0 4 1 3 0 28
5
0 0 0 0 1
```

### Sample Output 1

```
2 4 1 3 28 0 0
1 0 0 0 0
```

**Explanation:**  
- In the first test case, all zeros are moved to the end, and non-zero elements retain their order.
- In the second test case, the only non-zero element (`1`) is at the start, followed by all zeros.

---

### Sample Input 2

```
2
5
0 3 0 2 0
4
0 0 0 0
```

### Sample Output 2

```
3 2 0 0 0
0 0 0 0
```

---

## Constraints

- `1 <= T <= 10`
- `1 <= N <= 10^5`
- Array elements can be negative, zero, or positive.

---

## Notes

- The solution must maintain the relative order of non-zero elements.
- The operation must be performed in-place (O(1) extra space).
- Aim for O(n) time complexity.
