'''
Finding all the permutaions of a given string.

Input : 112
Output : 
112
121
211

O(n*n!)

'''

def unique_permu(a):
    
    result = []
    permu = []
    
    hashmap = {n:0 for n in a} #gets rid of all the duplicates 
    
    for i in a:
        hashmap[i]+=1
        
    def dfs():
        
        if(len(permu)==len(a)):
            cop = permu.copy()
            result.append("".join(cop))
            return
        
        for i in hashmap:
            if(hashmap[i]>0):
                permu.append(i)
                hashmap[i]-=1
                dfs()
                permu.pop()
                hashmap[i]+=1
    
    dfs()
    print(result)
    
def permutation(string):
    strr = list(string)
    unique_permu(strr)
    
permutation("112")