class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        max_count=0
        zero=0
        while(end<len(nums)):#sliding window
            if(nums[end]==0):
                zero+=1
            while(zero>k):
                if(nums[start]==0):
                    zero-=1
                start+=1
            max_count= max(max_count,end-start+1)
            end+=1
        return max_count