/*
Given two sorted arrays, find the number of elements in common. 
The arrays are the of different length and each has all distinct elements.
*/

//TC - O(m+n)
#include <iostream>
using namespace std;

int intersection(int a[],int b[],int n,int m)
{

    //int n = sizeof(b)/sizeof(b[0]);
    int i=0;
    int j=0;
    int count=0;
    while(i<n && j<m)
    {
         if(a[i]>b[j])
        {
            j++;
        }
        if(a[i]<b[j])
        {
            i++;
        }
        if(a[i]==b[j])
        {
            count++;
            i++;
            j++;
        }
       
    }
   
    return count;
}
int main() {
 
    int a[] = {1,3,4,7};
    int b[] = {2,3,5,7,8};
    
    cout << intersection(a,b,4,5);
    
    return 0;
}