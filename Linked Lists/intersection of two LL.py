'''
Given two linked lists, the task is to complete the function findIntersection(), that returns the intersection of two linked lists. Each of the two linked list contains distinct node values.

Example 1:

Input:
LinkedList1: 9->6->4->2->3->8
LinkedList2: 1->2->8->6
Output: 6 2 8

TC : O(n+m)
'''


class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        head = None
        ptr = head
        inter={} #so basically dic takes less look up than list 
        while(head2!=None):
            inter[head2.data] = 1
            head2=head2.next
            
        while(head1!=None):
            if(head1.data in inter): 
                if(head):
                    ptr.next=Node(head1.data)
                    ptr=ptr.next
                else:
                    head = Node(head1.data)
                    ptr = head
            head1=head1.next
                
        # print(inter)  
        return head