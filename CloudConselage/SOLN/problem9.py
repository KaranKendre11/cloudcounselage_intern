INT_MAX = 4294967296
INT_MIN = -4294967296
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def isBST(node):
    return (isBSTUtil(node,INT_MIN,INT_MAX))

def isBSTUtil(node,mini,maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data -1) and
            isBSTUtil(node.right, node.data +1, maxi))

root = Node(2)
root.left = Node(1)
root.right = Node(3)

if (isBST(root)):
    print("True")
else:
    print ("False")
