# Given the head of a linked list, remove the n^(th) node from the end of the list and return its head.

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
        