

def hotelBookings(queries):
    # Write your code here.
    temp =0

    if not queries:
        return 0
    for i in queries:
        if not i:
            continue
        if(i[0] == "+"):
            temp +=1
    return temp
    pass