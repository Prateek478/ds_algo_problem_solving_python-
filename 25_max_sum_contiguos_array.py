'''
Maximum sum contiguos subarray, kadanes algorithm

find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
Ex: [-2, -3, 4, -1, -2, 1, 5, -3]

max sum contiguos subarray is 7 [4,-1,-2,1,5]
'''
# Iterative method
def max_contiguous_array(arr):
    max_so_far = max_ending_here = 0
    
    for i in arr:
        max_ending_here = max_ending_here + i
        
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

# Using dp
def max_contiguous_array_dp(arr1):
    max_so_far_dp = max_ending_here_dp = arr1[0]
    
    for i in range(1,len(arr1)):
        
        max_ending_here_dp = max(arr1[i], max_ending_here_dp + arr1[i])
        max_so_far_dp = max(max_so_far_dp, max_ending_here_dp)

    return max_so_far_dp
    
if __name__ == "__main__":
    array = [-2,-3,4,-1,-2,1,5,-3]
    print("Max sub continuous array sum : {}".format(max_contiguous_array(array)))
    print("DP Max sub continuous array sum : {}".format(max_contiguous_array_dp(array)))
