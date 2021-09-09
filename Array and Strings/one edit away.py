'''
One Away: There are three types of edits that can be performed on strings: insert a character,remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
Input :
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bae -> false

TC : O(max(m,n))
'''

def oneAway(string1,string2):
    if(len(string1)==len(string2)):
        return Replace(string1,string2)
    if(len(string2)+1==len(string1)):
        return Insert(string2,string1)
    if(len(string2)-1==len(string1)):
        return Insert(string1,string2)
    return False
    
def Replace(string1,string2):
    count=0
    # print('Replace')
    for i in range(len(string1)):
        if(string1[i]!=string2[i]):
            count+=1
    return count==1

def Insert(string1,string2):
    count=0
    i,j=0,0
    # print('Insert',string1,string2)
    while(i<len(string1) and j<len(string2)):
        if(string1[i]!=string2[j]):
            j+=1 #since the min len string is always string 1 whos indexing is i
            count+=1
        elif(string1[i]==string2[j]):
            i+=1
            j+=1
    # print(count)
    return count==1
    
print(oneAway('pale','pxe'))