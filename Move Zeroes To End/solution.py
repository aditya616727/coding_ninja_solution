def pushZerosAtEnd(arr):
    # write your code here
	pos = 0
	for i in range(len(arr)):
		if arr[i] !=0:
			arr[pos] =arr[i]
			pos = pos+1
	while pos< len(arr):
			arr[pos] =0
			pos=pos+1

	return arr