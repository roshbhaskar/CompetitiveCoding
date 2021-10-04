class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        q=collections.deque()
        start=0
        end=0
        while(end<len(nums)):
            while q and nums[q[-1]]<nums[end]:
                q.pop()
            q.append(end)

            if(start>q[0]):
                q.popleft()
            if(end-start+1==k):
                result.append(nums[q[0]])
                start+=1
            end+=1
        return result