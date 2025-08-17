## Problem Statement

Ninja is good at numbers. So today his friend gave him a task that required him to find out numbers made of 2 and 5 only less than a given limit.

Given an integer N, you need to print all numbers less than N which are having digits only 2 or 5 or both.

### For example:
All numbers less than 30 with digits 2 and 5 are 2, 5, 22, 25.

---

## Detailed Explanation (Input/Output Format, Notes, Images)

### Constraints:
- 1 <= T <= 10
- 1 <= N <= 10^16

**Time Limit:** 1 sec

**Note:**
You are not required to print anything; it has already been taken care of. Just implement the function.

---

### Sample Input 1:
```
2  
10
100
```

### Sample Output 1:
```
2 5 
2 5 22 25 52 55
```

#### Explanation For Sample Output 1:
For the first test case, only 2 and 5 are the required numbers. Hence we print them in ascending order.
For the second test case, we have 6 required numbers.

---

### Sample Input 2:
```
2
2
7
```

### Sample Output 2:
```
2
2 5
```
