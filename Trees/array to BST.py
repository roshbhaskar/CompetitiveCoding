'''
convert an array to a BST of minimum height

TC : O(N*logN)
'''

def arrToBST(arr):
    arr.sort()
    return createBST(arr,0,len(arr)-1)

def createBST(arr,min,max):
    if(min>max):
        return
    mid = (min+max)//2
    node=createNode(arr[mid]) #creates a tree node
    node.left = createBST(arr,min,mid-1)
    node.right = createBST(arr,mid+1,max)
    return node