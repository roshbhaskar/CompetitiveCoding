int Solution::maxSubArray(const vector<int> &A) {
    
    int max_arr = -1001; //  maximum of entire array
    int max_i = 0; // maximum till the ith index
    
    for(int i = 0; i<A.size() ; ++i)
    {
        max_i = max_i + A[i];
        if(max_i < A[i])
        {
            max_i = A[i];
        }
        if(max_arr < max_i)
        {
            max_arr = max_i;
        }
    }
    
    return max_arr;
}
