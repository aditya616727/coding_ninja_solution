# Hotel Floor Room Booking Problem

## Problem Statement

You are the receptionist at a hotel which has 10 floors, numbered from 0 to 9, and each floor has 26 rooms named from ‘A’ to ‘Z’. Your task is to handle booking queries.

You get booking queries in the form of strings of size 3:
- The **first character** is ‘+’ (room is booked) or ‘-’ (room is freed).
- The **second character** represents the floor of the room (`0` to `9`).
- The **third character** represents the room name (`A` to `Z`).

On booking of each room, you collect **1 coin** from the customer. After all booking queries, count the number of coins collected.

**Assume:**  
- The list describes a correct sequence of bookings in chronological order (only free rooms can be booked, and only booked rooms can be freed).

---

## Example

**Booking queries:**  
`["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]`

| Query | Action | Coin Collected? |
|-------|--------|----------------|
| +1A   | Book Room A on 1st floor | Yes (1) |
| +3E   | Book Room E on 3rd floor | Yes (1) |
| -1A   | Free Room A on 1st floor | No      |
| +4F   | Book Room F on 4th floor | Yes (1) |
| +1A   | Book Room A on 1st floor | Yes (1) |
| -3E   | Free Room E on 3rd floor | No      |

**Total coins collected:** 4

---

## Input/Output Format

- **Input:**
  - The first line contains an integer `T`, the number of test cases.
  - For each test case:
    - The first line contains an integer `N`, the number of queries.
    - The second line contains `N` space-separated booking queries.

- **Output:**
  - For each test case, print the number of coins collected.

---

## Constraints

- 1 ≤ T ≤ 100
- 0 ≤ N ≤ 600
- Each query string length = 3

---

## Sample Input 1
