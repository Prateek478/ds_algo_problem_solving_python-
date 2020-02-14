"""
Check for balanced parentheses in Python
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
Examples:
Input : {[]{()}}
Output : Balanced
Input : [{}{}(]
Output : Unbalanced
"""
#Method 1
def check_balanced_paranthesis(var):
    open_par = ["{","[","("] 
    close_par = ["}","]",")"]
    stack = []
    
    for i in var:
        if i in open_par:
            stack.append(i)
        elif i in close_par:
            pos = close_par.index(i)
            if len(stack) and open_par[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                print("Unbalanced Paranthesis")
            
    if len(stack) == 0:
        print("Balanced paranthesis")

#Method 2
def check_balanced_paranthesis_2(my_string):
    brackets = ['()', '{}', '[]'] 

    while any(x in my_string for x in brackets):
        for i in brackets:
            my_string = my_string.replace(i,'')
    
    if len(my_string) == 0:
        print("Balanced paranthesis")    
    else:
        print("Unbalanced Paranthesis")
        
        
 if __name__ == "__main__":
    input = '{[]{()}}'
    check_balanced_paranthesis(input)
    check_balanced_paranthesis_2(input)
    input = '[{}{}(]'
    check_balanced_paranthesis(input)
    check_balanced_paranthesis_2(input)       

