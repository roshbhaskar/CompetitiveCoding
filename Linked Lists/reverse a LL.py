'''
Given a linked list of N nodes. The task is to reverse this list.But with O(1) space complexity.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.

TC : O(N)

'''


class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        
        if(head==None):
            return
        #one element
        if(head.next==None):
            return head
        #two element
        if(head.next.next==None):
            ptr=head.next
            ptr.next = head
            head.next= None
            return ptr
        
        #using 3 pointers for 3 or more elements
        ptr1=head
        ptr2=head.next
        ptr3=ptr2.next
        
        ptr1.next=None
        while(ptr3):
            ptr2.next=ptr1
            ptr1=ptr2
            ptr2=ptr3
            ptr3=ptr3.next
        ptr2.next = ptr1
        
        return ptr2