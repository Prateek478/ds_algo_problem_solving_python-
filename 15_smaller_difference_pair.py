'''
Smallest Difference pair of values between two unsorted Arrays
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.
Examples :
Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8}
Output : 3
That is, the pair (11, 8)
Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80}
Output : 10
That is, the pair (40, 50)
'''

def smallest_diff(A, B):
    diff = float("inf")
    A.sort()
    B.sort()
    a=b=0
    while (a < len(A) and b < len(B)):
        if abs(A[a] - B[b]) < diff:
            diff = abs(A[a] - B[b])
            
        # Move Smaller Value
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    # return final sma result
    return diff

def smallest_diff(A, B):
    diff = float("inf")
    A.sort()
    B.sort()
    a=b=0
    while (a < len(A) and b < len(B)):
        if abs(A[a] - B[b]) < diff:
            diff = abs(A[a] - B[b])
            
        # Move Smaller Value
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    # return final sma result
    return diff
    
# ord(n2) complexity
def smallest_diff_1(A, B):
    A.sort()
    B.sort()
    diff = {}
    
    for i in range(len(A)):
        for j in range(len(B)):
            if abs(A[i]-B[j]) not in diff: 
                diff[abs(A[i]-B[j])] = ((A[i],B[j]))
    # return final sma result
    return min(diff.keys())
    #return diff
    
if __name__ == "__main__":
    A = [1, 3, 15, 11, 2]
    B = [23, 127, 235, 19, 8]
    
    print(smallest_diff(A, B))
    print(smallest_diff_1(A, B))
