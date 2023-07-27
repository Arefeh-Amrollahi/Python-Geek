

def Unionarray(arr1, arr2, n, m):
	# Create a set to store unique elements from both arrays
	set1 = set(arr1)
	set2 = set(arr2)
	# Merge both sets and convert back to list
	result = list(set1.union(set2))
	return result

# Driver code
if __name__ == "__main__":
	arr1 = [1, 2, 2, 2, 3]
	arr2 = [2, 3, 3, 4, 5, 5]
	n = len(arr1)
	m = len(arr2)

	# Function call
	uni = Unionarray(arr1, arr2, n, m)
	for i in uni:
		print(i, end=" ")
