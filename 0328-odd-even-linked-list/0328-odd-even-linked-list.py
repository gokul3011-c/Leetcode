# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        pos = 1
        stackev = []
        stackodd = []
        while temp:
            if pos % 2 == 0:
                stackev.append(temp.val)
            else:
                stackodd.append(temp.val)
            temp = temp.next
            pos +=1
          
        newHead = None
        tail = None                  
        for i in stackodd:
            newnode = ListNode(i)
            if newHead is None:
                newHead = newnode
                tail = newnode
            else:
                tail.next = newnode
                tail = newnode

        for i in stackev:
            newnode = ListNode(i)
            if newHead is None:
                newHead = newnode
                tail = newnode
            else:
                tail.next = newnode
                tail = newnode

        return newHead
        