'''
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def compression(string):
    count=0
    string=string+'#' #adding a special symbol to consider all the elements while comparison
    result=[]
    for i in range(1,len(string)):
        if(string[i-1]!=string[i]):
            count+=1
            result.append(string[i-1])
            result.append(str(count))
            count=0
        if(string[i-1]==string[i]):
            count+=1
    
    print("".join(result))
    
compression('aabcccccaaab')