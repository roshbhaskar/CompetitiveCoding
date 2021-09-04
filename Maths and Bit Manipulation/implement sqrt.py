'''
finding sqrt of n without math function 

TC: O(logN)
'''

def sqrt(n):
    print(mysqrt(n,1,n))
    
def mysqrt(n,start,end):
    if(start>end):
        return -1
    guess = (start+end)//2
    #this can be easily extended to other roots as well. For cube root multiply guess 3 times
    if(guess*guess==n):#if(guess*guess*guess==n):
        return guess
    elif(guess*guess < n):#elif(guess*guess*guess < n):
        return mysqrt(n,guess+1,end)
    elif(guess*guess > n):#elif(guess*guess*guess > n):
        return mysqrt(n,start,guess-1)
sqrt(8)