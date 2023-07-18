# Python program for the union of two arrays using Set
def getUnion(a, n, b, m):

	# Defining set container s
	hs = set()
	if(n < m):
		min = n
	else:
		min = m

	# add elements from both the arrays for
	# index from 0 to min(n, m)-1
	for i in range(0, min):
		hs.add(a[i])
		hs.add(b[i])

	if(n > m):
		for i in range(m, n):
			hs.add(a[i])
	else:
		if(n < m):
			for i in range(m, n):
				hs.add(b[i])

	print("Number of elements after union operation: ", len(hs))
	print("The union set of both arrays is :")
	for i in hs:
		print(i, end=" ")
	print("\n")
	# s will contain only distinct
	# elements from array a and b


# Driver Program
a = [1, 2, 5, 6, 2, 3, 5, 7, 3]
b = [2, 4, 5, 6, 8, 9, 4, 6, 5, 4]
n1 = len(a)
n2 = len(b)

# Function call
getUnion(a, n1, b, n2)

