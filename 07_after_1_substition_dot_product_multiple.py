
a = [0,2,8,4,10]

b=a
length=len(a)
temp=[]
temp_1 = []

def call_func_max(b,length):
    while length>0:
        tmp=b[:length]
        maxv=max(tmp)
        ind=tmp.index(maxv)
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
        ind=tmp.index(minv)
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
