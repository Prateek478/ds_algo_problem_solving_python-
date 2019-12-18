'''
Given an array of distinct elements. The task is to find triplets in array whose sum is zero.
'''

# Sum of three number equal to zero o(n3)
def sum_of_three_equals_zero(a):
    for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                #print ("i, j, k : ",i,j,k)
                if a[i] + a[j] + a[k] == 0 :
                    return True
    return False
    
# Sum of three number equal to zero o(n2)
def sum_of_three_equals_zero_1(a):
    for i in range(len(a)-2):
        ret = two_sum_n(a[i+1:], -a[i])
        if len(ret):
            #print(a[i],ret)
            return True
    return False


def two_sum_n(a, k):
        pairs = list()
        d = dict()
        for i in range(0, len(a)):
                d[a[i]] = i   # takes O(n)
        for i in range(0, len(a)): # takes O(n)
                if k - a[i] in d.keys() and  d[k - a[i]] != i:
                        pairs.append((a[i], k - a[i]))
        # instead of set, can also check in above if that pair exists in list before adding
        return pairs
        
if __name__ == "__main__":
    a = [-4,2,1,6,5,7]
    print(sum_of_three_equals_zero(a))
    print(sum_of_three_equals_zero_1(a))
    a = [4,2,2,6,-5,-1]
    print(sum_of_three_equals_zero(a))
    print(sum_of_three_equals_zero_1(a))
