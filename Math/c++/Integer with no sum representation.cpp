/*
Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.


Example 1:

Input: 
N = 6
array[] = {1, 10, 3, 11, 6, 15}
Output: 
2
Explanation:
2 is the smallest integer value that cannot 
be represented as sum of elements from the array.
Example 2:

Input: 
N = 3
array[] = {1, 1, 1}
Output: 
4
Explanation: 
1 is present in the array. 
2 can be created by combining two 1s.
3 can be created by combining three 1s.
4 is the smallest integer value that cannot be 
represented as sum of elements from the array.


Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
1 ≤ array[i] ≤ 109
Array may contain duplicates.
*/

class Solution
{   
public:
    long long smallestpositive(vector<long long> array, int n)
    { 
 
        long long num=1; // number that cannot be represented as a sum
        sort(array.begin(),array.end());
        for(int i=0; i<array.size();i++)
        {
            if(array[i]<=num)
            {
                num+=array[i];
            }
            else{
                break;
            }
        }
        
        return num;
    } 
};