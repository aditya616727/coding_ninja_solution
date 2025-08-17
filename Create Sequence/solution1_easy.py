def createSequence(n):
    # Write your code here.
    temp = []
    for i in range(1,n+1,1):
        s =str(i)
        if set(s).issubset({'2','5'}):
            temp.append(i)
    return temp

