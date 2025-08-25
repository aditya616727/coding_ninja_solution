# Duplicate In Array

## Problem Statement

You are given an array `ARR` of size `N` containing each number between 1 and `N - 1` at least once. There is a single integer value that is present in the array twice. Your task is to find the duplicate integer value present in the array.

### Example

Consider `ARR = [1, 2, 3, 4, 4]`, the duplicate integer value present in the array is `4`. Hence, the answer is `4` in this case.

**Note:**  
A duplicate number is always present in the given array.

---

## Input/Output Format

- The first line contains an integer `T`, the number of test cases.
- For each test case:
  - The first line contains an integer `N`, the size of the array.
  - The second line contains `N` space-separated integers, the elements of the array.

**Output:**  
For each test case, print the duplicate integer value present in the array.

---

## Constraints

- 1 <= T <= 10
- 2 <= N <= 10^5
- 1 <= ARR[i] <= N - 1

Where:
- `T` denotes the number of test cases,
- `N` denotes the number of elements in the array,
- `ARR[i]` denotes the `i-th` element of the array `ARR`.

**Time limit:** 1 sec

---

## Sample Input 1

```
2
5
4 2 1 3 1
7
6 3 1 5 4 3 2
```

## Sample Output 1

```
1
3
```

### Explanation

- For the first test case, the duplicate integer value present in the array is `1`.
- For the second test case, the duplicate integer value present in the array is `3`.

---

## Sample Input 2

```
2
6 
5 1 2 3 4 2  
9
8 7 2 5 4 7 1 3 6
```

## Sample Output 2

```
2
7
```

---

## Hints

1. Simply calculate the frequency of each value.
2. Try to optimise the above approach by using an array to store the frequencies.
3. Think of a solution using Floyd’s cycle finding algorithm.
4. Try to think of a solution