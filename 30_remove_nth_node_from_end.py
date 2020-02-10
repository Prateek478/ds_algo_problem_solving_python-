'''
Delete Nth node from the end of the given linked list
Input: 2 -> 3 -> 1 -> 7 -> NULL, N = 1  
Output:
Created Linked list is:
2 3 1 7
Linked List after Deletion is:
2 3 1
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert_at_beginning(head,val):
    if head is None:
        head = Node(val)
        return head
    new_node = Node(val)
    new_node.next = head
    head = new_node
    return head

def print_ll(head):
    pointer = head
    while pointer is not None:
        print(pointer.data)
        pointer = pointer.next

#optmized
def delete_nth_at_end(head,k):
    x = y = head
    for i in range(k):
        y=y.next
    while y.next is not None:
        x=x.next
        y=y.next
    print("deleted node is {}".format(x.next.data))
    x.next = x.next.next
    return head

#iterative
def delete_nth_at_end_iterative(head, n):
    count = 1
    curr = head
    while curr.next is not None:
        count += 1
        curr = curr.next
    k = count - n + 1
    if k > 1:
        temp = head
        count = 1
        while count < k - 1:
            temp = temp.next
            count += 1
        print "Node deleted is ", temp.next.data
        temp.next = temp.next.next
    elif k == 1:
        print "Node deleted is ", head.data
        head = head.next
    else:
        print "Please enter valid position"
        return -1
    return head
  
head = insert_at_beginning(None, 2)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 5)
head = insert_at_beginning(head, 6)
head = insert_at_beginning(head, 7)
#print_ll(head)
print
head = delete_nth_at_end(head, 3)
print
#print_ll(head)
head = insert_at_beginning(head, 8)
print
print_ll(head)
head = delete_nth_at_end_iterative(head, 3)
print
print_ll(head)
