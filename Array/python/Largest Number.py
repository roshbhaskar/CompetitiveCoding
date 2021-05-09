def cmp():
    class K():
        def __init__(A, value_of_a): # A is self here
            A.val = value_of_a
        
        def __lt__(A, B):
            a = str(A.val)
            b = str(B.val)
            if a+b > b+a: 
                return True
            return False
    return K
class Solution:
    # @param A : tuple of integers
    # @return a strings
    
        
    def largestNumber(self, A):
        B=[]
        flag = 0
        for int_ in A:
            B.append(str(int_))
            if(int_!=0):
                flag=1
        
        if(flag==0):
            return "0"
            
        B.sort(key=cmp())
        
        result = ""
        for str_ in B:
            result+=str_
        
        return result
        
        