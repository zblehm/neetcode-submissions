# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # save the next node before reversing the pointer
            next = curr.next
            # set pointer to the current node to previous (reverse the pointer)
            curr.next = prev
            # shift all nodes down the linked list one position
            prev = curr
            curr = next
        return prev
        
        