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

# from collections import Counter
from collections import Counter
class Solution:
    def majorityElement(self, A, N):
        # Create a counter for elements in the array
        cnt = Counter(A)
        
        # Iterate over the unique elements in the counter
        for num in cnt:
            # Check if the count of the current element is greater than N//2
            if cnt[num] > N // 2:
                return num
        return -1

# Example 1
A1 = [1, 2, 3]
N1 = len(A1)
solution = Solution()
print(solution.majorityElement(A1, N1))  # Output: -1

# Example 2
A2 = [3, 1, 3, 3, 2]
N2 = len(A2)
print(solution.majorityElement(A2, N2))  # Output: 3
