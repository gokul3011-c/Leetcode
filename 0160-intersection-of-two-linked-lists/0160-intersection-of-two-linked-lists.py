# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = headA
        count = 0
        while temp:
            count+=1
            temp = temp.next
        
        count1 = 0
        temp = headB
        while temp:
            count1+=1
            temp = temp.next
        
        N= abs(count - count1)

        if count > count1:
            temp = headA
        else:
            temp = headB
        i = 0
        while i < N:
            temp = temp.next
            i+=1
        if count > count1:
            tempA = temp
            tempB = headB
        else:
            tempB = temp
            tempA = headA

        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        return None
        