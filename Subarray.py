class Solution:
    def subarraySum(self, arr, n, s):
        # Initialize current sum and start pointer
        current_sum = arr[0]
        start = 0

        # Loop over each element in the array
        for i in range(1, n + 1):
            # Clean up the current_sum to maintain the subarray sum less than or equal to s
            while current_sum > s and start < i - 1:
                current_sum -= arr[start]
                start += 1

            # If current_sum becomes equal to s, return the start and end indices
            if current_sum == s:
                return [start + 1, i]  # +1 for 1-based indexing

            # Add the current element to the current_sum
            if i < n:
                current_sum += arr[i]

        # If we reach here, no subarray was found
        return [-1]
sol = Solution()
arr = [1,2,3,7,5]
n = 5
s = 12
print(sol.subarraySum(arr, n, s))  # This should print [2, 4] based on 1-based indexing
