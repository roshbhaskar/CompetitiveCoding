/*
Find the intersection of two different sized arrays a and b.

TC : (aloga + bloga)
where a and b are sizes of the array.

*/
#include <iostream>
#include <algorithm>
#include<vector>
int binsearch(int i , int *a,int min,int max)
{
    if(max<min)
    {
        return 0;
    }
    int mid = (min+max)/2;
    if(a[mid]==i)
    {
        return a[mid];
    }
    if(a[mid]>i)
    {
        return binsearch( i , a,min, mid-1);
    }
    if(a[mid]<i)
    {
        return binsearch( i , a,mid+1, max);
    }
}

void intersection(int a[], int b[],int n,int m)
{
    
    std::vector<int> result;
    for(int i = 0;i<m;++i)
    {
        if(binsearch(b[i],a,0,n-1))
        {
            result.push_back(binsearch(b[i],a,0,n-1));
        }
    }
    for(int i : result)
    {
        std::cout << i;
    }
}

int main() {
    int a[] = {2,1,5,3,8};
    int b[] = {7,2,1,4,3,8};
    std::sort(a,a + 5);
    intersection(a,b,5,6);

    return 0;
}
