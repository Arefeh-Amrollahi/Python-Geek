
def sort012(arr,n):
        # code here
        arr.sort()
        return arr

if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    n = len(arr)
 
    sort012(arr, n)
    print(arr)