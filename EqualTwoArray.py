from collections import Counter

def arrays_equal(a, b):
	return Counter(a) == Counter(b)

a = [3, 2, 1, 3, 2, 1]
b = [1, 2, 3, 1, 2, 3]
c = [4, 5, 6, 4, 5, 6]
 
print(arrays_equal(a, b))  # True
print(arrays_equal(a,b))