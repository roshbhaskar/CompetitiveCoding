'''
Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] 
is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular 
cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a huge number, return this modulo 10^9 + 7.

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. 
After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9

'''
#TC - O(nlogn)
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        h_=len(horizontalCuts)
        v_=len(verticalCuts)
        
        mod = math.pow(10,9) + 7
        
        max_w = max(verticalCuts[0],w-verticalCuts[v_-1])
        max_h = max(horizontalCuts[0],h-horizontalCuts[h_-1])
        
        for i in range(1,v_):
            max_w = max(max_w,verticalCuts[i]-verticalCuts[i-1])
        
        for j in range(1,h_):
            max_h = max(max_h,horizontalCuts[j]-horizontalCuts[j-1])
            
        return int((max_w*max_h)%mod)
       
