# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        before=dummy
        while True:
            kth=before
            for i in range(k):
                kth=kth.next
                if kth is None:
                    return dummy.next
           
            after=kth.next
            prev=after
            curr = before.next
            
            while curr!=after:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            temp=before.next
            before.next=kth
            before = temp









        

