

def termsOfAP(x):
    fin_arr = []
    temp = 0
    i =1
    while len(fin_arr) !=x:
        if i%4 !=2:
            fin_arr.append(3*i+2)
        i +=1

    return fin_arr

    # Write your code here
    # Return a list of integers
    pass