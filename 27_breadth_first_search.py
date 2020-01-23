# Binary tree Breadth first/Level Order search
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        
    def bfs(self, node):
        list = []
        list.append(node)
        while len(list):
            node = list.pop(0)
            print(node.data)
            if node.left:
                list.append(node.left)
            if node.right:
                list.append(node.right)
                
from collections import defaultdict

# BFS in graph works as FIFO means same as queue, unlike Depth First search FILO
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, v):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(v)
        visited[v] = True
        while len(queue):
            s = queue.pop(0)
            print(s),
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    
    bt.bfs(bt.root)
    
    #Graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print
    g.bfs(2)
