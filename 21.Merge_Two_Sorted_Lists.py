# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        root:ListNode = ListNode()
        main_tr:ListNode = root
        while list1 and list2:
            if list1.val < list2.val:
                main_tr.next = list1
                main_tr = main_tr.next
                list1 = list1.next
            else:
                main_tr.next = list2
                main_tr = main_tr.next
                list2 = list2.next
        if list1: main_tr.next = list1
        elif list2: main_tr.next = list2
        return root.next
