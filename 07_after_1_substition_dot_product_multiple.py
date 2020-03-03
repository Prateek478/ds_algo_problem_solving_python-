'''
You are given an array a of length n. The characteristic of this array is the value  — the sum of the products of the values ai by i. 
One may perform the following operation exactly once: pick some element of the array and move to any position. 
In particular, it's allowed to move the element to the beginning or to the end of the array. 
Also, it's allowed to put it back to the initial position. 
The goal is to get the array with the maximum possible value of characteristic.

Input
The first line of the input contains a single integer n (2 ≤ n ≤ 200 000) — the size of the array a.
The second line contains n integers ai (1 ≤ i ≤ n, |ai| ≤ 1 000 000) — the elements of the array a.

Output
Print a single integer — the maximum possible value of characteristic of a that can be obtained by performing no more than one move.

Examples
inputCopy
4
4 3 2 5
outputCopy
39
inputCopy
5
1 1 2 7 1
outputCopy
49

explanation of above input and output
In the first sample, one may pick the first element and place it before the third (before 5). 
Thus, the answer will be 3·1 + 2·2 + 4·3 + 5·4 = 39.

In the second sample, one may pick the fifth element of the array and place it before the third. 
The answer will be 1·1 + 1·2 + 1·3 + 2·4 + 7·5 = 49.
'''
a = [0,2,8,4,10]

b=a
length=len(a)
temp=[]
temp_1 = []

def call_func_max(b,length):
    while length>0:
        tmp=b[:length]
        maxv=max(tmp)
        if len(tmp) == 1:
           break
        elif tmp[length -1] == maxv:
            temp.append(maxv)
            length=length-1
            continue
        else:
            tmp.remove(maxv)
            tmp.append(maxv)
            break
    temp.reverse()
    tmp.extend(temp)
    value = dot_product(tmp)
    return (tmp, value)

def call_func_min(b,length):
    index = 0
    while length>index:
        tmp=b[index:length]
        minv=min(tmp)
        if len(tmp) == 1:
            break
        elif tmp[0] == minv:
            temp_1.append(minv)
            index = index+1
            continue
        else:
            tmp.remove(minv)
            temp_1.append(minv)
            break
    temp_1.extend(tmp)
    value = dot_product(temp_1)
    return (temp_1, value)

def dot_product(new_list):
    product_sum = 0
    for i in range(1,len(new_list)+1):
        product_sum = product_sum + i*new_list[i-1]
    return(product_sum)


x, x_product = call_func_max(b,length)
y, y_product = call_func_min(b,length)

print('Input List is : {}'.format(a))

if x_product >= y_product:
    print('After 1 replacement List is : {}'.format(x))
    print('Product sum after 1 replacement : {}'.format(x_product))
else:
    print('After 1 replacement List is : {}'.format(y))
    print('Product sum after 1 replacement : {}'.format(y_product))
