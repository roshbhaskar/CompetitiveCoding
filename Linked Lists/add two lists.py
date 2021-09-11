'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912. 
FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
Output: 9 -> 1 -> 2. That is, 912.

TC : O(max(m,n))

'''

def sumList(LL1,LL2):
    LL = createNone()
    head=LL
    carry=0
    #add till the lengths match
    while(LL1 and LL2):
        num = LL1.data + LL2.data + carry
        if(num>9):
            carry = num//10
            LL.data = num%10
        else:
            carry = 0
            LL.data = num
        LL1=LL1.next
        LL2=LL2.next
        LL.next=createNode()
    
    #LL1 is longer
    if(LL1):   
        while(LL1):
            num = LL1.data + carry
            if(num>9):
                carry = num//10
                LL.data = num%10
            else:
                carry = 0
                LL.data = num
            LL1=LL1.next
            LL.next=createNode()
            
    #LL2 is longer
    if(LL2):
        while(LL2):
            num = LL2.data + carry
            if(num>9):
                carry = num//10
                LL.data = num%10
            else:
                carry = 0
                LL.data = num
            LL2=LL2.next
            LL.next=createNode()
            
    #when both are empty but carry is present 
    if(carry>0 and (not LL1) and (not LL2)):
        LL.data = carry
    LL.next = None
    
    return head
        