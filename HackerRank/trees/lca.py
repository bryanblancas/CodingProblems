class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    
	if root is None:
        return None
    
    #Si ambos valores son menores, sólo tiene caso irnos hacia la izquierda
    #porque sólo ahí estará el padre de los dos valores
    #               4
    #       2             7
    #    1     3       6
    #  v1 = 1, v2 = 3  está a la izquierda del root (4)

    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    
    #si ambos valores son mayores, sólo tiene caso irnos hacia la derecha
    #               4
    #       2             7
    #    1     3       6     8
    #  v1 = 6, v2 = 8  está a la derecha del root (4)
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)

    #Si no paso los if's anteriores, entonces root está entre estos dos valores (v1 y v2)
    #por tanto, este es el LCA
    return root
    
tree = BinarySearchTree()
#t = int(input())
"""
6
4 2 3 1 7 6
1 7
"""
t = 6

#arr = list(map(int, input().split()))
arr = [4,2,3,1,7,6]

for i in range(t):
    tree.create(arr[i])

#v = list(map(int, input().split()))
v = [1,7]

ans = lca(tree.root, v[0], v[1])
#print (ans.info)
