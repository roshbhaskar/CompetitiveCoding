'''
Replace the whitespaces with %25

Input:
'Mr John Smith     isBT '
15

Output:
'Mr%25John%25Smith%25isBT%25'

TC : O(n)
SP : O(n)
'''
# since strings are immutable in python 
# doing string concatentaion takes O(n^2) time 
# hence converting into list and joining only when necessary
def replace(string,n):
    flag=1
    count=n
    for i in string:
        if(i==' ' and flag==1):
            count+=3
            flag=0
        if(i!=' '):
            flag=1
    string_new = ['1' for n in range(count)]
    
    index=0
    for i in range(len(string)):
        if(string[i]!=' '):
            string_new[index]=string[i]
            index+=1
            flag=1
        if(string[i]==' ' and flag==1):
            string_new[index]='%'
            string_new[index+1]='2'
            string_new[index+2]='5'
            index+=3
            flag=0
            
    print("".join(string_new))
    
replace('Mr John Smith     isBT ',15)