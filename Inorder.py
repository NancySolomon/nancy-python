class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                  self.left=node(data)
                else:
                  self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                  self.right=node(data)
                else:
                  self.right.insert(data)
        else:
            self.data=data

    def printtree(self):
        if self.left:
           self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()

    def inorder(self,k):
        res=[]
        if k:
           res=self.inorder(k.left)
           res.append(k.data)
           res=res+self.inorder(k.right)
        return res  


k=node(5)
k.insert(8)
k.insert(10)
k.printtree()  
print(k.inorder(k))      