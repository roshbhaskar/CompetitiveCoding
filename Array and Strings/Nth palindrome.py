'''
Given k find the Nth palindrome from k.

Input:
11 5

Output:
66

'''

def nthPalindrome(num,N):
    count=0
    result=0
    num=num+1
    while(count!=N):
        num1 = num
        temp = 0
        while(num1):
            r = num1%10
            temp = temp*10 + r #flip the digits
            num1/=10 
        if(temp==num1):
            count+=1
            result = num1 
        num+=1 #next number

    return result
