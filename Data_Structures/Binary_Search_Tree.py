class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root == None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if new_node.val < curr.val:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right

    def inOrder(self,root):
        if root :
            self.inOrder(root.left)
            print(root.val, end = " ")
            self.inOrder(root.right)

    def preOrder(self,root):
        if root :
            print(root.val, end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root :
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val, end = " ")
    
obj = BST()

obj.insert(4)
obj.insert(6)
obj.insert(32)
obj.insert(64)
obj.insert(2)

inRes = obj.inOrder(obj.root)
print(inRes)

preRes = obj.preOrder(obj.root)
print(preRes)

postRes = obj.postOrder(obj.root)
print(postRes)