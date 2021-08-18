def reverseList(head):
    '''
    iterative solution
    这里有一个有意思的地方，head=head.next必须在前面，不能放在最后。
    因为如果不立即改变head的指向，那么head和cur将会指向同一个节点。
    在执行cur.next=prev(None)之后，head.next也指向了prev，就会跳出循环。
    '''
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    
    return prev

'''
递归的形式执行
'''

def help_reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)

def reverseList_2(head):
    return help_reverse(head)

