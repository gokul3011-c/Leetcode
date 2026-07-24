# Definition for Singly Linked List
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        mid = 0
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        mid = count//2
        for i in range(mid):
            head = head.next
        
        return head






