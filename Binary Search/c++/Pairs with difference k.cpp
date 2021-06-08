/*
 Given an array of distinct integer values, count the number of pairs of integers that 
have difference k. For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference 
k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9).
*/
#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
bool binsearch(int a[],int key,int min,int max)
{
    if(max<min)
    {
        return false;
    }
    
    int mid = min + (max-min)/2;
    if(a[mid]==key)
    {
        return true;
    }
    if(a[mid]>key)
    {
        return binsearch(a,key,min,mid-1);
    }
    if(a[mid]<key)
    {
        return binsearch(a,key,mid+1,max);
    }
    
}

void print(std::vector<std::tuple<int, int>> const & data) {
    for(auto row : data) {
    	std::cout << std::get<0>(row) << " : " << std::get<1>(row) << "\n";
    	}
}

void pairsk(int a[],int n,int k)
{
    std::vector<std::tuple<int,int>> result;
    std::sort(a,a+n);
    for(int i=0; i<n; ++i)
    {
        int val = a[i];
        if(binsearch(a,val-k,0,n-1))
        {
            result.emplace_back(val,val-k);
        }
        
        if(binsearch(a,k-val,0,n-1))
        {
            result.emplace_back(val,k-val);
        }
        
        if(binsearch(a,val+k,0,n-1))
        {
            result.emplace_back(val,val+k);
        }
    }
   print(result);
} 


int main() {
    int a[] = {2,3,8,4,1,5};
    pairsk(a,6,1);
    return 0;
}
