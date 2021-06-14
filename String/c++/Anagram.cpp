/*
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to 
change to make the two substrings into anagrams of one another.

Example S = abccde

Break S into two parts: 'abc' and 'cde'. Note that all letters have been used,
 the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to 
 have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Sample Input
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output
3
1
-1
2
0
1

*/

#include <bits/stdc++.h>

using namespace std;

int minChanges(int arr1 [],int arr2[])
{
    int count = 0;
    for(int i =0;i<26;i++)
    {
        int val = abs(arr1[i]-arr2[i]);
        count+=val;
    }
    return count/2;
}

void charCounts(string s,int arr[])
{
    
    for(int i=0;i<s.size();i++)
    {
        int pos = int(s[i]) - int('a');
        arr[pos]+=1;
    }
} 

int anagram(string s) {
    if(s.size()%2==1)
    {
        return -1; //since odd lenght of string cant be divided into anagram
    }
    int pos = s.size()/2;
    string str1 = s.substr(0,pos); // 0 + pos
    string str2 = s.substr(pos,s.size()-1); // from pos till len-1
    
    int arr1[26] = {0};
    int arr2[26] ={0};

    charCounts(str1,arr1);
    charCounts(str2,arr2);

    return minChanges(arr1,arr2);
}
