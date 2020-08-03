""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def isBST(root, mini, maxi):
    if root is None:
        return True
    
    if root.data < mini or root.data > maxi:
        #print("root.data "+str(root.data)+" !< "+str(mini)+" ooo !>"+str(maxi))
        return False
    
    #print("-----------------")
    #print("estoy en "+str(root.data))
    #print("mandaré root.left,"+str(mini)+","+str(root.data - 1))
    #print("mandaré root.right,"+str(root.data-1)+","+str(maxi))
    return (isBST(root.left, mini, root.data-1) and isBST(root.right, root.data+1, maxi))
    
def checkBST(root):
    return (isBST(root, -4294967296, 4294967296))