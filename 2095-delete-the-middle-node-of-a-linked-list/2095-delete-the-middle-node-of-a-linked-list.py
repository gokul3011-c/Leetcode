# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp= temp.next
        if count == 1:
            return None
        count = count // 2
        i=1
        temp = head
        while i<count:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        return head
            
        
        