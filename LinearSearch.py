'''
Linear Search is defined as a sequential search algorithm that starts at one end and goes
through each element of a list until the desired element is found, otherwise the search continues
till the end of the data set.
'''
# Python3 code to linearly search x in arr[].


def search(arr, N, x):

	for i in range(0, N):
		if (arr[i] == x):
			return i
	return -1


# Driver Code
if __name__ == "__main__":
	arr = [2, 3, 4, 10, 40]
	x = 10
	N = len(arr)

	# Function call
	result = search(arr, N, x)
	if(result == -1):
		print("Element is not present in array")
	else:
		print("Element is present at index", result)
