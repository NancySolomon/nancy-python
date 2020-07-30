class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def printroot(self):
        print(self.data)
k=node(10)
k.printroot()