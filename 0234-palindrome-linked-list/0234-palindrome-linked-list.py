# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        flag = 0
        stack = []
        count  = 0
        if head is None or head.next is None:
            return True
        while(temp):
            count+=1
            stack.append(temp.val)
            temp = temp.next
        temp = head
        for i in range(count//2):
            if temp.val == stack.pop():
                temp = temp.next
                flag = 1
            else:
                flag = 0
                break
        if(flag == 1):
            return True
        else:
            return False

        