'''
Find out duplicates in the input characters without using extra space.
Chars can be uppercase or lowercase alphabets

Input:
abcdesff

Output:
False

TC : O(n)
'''

def duplicates(char):
    check = 0
    for i in char:
        val = ord(i)-ord('A')
        if((check&(1<<val)) > 0):
            return False
        check|=(1<<val)
        
    return True
    
print(duplicates('aAbcdesfB'))