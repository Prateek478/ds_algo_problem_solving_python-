#  palindrome check for both strings and numbers


# Only Number palindrome 
def reverse(num):
    initial = 0
    counter = 0
    while num > 0:
        initial = initial + (num%10)*(10**counter)
        num=int(num/10)
        counter=counter+1
    return initial

n=1001
print('initial value is : {}'.format(n))
reverse_value = reverse(n)
print('reverse value is : '+str(reverse_value))

# String and Number palindrome
def reverse_1(input):
    if type(input) == int:
        input = str(input)
        return int(input[::-1])
    return input[::-1]

input=10001
print('value is : {}'.format(input))
print('Is plalindrome : {}'.format(reverse_1(input) == input))
input = 'madam'
print('\nvalue is : {}'.format(input))
print('Is plalindrome : {}'.format(reverse_1(input) == input))


# String and Number palindrome 2
def reverse_2(input):
    if type(input) == int:
        input = str(input)
    z=''
    for i in input:
        z = i+z
    return z

input=10001
print('value is : {}'.format(input))
print('Is plalindrome : {}'.format(int(reverse_2(input)) == input))
input = 'madam1'
print('\nvalue is : {}'.format(input))
print('Is plalindrome : {}'.format(reverse_2(input) == input))


# String and Number palindrome 3
def reverse_3(input):
    if type(input) == int:
        input = str(input)
    for i in range(0,int(len(input)/2)):
        if input[i] != input[len(input)-i-1]:
            return False
    return True
            

input=10001
print('value is : {}'.format(input))
print('Is plalindrome : {}'.format(reverse_3(input)))
input = 'madam1'
print('\nvalue is : {}'.format(input))
print('Is plalindrome : {}'.format(reverse_3(input)))
