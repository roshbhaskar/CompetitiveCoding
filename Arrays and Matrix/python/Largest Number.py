def cmp():
    class compare_():
        def __init__(A, A_val): # A is self here
            A.val = A_val
        
        def __lt__(A, B): #less than function
            str1 = str(A.val)
            str2 = str(B.val)
            if str1+str2> str2+str1: 
                return True
            return False
    return compare_
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
        
        