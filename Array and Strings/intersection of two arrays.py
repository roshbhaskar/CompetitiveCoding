'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

TC : O(N*logN)

'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        for i in nums1:
            x= self.binSearch(nums2,i,0,len(nums2)-1)
            if(x>-1):
                res.append(i)
                nums2.pop(x)
        return res
        
    def binSearch(self,nums2,key,mini,maxi):
        if(mini>maxi):
            return -1
        mid=(mini+maxi)//2
        if(nums2[mid]==key):
            return mid
        if(nums2[mid]<key):
            return self.binSearch(nums2,key,mid+1,maxi)
        if(nums2[mid]>key):
            return self.binSearch(nums2,key,mini,mid-1)