def getInversions(arr, n):
    # write your code here !!
    temp =0
    for i in range(len(arr)):    
        for j in range(len(arr)):
            if i<j and arr[i]>arr[j]:
                temp +=1
    return temp



    pass 


