/*
Fibonacci numbers using memoization

TC: O(n)
*/

int fibo(int n , int* memo)
{
    if(n<=0)
    {
        return 0;
    }
    else if (n==1)
    {
        return 1;
    }
    else if(memo[n]>0)
    {
        return memo[n];
    }
    memo[n]= fibo(n-1,memo)+fibo(n-2,memo);
    return memo[n];
}
void fibonacci(int n)
{
    int memo[n+1];
    memset(memo,0,sizeof(memo));
    for(int i=0;i<n;i++)
    {
        cout << fibo(i,memo);
    }
}

