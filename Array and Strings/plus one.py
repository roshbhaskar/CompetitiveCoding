'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

TC : O(n)
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)
        if(i==0):
            return []
        carry = 1
        while(i>0):
            j=i-1
            x = digits[j] + carry
            print('x',x)
            print('digit',digits[j])
            if(x<10):
                digits[j]=x
                return digits
            else:
                digits[j]=x%10
                carry = x//10
                print('digit',digits[j])
            i-=1    
            
        if(carry):
            digits = [carry] + digits
        return digits