class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, A, D, N):
        # Helper function to reverse elements in a specified range.
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Ensure D is within the array size.
        D = D % N

        # Rotate the array using the reversal algorithm.
        reverse(A, 0, D - 1)       # Reverse the first D elements.
        reverse(A, D, N - 1)       # Reverse the remaining elements.
        reverse(A, 0, N - 1)       # Reverse the entire array.

# Example usage:
# solution = Solution()
# N = 5
# D = 2
# arr = [1, 2, 3, 4, 5]
# solution.rotateArr(arr, D, N)
# print(arr)  # Output: [3, 4, 5, 1, 2]
