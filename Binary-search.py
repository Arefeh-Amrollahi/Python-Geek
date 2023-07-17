'''
Iteration Method

    binarySearch(arr, x, low, high)
        repeat till low = high
               mid = (low + high)/2
                   if (x == arr[mid])
                   return mid
   
                   else if (x > arr[mid]) // x is on the right side
                       low = mid + 1
   
                   else                  // x is on the left side
                       high = mid - 1

2. Recursive Method (The recursive method follows the divide and conquers approach)

    binarySearch(arr, x, low, high)
           if low > high
               return False 
   
           else
               mid = (low + high) / 2 
                   if x == arr[mid]
                   return mid
       
               else if x > arr[mid]        // x is on the right side
                   return binarySearch(arr, x, mid + 1, high)
               
               else                        // x is on the right side
                   return binarySearch(arr, x, low,

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.
'''
# Python3 code to implement iterative Binary
# Search.


# It returns location of x in given array arr
def binarySearch(arr, l, r, x):

	while l <= r:

		mid = l + (r - l) // 2

		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1

	# If we reach here, then the element
	# was not present
	return -1


# Driver Code
if __name__ == '__main__':
	arr = [2, 3, 4, 10, 40]
	x = 10

	# Function call
	result = binarySearch(arr, 0, len(arr)-1, x)
	if result != -1:
		print("Element is present at index", result)
	else:
		print("Element is not present in array")
