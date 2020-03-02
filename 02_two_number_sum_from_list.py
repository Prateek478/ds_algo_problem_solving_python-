'''
Two number sum i.e given a array find all the pairs whose sum equal to given k

Eg: [1,5,7,8,2,0] and k=7
Result is [(0,7),(7,0),(2,5),(5,2)]
'''

def setofgroup(input, n):
    input.sort()
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            if n == input[i] + input[j]:
                output.append((input[i],input[j]))
    return(output)

def groupusinglistc(input,n):
    return[(input[i],j) for i in range(len(input)) for j in input[i+1:] if ((input[i]+j == n) and ((input[i] != n) or (j != n)))]

def two_sum_n(a, k):
	pairs = list()
	d = dict()
	for i in a:
		d[k-i] = i   # takes O(n)
	for i in a: # takes O(n)
		if i in d.keys():
			pairs.append((i, k - i))
    # instead of set, can also check in above if that pair exists in list before adding
    return pairs  # O(n), overall time complexity = O(n) + O(n) + O(n) = O(n)

if __name__ == "__main__":
    input = [3,20,2,12,7,0,5,8,9,2,10,6,-1]
    n = 9
    output = []
    print("M1 of 2 values sum == 9 are : {}".format(setofgroup(input,n)))
    print("M2 of 2 values sum == 9 are : {}".format(groupusinglistc(input,n)))
    print("M3 of 2 values sum == 9 are : {}".format(two_sum_n(input,n)))

    import timeit
    print("setofgroup(input,n) method time")
    print(timeit.timeit("setofgroup([3,20,2,12,7,0,5,8,9,2,10,6,-1],9)", setup = "from __main__ import setofgroup", number=1))
    print("groupusinglistc(input,n) method time")
    print(timeit.timeit("groupusinglistc([3,20,2,12,7,0,5,8,9,2,10,6,-1],9)", setup = "from __main__ import groupusinglistc", number=1))
    print("two_sum_n(input,n) method time")
    print(timeit.timeit("two_sum_n([3,20,2,12,7,0,5,8,9,2,10,6,-1],9)", setup = "from __main__ import two_sum_n", number=1))
