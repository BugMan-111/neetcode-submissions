# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [1]
        def recur(root):
            if root is None:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            local_max = 1 + left + right
            res[0] = max(res[0], local_max)
            return max(left + 1, right + 1)
        recur(root)
        return res[0] - 1
        
     