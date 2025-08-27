def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    a.sort()
    return a[-2],a[1]
    pass
