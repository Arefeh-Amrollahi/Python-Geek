class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):
        # Use a set to find the unique elements in the union of a and b
        return len(set(a).union(set(b)))

# Example usage:
# Assuming the class is instantiated and the method is called with the correct parameters.
solution = Solution()
array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3]
n = len(array1)  # Size of array1
m = len(array2)  # Size of array2
print(solution.doUnion(array1, n, array2, m))  # This should print 5

#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?page=1&difficulty=Basic&sortBy=submissions

