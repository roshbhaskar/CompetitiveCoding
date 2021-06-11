/*
A permutation, also called an “arrangement number” or “order,”
 is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.
 A string of length n has n! permutation. 
*/

// TC : O(N * N!)
#include <bits/stdc++.h>
using namespace std;

void permutation(string a, int left, int right)
{
    // Same algo for strings and array permutations
    if (left == right)
        cout << a <<endl; // print the permutation of the string
    else
    {
       
        for (int i = left; i <= right; i++)
        {
            swap(a[left], a[i]); // built in function
            permutation(a, left+1, right);
            //backtracking
            swap(a[left], a[i]);
        }
    }
}

int main()
{
	string str = "abcd";
	int n = str.size();
	permute(str, 0, n-1);
	return 0;
}