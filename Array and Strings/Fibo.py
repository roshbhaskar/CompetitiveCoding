'''
Fibonacci numbers from 0 to n.

TC : O(n)
Using memoization
'''

def fibo(n):
    memo = [0 for i in range(n+1)]
    for i in range(0,n+1):
        print(fibo_memo(i,memo))
        
def fibo_memo(n,memo):
    if(n<=0):
        return 0
    elif(n==1):
        return 1
    elif(memo[n]>0):
        return memo[n]
    memo[n] = fibo_memo(n-1,memo)+fibo_memo(n-2,memo)
    return memo[n]
    
fibo(5)