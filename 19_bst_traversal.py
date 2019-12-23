class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

class Depth_First_Search:
    def __init__(self):
        self.value = []

    def preorder_traversal(self,root):
        if root is not None:
            #print(root.val)
            self.value.append(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
        
    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            #print(root.val)
            self.value.append(root.val)
            self.inorder_traversal(root.right)
    
    def postorder_traversal(self,root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            #print(root.val)
            self.value.append(root.val)

'''Depth first search(inorder, preorder and postorder) and Breath first search Binary tree traverse'''

def Bfs_traverse(root):
    if root is None:
        return
    queue = []
    output = []
    queue.append(root)
    
    while len(queue)>0:
        #print(queue[0].val)
        output.append(queue[0].val)
        temp = queue.pop(0)
        
        if temp.left is not None:
            queue.append(temp.left)
        
        if temp.right is not None:
            queue.append(temp.right)
    return output

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
    b = Depth_First_Search()
    b.preorder_traversal(bt)
    print("preorder : {}".format(b.value))
    b = Depth_First_Search()
    b.inorder_traversal(bt)
    print("inorder : {}".format(b.value))
    b = Depth_First_Search()
    b.postorder_traversal(bt)
    print("postorder : {}".format(b.value))
    print("depth first search : {}".format(Bfs_traverse(bt)))
    
