'''
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
 
Input: Tact Coa 
Output: True (permutations: "taco cat'; "atco eta·; etc.) 

def palindrome -
TC: O(N)
SC: O(N)

'''
def palindrome(string):
    string = string.lower()
    Hash = {n:0 for n in string}
    for i in string:
        Hash[i]+=1
       
    count=0 
    for c in Hash:
        if(Hash[c]%2==1 and c!=' '):
            count+=1
            
    return count<=1

print(palindrome('TactCoa'))