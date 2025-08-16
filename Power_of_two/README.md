# Power of Two

## Problem Statement

You have been given an integer `N`.

Your task is to return `true` if it is a power of two. Otherwise, return `false`.

An integer `N` is a power of two if it can be expressed as `2^K` where `K` is an integer.

---

## Example

### Sample Input 1:
```
16
```
### Sample Output 1:
```
true
```
**Explanation:**  
16 can be represented as 2^4. So, 16 is a power of two, and hence `true` is our answer.

---

### Sample Input 2:
```
10
```
### Sample Output 2:
```
false
```
**Explanation:**  
10 cannot be represented as a power of two, so the answer is `false`.

---

## Constraints

- -2^31 <= N <= 2^31 - 1

**Time Limit:** 1 second

---

## Notes

- Negative numbers and zero are not considered powers of two.
- Only positive integers that can be written as 2 raised to some integer power