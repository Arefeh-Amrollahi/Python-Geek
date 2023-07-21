'''
If x is 2:
math.log2(2) = 1, which is an integer.
math.log2(2) % 1 will be equal to 0 because 1 divided by 1 is 1 with no remainder.
So, math.log2(2) % 1 == 0 will be True.

If x is 8:
math.log2(8) = 3, which is an integer.
math.log2(8) % 1 will be equal to 0 because 3 divided by 1 is 3 with no remainder.
So, math.log2(8) % 1 == 0 will be True.

If x is 5:
math.log2(5) = 2.321928094887362, which is not an integer.
math.log2(5) % 1 will be a non-zero decimal value because there is a remainder when 2.321928094887362 is divided by 1.
So, math.log2(5) % 1 == 0 will be False
'''

# Function to check if x is power of 2
import math

def isPowerOfTwo (x):
    if x < 1:
        return False
    return math.log2(x) % 1 == 0
        
if __name__ == "__main__":
    # Function calls
	print("Yes" if isPowerOfTwo(31) else "No")


    
