/*
Finding sqrt in O(logn) time without the built in function
*/
int root(int n , int min ,int max)
{
    if(max<min)
    {
        return -1;
    }
    int guess = (min+max)/2;
    if(guess*guess == n)
    {
        return guess;
    }
    else if(guess*guess < n)
    {
        return root(n,guess+1,max);
    }
    else if(guess*guess > n)
    {
        return root(n,min,guess-1);
    }
}
int main()
{
    cout<<root(4,1,4);
}
