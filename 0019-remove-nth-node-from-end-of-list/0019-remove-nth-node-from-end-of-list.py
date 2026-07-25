# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        
        pos = count - n + 1
        if pos == 1:
            return head.next
        i = 1
        temp = head
        while i < pos - 1:
            temp = temp.next
            i+=1
        
        temp.next = temp.next.next
        return head
        