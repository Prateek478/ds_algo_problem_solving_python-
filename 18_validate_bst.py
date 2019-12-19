'''
Validate Binary Search Tree
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

class BST_Validate:
    def __init__(self):
        self.inorder_list = []                
    
    # A utility function to do inorder tree traversal to validate binary tree 
    def inorder_traversal(self,root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val)
        self.inorder_list.append(root.val)
        self.inorder_traversal(root.right)
        return inorder_list

INT_MAX = 4294967296
INT_MIN = -4294967296

# Retuns true if the given tree is a BST and its values 
def isBSTUtil(node, mini, maxi):
        if node is None:
            return True
        
        if node.val < mini or node.val > maxi:
            return False
        
        return (isBSTUtil(node.left, mini, node.val -1) and isBSTUtil(node.right, node.val+1, maxi)) 
    
if __name__ == "__main__":
    # Binary Tree Construction
    bt = Node(50)
    bt.left = Node(40)
    bt.right = Node(80)
    bt.left.left = Node(20)
    bt.left.left.left = Node(10)
    bt.right.left = Node(70)
    bt.right.right = Node(90)

    #Method 1
    b = BST_Validate()
    output = b.inorder_traversal(bt)
    if output == sorted(output):
        print("BST")
    else:
        print("Not BST")

    #Method 2
    #o(n) best approach
    if isBSTUtil(bt, INT_MIN, INT_MAX):
        print("BST")
    else:
        print("Not BST")
