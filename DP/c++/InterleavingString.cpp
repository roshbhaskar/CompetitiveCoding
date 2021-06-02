/*
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

*/

//TC- O(n^2) SC - O(n^2)
class Solution {
public:
    int dp[101][101];
    
    bool check(string s1,string s2,string s3,int n,int m,int sum){
        if(sum==0){
            return 1;
        }
        if(dp[n][m]!=-1){
            return dp[n][m];
        }
        
        int a=0;
        int b=0;
        
        if(n-1>=0 and s1[n-1]==s3[sum-1]){
            a=check(s1,s2,s3,n-1,m,sum-1);
        }
        if(m-1>=0 and s2[m-1]==s3[sum-1]){
            b=check(s1,s2,s3,n,m-1,sum-1);
        }
        
        return dp[n][m] = a or b;
        
    }
    
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.length();
        int m = s2.length();
        if(m+n!=s3.length()){
            return false;
        }
        dp[n][m];
        memset(dp,-1,sizeof(dp));
        int res= check(s1,s2,s3,n,m,s3.length());
        if(res==1){
            return true;
        }
        else{
            return false;
        }
    }
};
