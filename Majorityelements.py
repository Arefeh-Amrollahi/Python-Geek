# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.
 

# Example 1:

# Input:
# N = 3 
# A[] = {1,2,3} 
# Output:
# -1
# Explanation:
# Since, each element in 
# {1,2,3} appears only once so there 
# is no majority element.
# Example 2:

# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element.
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&sortBy=submissions

class Solution:
    def majorityElement(self, A, N):
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None

        # 1st pass to find the candidate
        for num in A:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # 2nd pass to confirm the candidate is a majority
        count = sum(1 for num in A if num == candidate)
        if count > N // 2:
            return candidate
        else:
            return -1

# Let's test the function with an example
sol = Solution()

# Example 1: Should return -1 as there is no majority element
print(sol.majorityElement([1, 2, 3], 3))

# Example 2: Should return 3 as it is the majority element
print(sol.majorityElement([3, 1, 3, 3, 2], 5))
