# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [-1, None]
        def recur(root, depth):
            if root is None:
                return [False, False]
            nonlocal res
            # for every node, see this node could reach for three and 12
            left_search = recur(root.left, depth + 1)
            right_search = recur(root.right, depth + 1)
            find_p = left_search[0] or right_search[0] or (root.val == p.val)
            find_q = left_search[1] or right_search[1] or (root.val == q.val)
            if find_p and find_q and depth > res[0]:
                res = [depth, root]
            return [find_p, find_q]
        recur(root, 0)
        return res[1]
        