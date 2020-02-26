# Creting tree
class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

#Finding length of tree
def len_tree(root):
    if root is None:
        return 0
    ltree = len_tree(root.left)
    rtree = len_tree(root.right)
    
    return ltree+1 if ltree>rtree else rtree+1


# Get the tree depth Using Level Order Traversal
def max_width_tree(root):
    if root is None:
        return 0
    tree_len = len_tree(root)
    max_width = 0
    
    for i in range(1,tree_len+1):
        width = level_width(root,i)
        max_width = max(width, max_width)    
    return max_width


def level_width(root,level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return level_width(root.left,level-1)+level_width(root.right,level-1)
    
# Get the tree depth Using Level Order Traversal
def max_width_tree_queue(root):
    if root is None:
        return 0
    q = []
    max_width = 0
    
    q.insert(0,root)
    
    while q != []:
        count = len(q)
        max_width = max(max_width,count)
        while count != 0:
            count  = count - 1
            item = q.pop()

            if item.left is not None:
                q.insert(0,item.left)
            if item.right is not None:
                q.insert(0,item.right)
        
    return max_width

# Creating tree
root=node(1)
root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)
root.right = node(3)
root.right.right = node(8)
root.right.right.left = node(6)
root.right.right.right = node(7)

print("length of tree : {}".format(len_tree(root)))
print("Max tree width : {}".format(max_width_tree(root)))
print("Max tree width using queue : {}".format(max_width_tree_queue(root)))
