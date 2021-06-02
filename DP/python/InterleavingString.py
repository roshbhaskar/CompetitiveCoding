'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 
Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
'''

#TC- O(n^2) SC - O(n^2)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        sum_= len(s3)
        if(n+m!=sum_):
            return False
        dp= [[-1 for i in range(m+1)] for j in range(n+1)]
        
        def solve(s1,s2,s3,n,m,sum_):
            if(sum_==0):
                return 1
            if(dp[n][m]!=-1):
                return dp[n][m]
            a=b=0
            
            if(n-1>=0 and s1[n-1]==s3[sum_-1]):
                a=solve(s1,s2,s3,n-1,m,sum_-1)
            if(m-1>=0 and s2[m-1]==s3[sum_-1]):
                b=solve(s1,s2,s3,n,m-1,sum_-1)   
            dp[n][m]= (a or b)
            return dp[n][m]
        
        
        
        res = solve(s1,s2,s3,n,m,sum_)        
        
        if(res):
            return True
        return False
        
