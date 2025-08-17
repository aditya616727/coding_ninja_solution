# Palindrome Count

## Problem Statement

Ninja loves to play with strings and anagrams. A palindrome is a string that is read the same backward or forward. An anagram is a string that is formed by rearranging the characters of the string. Given a string `STR`, find the number of substrings whose anagram is palindromic.

---

## Input/Output Format

- The first line contains an integer `T`, the number of test cases.
- For each test case:
	- The first line contains the string `STR`.

### Sample Input 1

```
2
aa
abc
```

### Sample Output 1

```
3
3
```

**Explanation for Sample Input 1:**

- For the first test case:
	- Substrings: {a, a, aa}
	- All substrings are palindromes, so the result is 3.
- For the second test case:
	- Substrings: {a, b, c, ab, bc, abc}
	- Only {a, b, c} are palindromes. No anagram of {ab, bc, abc} is a palindrome. So, the result is 3.

---

### Sample Input 2

```
2
aaa
aab
```

### Sample Output 2

```
6
5
```

---

## Constraints

- `1 <= T <= 10`
- `1 <= |STR| <= 5*10^3`
- The string `STR` contains lowercase letters only.

---

## Notes

- A substring's anagram is palindromic if the characters can be rearranged to form a palindrome.
- For a string to have a palindromic anagram, at most one character can have an odd frequency.
- Aim for an efficient solution due to the input size constraints.
