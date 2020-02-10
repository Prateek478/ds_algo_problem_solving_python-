'''
Permutations of a given string

Eg: input : "abc"
output: abc acb bac bca cab cba
'''

# Python program to print all permutations
def permute(a, l, r): 
    if l == r: 
        #print("string l,r : ",l,r)
        print (''.join(List) ) 
    else: 
        for i in range(l, r + 1):
            print("i and l : ",str(i),str(l))
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            #print("in the end")
            a[l], a[i] = a[i], a[l] # backtrack 


# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
