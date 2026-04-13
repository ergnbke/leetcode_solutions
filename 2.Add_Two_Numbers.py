# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and l1.next == None:
            return l2
        if l2.val == 0 and l2.next == None:
            return l1
        hoba:ListNode = ListNode()
        temmp:ListNode = hoba
        exess:int = 0
        l1_next = l1.next
        l2_next = l2.next
        if l1:
            exess += l1.val
        if l2:
            exess += l2.val
        hoba.val = exess % 10
        exess //= 10
        while 1:
            tempp:ListNode = ListNode()
            if l1_next:
                exess += l1_next.val
                l1_next = l1_next.next
            if l2_next:
                exess += l2_next.val
                l2_next = l2_next.next
            if l1_next == None and l2_next == None and exess == 0:
                break
            tempp.val = exess % 10
            exess //= 10
            temmp.next = tempp
            temmp = tempp

        return hoba
