'''
Check if two arrays are equal or not using Counter Class
We can use the Counter class from the collections module to count the number of occurrences of each element in the arrays and then compare the resulting dictionaries.

Steps:

Use the Counter class to count the number of occurrences of each element in a and b.
Use the == operator to compare the resulting Counter objects.
Return the result of the comparison.
Import the Counter class from the collections module.
Below is the implementation of the above approach:

https://www.geeksforgeeks.org/check-if-two-arrays-are-equal-or-not/

'''
from collections import Counter
 
def arrays_equal(a, b):
    return Counter(a) == Counter(b)
 
a = [3, 2, 1, 3, 2, 1]
b = [1, 2, 3, 1, 2, 3]
c = [4, 5, 6, 4, 5, 6]
 
print(arrays_equal(a, b))  # True
print(arrays_equal(a, c))  # False

'''Second way'''

def areEqual(arr1, arr2, N, M):
 
    # If lengths of array are not
    # equal means array are not equal
    if (N != M):
        return False
 
    # Sort both arrays
    arr1.sort()
    arr2.sort()
 
    # Linearly compare elements
    for i in range(0, N):
        if (arr1[i] != arr2[i]):
            return False
 
    # If all elements were same.
    return True
 
 
# Driver Code
if __name__ == "__main__":
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
    n = len(arr1)
    m = len(arr2)
 
    if (areEqual(arr1, arr2, n, m)):
        print("Yes")
    else:
        print("No")