# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def recur(root, passed):
            if root is None:
                return 0
            if (root, passed) in cache:
                return cache[(root, passed)]
            res = 0
            if passed:
                res = recur(root.left, False) + recur(root.right, False)
            else:
                res = max(root.val + recur(root.left, True) + recur(root.right, True), recur(root.left, False) + recur(root.right, False))
            cache[(root, passed)] = res
            return res
        
        return recur(root, False )
        