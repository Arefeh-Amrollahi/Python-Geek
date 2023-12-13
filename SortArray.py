#
# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

class Solution:
    def sort012(self, arr, n):
        # Sort the array in ascending order and return a copy
        return sorted(arr)

# Example usage:
arr1 = [0, 2, 1, 2, 0]
n1 = len(arr1)
solution = Solution()
sorted_arr1 = solution.sort012(arr1, n1)
print(sorted_arr1)  # Output: [0, 0, 1, 2, 2]

arr2 = [0, 1, 0]
n2 = len(arr2)
sorted_arr2 = solution.sort012(arr2, n2)
print(sorted_arr2)  # Output: [0, 0, 1]
