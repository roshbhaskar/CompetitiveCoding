'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

TC : O(N) [almost]
'''
class Solution:
    def twoSum(self, fake: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(fake)):
            if(fake[i] in hashmap):
                return [hashmap[fake[i]],i]
            else:
                hashmap[target-fake[i]]=i