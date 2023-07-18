'''
Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
Output: 5
Explanation: The missing number between 1 to 8 is 5

https://www.geeksforgeeks.org/find-the-missing-number/
'''

def getMissingNo(arr, n):
	t = (n + 1)*(n + 2)/2
	sum= sum(arr)
	return t - sum

# Driver code
if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)
	
	# Function call
	miss = getMissingNo(arr, N)
	print(miss)