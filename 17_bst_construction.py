'''
Binary search tree construction
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data
        
def insert_node(root, node):
    if root is None:
        root=node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.left,node)
                
# A utility function to do inorder tree traversal 
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)

# Binary Tree Construction
bt = Node(50)
insert_node(bt,Node(40))
insert_node(bt,Node(80))
insert_node(bt,Node(20))
insert_node(bt,Node(10))
insert_node(bt,Node(70))
insert_node(bt,Node(90))
inorder_traversal(bt)
