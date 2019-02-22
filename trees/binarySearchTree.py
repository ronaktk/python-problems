# Binary Search Tree
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        if self.data==data:
            return False
        elif data<self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left=Node(data)
                return True
        elif data>self.data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right=Node(data)
                return True
                
    def preorder(self):
        if self:
            print(str(self.data),end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
         
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data),end=' ')
            if self.right:
                self.right.inorder()
                
    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data),end=' ')
    
    def height(self):
        if self.left and self.right:
            return 1+max(self.left.height(),self.right.height())
        elif self.left:
            return 1+self.left.height()
        elif self.right:
            return 1+self.right.height()
        else:
            return 1
            
    def find(self,data):
        if self.data==data:
            return True
        elif self.data>data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        elif self.data<data:
            if self.right:
                return self.right.find(data)
            else:
                return False
    
class BST(object):
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
            
    def preorder(self):
        print()
        if self.root!=None:
            print("Preorder")
            self.root.preorder()
    
    def inorder(self):
        print()
        if self.root!=None:
            print("Inorder")
            self.root.inorder()
            
    def postorder(self):
        print()
        if self.root!=None:
            print("Postorder")
            self.root.postorder()
            
    def height(self):
        print()
        if self.root:
            return self.root.height()
        else:
            return False
        
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
        
tree=BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(20)
tree.preorder()
tree.inorder()
tree.postorder()
h=tree.height()
print("Height of the tree: ")
print(h)
f=tree.find(3)
print(f)