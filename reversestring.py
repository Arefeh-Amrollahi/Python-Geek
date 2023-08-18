def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

'''
# Driver Code
if __name__ == '__main__':
	str = "geeksforgeeks" # Input String

	# Step 1: Initialise an object of StringBuffer class
	sb = str[::-1]

	# Step 2: Invoke the .reverse() method (not applicable in Python)

	# Step 3: Print the reversed string
	print(sb)

'''