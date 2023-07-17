'''
Iteration Method

    binarySearch(arr, x, low, high)
        repeat till low = high
               mid = (low + high)/2
                   if (x == arr[mid])
                   return mid
   
                   else if (x > arr[mid]) // x is on the right side
                       low = mid + 1
   
                   else                  // x is on the left side
                       high = mid - 1

2. Recursive Method (The recursive method follows the divide and conquers approach)

    binarySearch(arr, x, low, high)
           if low > high
               return False 
   
           else
               mid = (low + high) / 2 
                   if x == arr[mid]
                   return mid
       
               else if x > arr[mid]        // x is on the right side
                   return binarySearch(arr, x, mid + 1, high)
               
               else                        // x is on the right side
                   return binarySearch(arr, x, low,

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.
'''
def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1

    # This below check covers all cases , so need to check
    # for mid=lo-(hi-lo)/2
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid

    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")


if __name__ == '__main__':
    v = [1, 3, 4, 5, 6]

    To_Find = 1
    binarySearch(v, To_Find)

    To_Find = 6
    binarySearch(v, To_Find)

    To_Find = 10
    binarySearch(v, To_Find)

# This code is contrbuted by Tapesh(tapeshdua420)