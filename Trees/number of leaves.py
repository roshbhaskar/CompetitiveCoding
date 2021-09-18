def countLeaves(root):
    # Code here
    count=0
    if(root==None):
        return 0
    if(root.right==None and root.left==None):
        return 1
    count += countLeaves(root.left) + countLeaves(root.right) # sums the count
    return count # returns the count to previous calls