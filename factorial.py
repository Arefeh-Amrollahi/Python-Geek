
# # factorial of given number
# def factorial(n):
	
# 	# single line to find factorial
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1)

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))
# Python 3 program to find
# # factorial of given number
# import math

# def factorial(n):
#     return(math.factorial(n))


# # Driver Code
# num = 5
# print("Factorial of", num, "is",
#       factorial(num))

# This code is contributed by Ashutosh Pandit
import math
def factorial(n):
    return(math.factorial(n))
num = 5
print("fact", factorial(num), "is")
