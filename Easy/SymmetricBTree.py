# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, p, q):
        if not p and not q:
            return True
        elif not p and q or p and not q:
            return False
        else:
            return p.val == q.val and self.is_mirror(p.left, q.right) and self.is_mirror(p.right, q.left)
        

    def isSymmetric(self, root):
        """
        队列
        :param root:
        :return:
        """

        if not root:
            return True

        node_queue = [root.left, root.right]    # 在空队列中加入左子树和右子树

        while node_queue:
            left = node_queue.pop(0)            # 依次弹出两个元素
            right = node_queue.pop(0)

            if not right and not left:          # 如果均为空，继续下一个循环
                continue
            if not right or not left:           # 如果只有一个为空，返回False
                return False

            if left.val != right.val:           # 都非空，再判断值是否相等
                return False

            node_queue.append(left.left)        # 将两个左右子树的左右子树逆序加入队列
            node_queue.append(right.right)
            node_queue.append(left.right)
            node_queue.append(right.left)

        return True
