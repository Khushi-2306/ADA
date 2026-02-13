# binary tree node
class node :
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

#inorder trasversal(left-root-right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

#preorder trversal (root-left-right)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

#postorder transversal(left-right-root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

#level order transversal(breadth first search)
def level_order(root):
    if root is None:
        return 
    
    queue=[]
    queue.append(root)

    while queue:
        current=queue.pop(0)
        print(current.dat, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("inorder transversal:")
inorder(root)

print("\n preorder transversal:")
preorder(root)

print("\n postorder transversal:")
postorder(root)

print("\n level order transversal:")