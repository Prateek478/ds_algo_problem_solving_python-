'''
Invert a binary tree.
Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

def bfs_invert(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    
    while len(queue):
        #print(queue[0].val)
        temp = queue.pop(0)        
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
        temp.left, temp.right = temp.right, temp.left

def invert_rec(self, node):
	if node is None:
		return
	self.invert_rec(node.left)
	self.invert_rec(node.right)
	node.left, node.right = node.right, node.left

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

if __name__ == "__main__":
    # Binary Tree Construction
    bt = Node(50)
    bt.left = Node(40)
    bt.right = Node(80)
    bt.left.left = Node(20)
    bt.left.left.left = Node(10)
    bt.right.left = Node(70)
    bt.right.right = Node(90)
    
    inorder_traversal(bt)
    bfs_invert(bt)
    print("\n")
    inorder_traversal(bt)
    invert_rec(bt)
    print("\n")
    inorder_traversal(bt)

    
