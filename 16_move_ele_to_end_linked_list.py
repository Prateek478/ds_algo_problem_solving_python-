'''
Move all occurrences of an element to end in a linked list
Given a linked list and a key in it, the task is to move all occurrences of given key to end of linked list,
keeping order of all other elements same.
Examples:
Input  : 1 -> 2 -> 2 -> 4 -> 3
         key = 2
Output : 1 -> 4 -> 3 -> 2 -> 2
Input  : 6 -> 6 -> 7 -> 6 -> 3 -> 10
         key = 6
Output : 7 -> 3 -> 10 -> 6 -> 6 -> 6
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_item(head, item):
    temp = head
    prev = None
    if temp.next == None:
        temp = None
        return head
    
    while temp.next is not None:
        if temp.data == item:
            print("delete node in middle", temp.data)
            prev.next = temp.next 
            return head
        prev = temp
        temp = temp.next
        
    prev.next = None
    print("delete node in end", temp.data)
    return head

def insert_at_end(head, data):
    new_node = Node(data)
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    new_node.next = None

def print_from_beginning(node):
    if node is None:
        print
        return
    print(node.data)
    print_from_beginning(node.next)

def move_to_end(head, key):
    if head == None:
        return
    temp = head
    nodelist = []

    while temp.next is not None:
        if temp.data == key:
            nodelist.append(temp.data)
        temp = temp.next

    if len(nodelist) == 0:
        print("No key is matching the existing linklist")
        return
    else:
        print('nodelist',nodelist)
        for node in nodelist:
            delete_item(head,node)
        for node in nodelist:
            insert_at_end(head,node)
    return head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(2)
    key = 2
    #print_from_beginning(head)
    move_to_end(head, key)
    print_from_beginning(head)
