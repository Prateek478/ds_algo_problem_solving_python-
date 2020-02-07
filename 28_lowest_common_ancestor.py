'''
Today’s Problem: Lowest Common Ancestor in a Binary Tree

Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.

Following is definition of LCA from Wikipedia:
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both 
n1 and n2 as descendants (where we allow a node to be a descendant of itself).
'''
class Node: 
    # Constructor to create a new binary node 
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  

def findPath( root, path, k): 
    if root is None: 
        return False
      
    path.append(root.key)   
    if root.key == k :
        return True
  
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    path.pop() 
    return False
  
def findLCA(root, n1, n2): 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2.   
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    # print(path1, path2)
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  
# Python program to find LCA of n1 and n2 using one 
# This function returns pointer to LCA of two given 
def findLCA1(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    if root.key == n1 or root.key == n2: 
        return root  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA1(root.left, n1, n2)  
    right_lca = findLCA1(root.right, n1, n2) 
    
    if left_lca and right_lca: 
        return root
    
    return left_lca if left_lca is not None else right_lca 
  
# Driver program to test above function 
# Let's create the Binary Tree shown in above diagram 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,))) 
print ("LCA(4, 6) = %d" %(findLCA(root, 4, 6))) 
print ("LCA(3, 4) = %d" %(findLCA(root,3,4))) 
print ("LCA(2, 4) = %d" %(findLCA(root,4, 2))) 

# Method 2 traverse the tree only once
print("LCA1(4, 5) = {}".format(findLCA1(root, 4, 5,).key)) 
print ("LCA1(4, 6) = %d" %(findLCA1(root, 4, 6).key)) 
print ("LCA1(3, 4) = %d" %(findLCA1(root,3,4).key)) 
print ("LCA1(2, 4) = %d" %(findLCA1(root,4, 2).key)) 
