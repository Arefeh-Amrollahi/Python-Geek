
# arr2[0..m-1] contain same elements.
'''
def areEqual(arr1, arr2, N, M):

	# If lengths of array are not
	# equal means array are not equal
	if (N != M):
		return False

	# Sort both arrays
	arr1.sort()
	arr2.sort()

	# Linearly compare elements
	for i in range(0, N):
		if (arr1[i] != arr2[i]):
			return False

	# If all elements were same.
	return True


# Driver Code
if __name__ == "__main__":
	arr1 = [3, 5, 2, 5, 2]
	arr2 = [2, 3, 5, 5, 2]
	n = len(arr1)
	m = len(arr2)

	if (areEqual(arr1, arr2, n, m)):
		print("Yes")
	else:
		print("No")
'''
def check(self,A,B,N):
        
        #return: True or False
        
        if sorted(A) == sorted(B):
            return 1
        return 0
 
 