'''
Finding all the permutaions of a given string.

Input : ABC
Output : 
ABC
ACB
BAC
BCA
CBA
CAB

TC : O(n*n!)
'''

def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

def all_permu(a,left,right):
    if(left==right):
        print("".join(a))
    else:
        for i in range(left,right):
            swap(a,left,i)
            all_permu(a,left+1,right)
            swap(a,left,i)
            
def permutation(string):
    strr = list(string)
    all_permu(strr,0,len(strr))
    #print("y")
permutation("ABC")