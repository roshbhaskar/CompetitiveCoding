'''
Find unique pairs that have k difference in an array of size N. 

Input : 
[2,1,4,5,3]
2

Output:
[(2,4),(5,3),(1,3)]

TC : O(N)
SC : O(N)
'''
def pairs(N,k):
    result = []
    hashmap = {n:0 for n in N}
    for i in N:
        hashmap[i]+=1
    
    if(k==0):
        for i in hashmap:
            if(hashmap[i]>=2):
                result.append([i,i])
    for i in N:
        # for duplicate pairs 
        # if((i+k) in hashmap):
        #     result.append([i,i+k])
        
        # without duplicate pairs
        if((i-k) in hashmap):
            result.append([i,i-k])
    print(result)

pairs([2,1,4,5,3],2)