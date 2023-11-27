# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Note :-  l and r denotes the starting and ending index of the array.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# L=0 R=5

# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.

# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1?page=1&sortBy=submissions
class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        # Sort the array within the range [l, r]
        arr = arr[l:r+1]
        arr.sort()

        # Return the k-th smallest element in the sorted array
        return arr[k-1]

# Let's test the function with an example
sol = Solution()

# Example 1: Should return 7 as the 3rd smallest element
print(sol.kthSmallest([7, 10, 4, 3, 20, 15], 0, 5, 3))


