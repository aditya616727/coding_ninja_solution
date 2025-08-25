def findDuplicate(arr):
    # Write your code here
    temp =[0]*(max(arr)+1)
    for i in arr:
        temp[i]=temp[i]+1
    for i,j in enumerate(temp):
        if j >1:
            return i
    pass
