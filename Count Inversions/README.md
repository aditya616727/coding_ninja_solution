# Count Inversions

## Problem Statement
For a given integer array/list `ARR` of size `N` containing all distinct values, find the total number of **Inversions** that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met:

1. `ARR[i] > ARR[j]`
2. `i < j`

Where `i` and `j` denote the indices ranging from `[0, N)`.

---

## Constraints
- 1 <= N <= 10^5
- 1 <= ARR[i] <= 10^9

Where `ARR[i]` denotes the array element at `i`th index.

**Time Limit:** 1 sec

---

## Input Format
- The first line contains an integer `N`, the size of the array.
- The second line contains `N` space-separated integers, the elements of the array `ARR`.

## Output Format
- Print the total number of inversions in the array.

---

## Sample Input 1
```
3
3 2 1
```

## Sample Output 1
```
3
```

### Explanation
We have a total of 3 pairs which satisfy the condition of inversion: (3, 2), (2, 1), and (3, 1).

---

## Sample Input 2
```
5
2 5 1 3 4
```

## Sample Output 2
```
4
```

### Explanation
We have a total of 4 pairs which satisfy the condition of inversion: (2, 1), (5, 1), (5, 3), and (5, 4).

---

## Hints
1. Start with the brute force approach.
2. Use a modified merge sort.
3. Iterate through the elements in sorted order and use a Fenwick tree to track the inversions.
