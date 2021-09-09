'''
String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring 
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one 
call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat").

TC : O(N)
'''

def rotation(str1,string):
    n_string=str1+str1
    j=0
    for i in range(len(n_string)):
        #print(string[j],n_string[i],string[j]==n_string[i])
        if(j==len(string)):
            return True
        if(string[j]==n_string[i]):
            j+=1
            #print("j",j)
        elif(string[j]!=n_string[i]):
            j=0
    if(j==len(string)):
        return True
    return False
    
print(rotation('erbottlewate','waterbottle'))