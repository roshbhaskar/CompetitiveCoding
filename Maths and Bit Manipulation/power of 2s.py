'''
Print out all the powers of 2 between 1 to n

Input : 5
Output : 2 4

Input : 14
Output : 2 4 8

TC : O(logN)
'''
def power2(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        x = power2(n//2)
        current = x*2
        print(current)
        return current #so that for the next iteration current is set to prev times 2
power2(12)