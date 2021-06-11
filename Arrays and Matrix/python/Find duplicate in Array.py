class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        check = 0
        for i in A:
            if(check&(1<<i)>0):
                return i
            else:
                check|=(1<<i)
        return -1
