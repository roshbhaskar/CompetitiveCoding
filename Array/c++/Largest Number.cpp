bool cmp_condition (string s1,string s2)
{
    if(s1+s2>s2+s1){
        return true;
    }
    return false;
}

string Solution::largestNumber(const vector<int> &A) {
    //creating a vector will the same contents as A but of string type
    vector<string>B;
    bool flag = 0;
    
    for(int i=0;i<A.size();++i){
        B.push_back(to_string(A[i]));
        if(A[i]!=0)
        {
            flag=1;
        }
    }
    // if the whole vector A is just zeros then 0 is the largest number
    if(!flag)
    {
        return "0";
    }
    //cmp with the condition
    sort(B.begin(),B.end(),cmp_condition);
    
    //joining the elements in the vector B to a string
    string result = "";
    for( auto& str : B)
    {
        result+=str;
    }
    return result;
}
