'''
Find inorder successor of a given node in a BST

TC : O(logN)
'''

def inorderSuccessor(root,node):
    if(root.right):
        return checkRight(root.right)
    
    succ= None
    while(root!=None):
        if(root.data>node.data):
            succ=root
            root=root.left
        elif(root.data<node.data):
            root=root.right
        else:
            break
    
    return succ

def checkRight(root):
    while(root.right!=None):
        root=root.right
    return root
    