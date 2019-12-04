# Python3 program to count distinct 
# elements in a given array 
def countDistinct(arr, n): 

	res = 1

	# Pick all elements one by one 
	for i in range(1, n): 
		j = 0
		for j in range(i): 
			if (arr[i] == arr[j]): 
				break

		# If not printed earlier, then print it 
		if (i == j + 1): 
			res += 1
	
	return res 

# Driver Code 
arr = [12, 10, 9, 45, 2, 10, 10, 45] 
n = len(arr) 
print(countDistinct(arr, n)) 

# This code is contributed by Mohit Kumar 
