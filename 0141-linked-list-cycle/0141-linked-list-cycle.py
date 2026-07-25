# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        node = {}
        if head is None or head.next is None:
            return False
        while temp:
            if temp in node:
                return True
            node[temp] = 1
            temp=temp.next
        return False       