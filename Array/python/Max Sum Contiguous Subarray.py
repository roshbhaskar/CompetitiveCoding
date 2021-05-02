class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_arr = -1001 #max of the whole array
        max_i = 0 #max till the ith index
        
        for i in range(len(A)):
            max_i+=A[i]
            if(max_i<A[i]):
                max_i = A[i] #changing max to current ith value
            if(max_arr < max_i):
                max_arr=max_i #changing overall max of the array
        return max_arr