# Race Car Problem

## Problem Statement

Design a class `Car` having a parameterized constructor that takes two arguments as input: `noOfGear` and `color`. The class should have a `printCarInfo` method that prints the car information (`noOfGear` and `color`).

Design another class `RaceCar` that inherits from `Car`. Its parameterized constructor should have an additional attribute `maxSpeed`. The class should have a `printRaceCarInfo` method that prints the race car information (`noOfGear`, `color`, and `maxSpeed`).

**Note:**  
You have to create an object of class `RaceCar` and call the `printRaceCarInfo` method.

---

## Input/Output Format

**Sample Input 1:**
```
5
red
1000
```

**Sample Output 1:**
```
noOfGear: 5
color: red
maxSpeed: 1000
```

---

## Explanation

When we call the `printRaceCarInfo` function, all the information related to the race car will be printed in the