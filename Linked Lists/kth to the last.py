'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.Length of the Linked list is not given.

TC : O(N)
SC : O(1)
'''

def kthLast(LL,k):
    ptr1=LL
    ptr2=LL
    for i in range(k):
        ptr2=ptr2.next
        
    while(ptr2):
        ptr2=ptr2.next
        ptr1=ptr1.next
        
    return ptr1
    
        
