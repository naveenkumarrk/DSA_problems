class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    queue.append(temp.left)
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    queue.append(temp.right)
    
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.val, end = " ")
            self.inOrder(node.right)

    def preOrder(self,node):
        if node:
            print(node.val,end = " ")
            self.preOrder(node.left)
            self.preOrder(node.right)


    def search(self,node):
        if node is None:
            return
        

    def levelOrder(self,node):
        if node is None:
            return
        queue = [node]
        total = 0 
        while queue:
            temp = queue.pop(0)
            total += temp.val
            print(temp.val, end =" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        print(total)

        

obj = BT()
obj.insert(1)
obj.levelOrder(obj.root)
print()

obj.insert(2)
obj.levelOrder(obj.root)
print()

obj.insert(3)
obj.levelOrder(obj.root)
print()

obj.insert(4)
obj.levelOrder(obj.root)
print()

obj.insert(5)
obj.levelOrder(obj.root)
print()

obj.insert(6)
obj.levelOrder(obj.root)
print()

obj.insert(7)
obj.levelOrder(obj.root)
print()
        
        