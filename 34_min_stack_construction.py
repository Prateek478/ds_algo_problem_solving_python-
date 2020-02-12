"""
Min Max stack construction
Design a Data Structure SpecialStack that supports all the stack operations
like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element
from the SpecialStack. All these operations of SpecialStack must be O(1).
To implement SpecialStack, you should only use standard Stack data structure and no other data structure like
arrays, list, .. etc.
https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = None
    
    def display(self):
        temp = self.top
        stack_data = []
        while temp:
            stack_data.append(temp.data)
            temp = temp.next
        return stack_data
            
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            self.min = data
        elif data < self.min:
            temp =  2 * data - self.min
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.min = data
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}".format(data))
        
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        else:
            remove_node = self.top
            self.top = self.top.next
            if remove_node.data < self.min:
                print("Top most element removed : {}".format(self.min))
                self.min = 2*self.min - remove_node.data
            else:
                print("Top most element removed : {}".format(remove_node.data))
        
    def getMin(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        else:
            print("minimum stack element : {}".format(self.min))
            
    def peek(self):
        if self.top is None:
            print ("stack is empty")
            return -1
        elif self.top.data < self.min:
            print ("Top most ele", self.min)
        else:
            print ("Top most ele", self.top.data)

if __name__ == "__main__":
    s = Stack()
    s.push(3); 
    s.push(5);
    print (s.display())
    s.getMin(); 
    s.push(2); 
    s.push(1); 
    print (s.display())
    s.getMin(); 
    s.pop(); 
    print (s.display())
    s.getMin(); 
    s.pop(); 
    print (s.display())
    s.peek(); 
  
