class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(-1)
        cur = h
        
        cur1 = l1
        cur2 = l2
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        if cur1:
            cur.next = cur1
        
        if cur2:
            cur.next = cur2
        
        return h.next