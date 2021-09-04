'''
Find intersection of 2 arrays.

Input:
[2,3,1,4,6]
[5,1,2,8,3]

Output:
[1,2,3]

TC: O(N*logN)

'''

def intersection(a,b):
    a=sorted(a)
    b=sorted(b)
    i,j=0,0
    result = []
    while(i<len(a) and j<len(b)):
        if(a[i]==b[j]):
            result.append(a[i])
            i+=1
            j+=1
        elif(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            j+=1
    print(result)
    
intersection([2,3,1,4,6],[5,1,2,8,3])