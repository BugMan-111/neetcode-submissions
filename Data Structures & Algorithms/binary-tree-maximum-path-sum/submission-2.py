# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def recur(root):
            if root is None:
                return 0
            left_max = recur(root.left)
            right_max = recur(root.right)
            res[0] = max(res[0], root.val, root.val + left_max, root.val + right_max, left_max + right_max + root.val)
            return max(root.val , left_max + root.val , right_max + root.val )
        recur(root)
        return res[0]