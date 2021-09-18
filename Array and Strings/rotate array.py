'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

TC : O(n)
SP : O(1)
'''
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reverse full list 
        #reverse 0 to k-1
        #reverse k to len(list)-1
        # nums=nums[::-1]
        k=k%len(nums)
        start=0
        end=len(nums)-1
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        
        start=0
        end=k-1
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
            
        start=k
        end=len(nums)-1
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1