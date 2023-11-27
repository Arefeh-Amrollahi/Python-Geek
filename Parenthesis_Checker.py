# Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
# For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

# Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

# Example 1:

# Input:
# {([])}
# Output: 
# true
# Explanation: 
# { ( [ ] ) }. Same colored brackets can form 
# balanced pairs, with 0 number of 
# unbalanced bracket.
# https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&sortBy=submissions

class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # code here
        stack = []
        
        # Dictionary to hold the matching pairs of brackets
        bracket_pair = {')': '(', '}': '{', ']': '['}
        
        # Loop through each character in the expression
        for char in x:
            # If the character is an opening bracket, push to stack
            if char in '([{':
                stack.append(char)
            # If the character is a closing bracket
            elif char in ')]}':
                # If stack is empty or the top of the stack is not the matching opening bracket
                if not stack or stack[-1] != bracket_pair[char]:
                    return False
                stack.pop()
        
        # If stack is empty, all brackets are balanced
        return not stack

# Let's test the function with the given examples

sol = Solution()

# Example 1: Should return True as the brackets are balanced
print(sol.ispar("{([])}"))

# Example 2: Should return True as the brackets are balanced
print(sol.ispar("()"))

# Example 3: Should return False as the brackets are not balanced
print(sol.ispar("([]"))
