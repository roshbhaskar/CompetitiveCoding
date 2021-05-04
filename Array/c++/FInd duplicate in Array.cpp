int Solution::repeatedNumber(const vector<int> &A) {
    
    int check = 0; // can be implemented using the checker bit : as in python code
    vector<int>temp(A); // Using O(n) space
    sort(temp.begin(),temp.end());
    
    for(int i=0;i<temp.size()-1;i++)
    {
        if(temp[i]==temp[i+1])
        {
            return temp[i];
        }
    }
    return -1;
}
