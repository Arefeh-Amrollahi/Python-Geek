'''. 

All power of two numbers have only one bit set. So count the no. of set bits and if you get 1 then number is a power of 2. Please see Count set bits in an integer for counting set bits.
4. If we subtract a power of 2 numbers by 1 then all unset bits after the only set bit become set; and the set bit become unset.
For example for 4 ( 100) and 16(10000), we get following after subtracting 1 
3 –> 011 
15 –> 01111
So, if a number n is a power of 2 then bitwise & of n and n-1 will be zero. We can say n is a power of 2 or not based on value of n&(n-1). The expression n&(n-1) will not work when n is 0. To handle this case also, our expression will become n& (!n&(n-1)) (thanks to https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/Mohammad for adding this case). 
Below is the implementation of this method.
'''
# Python program to check if given
# number is power of 2 or not

# Function to check if x is power of 2
def isPowerOfTwo (x):

	# First x in the below expression
	# is for the case when x is 0
	return (x and (not(x & (x - 1))) )

# Driver code
if(isPowerOfTwo(31)):
	print('Yes')
else:
	print('No')
	
if(isPowerOfTwo(64)):
	print('Yes')
else:
	print('No')
