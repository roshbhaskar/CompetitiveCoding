'''
Implement pow function for a^b where -ve <= b <= +ve is the range for b

Input : 2 2
Output : 4

Input : 2 -2
Output :0.25

TC : O(b)
'''
def mypow(a,b):
    if(b==0):
        return 1
    if(b<0):
        print(pow_neg(a,b))
    else:
        print(pow_pos(a,b))
        
def pow_pos(a,b):
    if(b==0):
        return 1
    if(b==1):
        return a
    else:
        x = pow_pos(a,b-1)
        curr = x*a
        return curr
        
def pow_neg(a,b):
    if(b==0):
        return 1
    if(b==-1):
        return 1/a
    else:
        x = pow_neg(a,b+1)
        curr = x*1/a
        return curr

mypow(2,-3)