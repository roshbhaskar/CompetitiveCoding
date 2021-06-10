'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permu = []
        hashmap = {n:0 for n in nums}
        
        for n in nums:
            hashmap[n]+=1
            
    
        def dfsonArry():
            if(len(nums)==len(permu)):
                result.append(permu.copy()) #adding a copy of permu since permu will be changed later on
                return
            
            for n in hashmap:
                if(hashmap[n]>0): #if the number is available for choosing
                    permu.append(n)
                    hashmap[n]-=1
                    
                    dfsonArry()
                    
                    #backtrack
                    hashmap[n]+=1
                    permu.pop()
        
        dfsonArry()
        return result