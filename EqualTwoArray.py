'''
Check if two arrays are equal or not using Counter Class
We can use the Counter class from the collections module to count the number of occurrences of each element in the arrays and then compare the resulting dictionaries.

Steps:

Use the Counter class to count the number of occurrences of each element in a and b.
Use the == operator to compare the resulting Counter objects.
Return the result of the comparison.
Import the Counter class from the collections module.
Below is the implementation of the above approach:

'''
from collections import Counter
 
def arrays_equal(a, b):
    return Counter(a) == Counter(b)
 
a = [3, 2, 1, 3, 2, 1]
b = [1, 2, 3, 1, 2, 3]
c = [4, 5, 6, 4, 5, 6]
 
print(arrays_equal(a, b))  # True
print(arrays_equal(a, c))  # False
 