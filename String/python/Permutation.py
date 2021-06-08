'''
Given a smaller string 's' and a bigger string 'b', design an algorithm to find all permutations of the shorter string within the longer one.
Print the starting location of each permutation.

Example
s: abbc 
b: cbabadcbbabbcbabaabccbabc

Output
0 6 9 11 19 20

Explaination 
at index 0 cbab -> is a permutation of abba

'''

def check(s,b):
    s = ''.join(sorted(s))
    b = ''.join(sorted(b))
    if(s==b):
        return True
    return False

def permutations(s,b):
    
    length=0
    
    result = []
    while(length<len(s)-len(b)):
        value_s=0
        if(check(s[length:length+len(b)],b)):
        
            result.append(length)
        
        length+=1
    print(result)
        
if __name__ == "__main__":
    
    s="abbc"
    b="cbabadcbbabbcbabaabccbabc"
    print(len(b))
    permutations(b,s)
