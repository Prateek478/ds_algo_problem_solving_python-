"""
Search element in a sorted matrix.
Given a sorted matrix mat[n][m] and an element ‘x’. Find position of x in the matrix if it is present, else print -1. 
Matrix is sorted in a way such that all elements in a row are sorted in increasing order and for row ‘i’, where 1

Example:
Input : mat[][] = { {1, 5, 9}, {14, 20, 21}, {30, 34, 43} } x = 14 Output : Found at (1, 0)
Input : mat[][] = { {1, 5, 9, 11}, {14, 20, 21, 26}, {30, 34, 43, 50} } x = 42 Output : -1

https://www.geeksforgeeks.org/search-element-sorted-matrix/
"""

# Brute force method o(n*m)
def brute_force(array, val):
    for sub_array in array:
        if val in sub_array:
            return((array.index(sub_array),sub_array.index(val)))
    return -1

import numpy
# using binary search log(n*m)
def search_typecast_2D_to_1D(array, val):
    npa = numpy.array(array)
    array_1d = npa.flatten()
    print(array_1d)

    ret = binary_search(array_1d, val)
    if ret != -1:
        print("Element matches : {}".format(val))
    else:
        print("Element Not Found : {}".format(val))
        
def binary_search(a, ele):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = int((low + high)/2)
        if ele == a[mid]:
            return mid
        elif ele < a[mid]:
            high = mid - 1
        elif ele > a[mid]:
            low = mid + 1
    return -1


if __name__ == "__main__":    
  a = [[3,6,9],[11, 14,17],[19,26,29]]
  print(brute_force(a, 17))
  print(brute_force(a, 30))
  search_typecast_2D_to_1D(a, 31)
  search_typecast_2D_to_1D(a, 19)
