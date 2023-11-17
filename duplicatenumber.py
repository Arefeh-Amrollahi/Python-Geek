class Solution:
    def duplicates(self, arr, n):
        # Dictionary to store the count of each element
        count = {}
        # List to store the duplicates
        duplicates = []
        
        # Count the occurrence of each element
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Find all elements that appear more than once
        for key, value in count.items():
            if value > 1:
                duplicates.append(key)
        
        # If no duplicates, return [-1]
        if not duplicates:
            return [-1]
        
        # Otherwise, sort the list of duplicates and return it
        duplicates.sort()
        return duplicates

# Example usage:
# Creating an object of the Solution class
sol = Solution()
# Calling the duplicates method with an example array
print(sol.duplicates([0, 3, 1, 2], 4))  # Output would be [-1] as there are no duplicates
# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&sortBy=submissions