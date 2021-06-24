'''
Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9.


Example 1:

Input:
N = 8
Output:
8
Explanation:
After removing natural numbers which contains
digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
and 8th number is 8.
Example 2:

Input:
N = 9
Output:
10
Explanation:
After removing natural numbers which contains
digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10
and 9th number is 10.

'''
import math

class Solution:
    def findNth(self,N):
        num = 0
        units = 0
        while(N):
           
            temp = int(math.pow(10,units) * (N%9))
            num += temp
            units+=1
            N = N//9
        # print(num,string)
        return num