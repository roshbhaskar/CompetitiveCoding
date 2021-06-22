/*
Given a fraction. Convert it into a decimal. 
If the fractional part is repeating, enclose the repeating part in parentheses.
 

Example 1:

Input: numerator = 1, denominator = 3
Output: "0.(3)"
Explanation: 1/3 = 0.3333... So here 3 is 
recurring.
Example 2:

Input: numerator = 5, denominator = 2
Output: "2.5"
Explanation: 5/2 = 2.5
*/

#include<bits/stdc++.h>
using namespace std;

class Solution{
	public:
	string fractionToDecimal(int numerator, int denominator) {
	   
	    string ans = "";

        int rem_index;
        ans = ans + to_string(numerator/denominator);
        int rem = numerator % denominator;
        
        if(rem == 0)
        {
            return ans;
        }
        
        if(rem != 0)
        {
            ans += ".";
        }
        
        unordered_map<int,int> map;
        int len = ans.size();
        while(rem != 0 && map.find(rem) == map.end())
        {
            map[rem] = len;
            numerator = rem * 10;
            ans = ans + to_string(numerator/denominator);
            rem = numerator % denominator;
            len = len+1;
        }
        if(rem != 0)
        {
            rem_index = map[rem];
            ans = ans.substr(0,rem_index)+"("+ans.substr(rem_index,ans.size()-rem_index+1)+")";
        }
        
        return ans;
	}
};