
from collections import deque

def createSequence(n):
    # Write your code here.

    result = []
    q = deque(["2", "5"])
    
    while q:
        num_str = q.popleft()
        num = int(num_str)
        
        if num <= n:   # only consider numbers less than n
            result.append(num)
            q.append(num_str + "2")
            q.append(num_str + "5")
    
    return sorted(result)




