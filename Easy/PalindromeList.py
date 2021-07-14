def palindromeLinkedList(head):
    '''
    先遍历链表，找到链表的中间值，然后将后半部分反转（之前的反转算法）
    然后依次比较前半部分和后半部分的值
    '''
    fast = slow = head
    # find the mid node--slow
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        # nxt = slow.next
        # slow.next = node
        # node = slow
        # slow = nxt
        cur = slow
        slow = slow.next
        cur.next = node
        node = cur
    
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

def isPalindrome(head):
    '''
    先找链表的中间值，然后用一个栈保存后半部分的值，然后出栈，比较前半部分
    '''
    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    
    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    
    return True