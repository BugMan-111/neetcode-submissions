# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(root):
            nonlocal res
            if root is None:
                return 0
            # find the longest path from left and right
            left = recur(root.left)
            right = recur(root.right)

            # calculate the local maximum dia and compare with global(stored) maximum 
            res = max(res, left + right + 1)

            # calculate the comparative longest path between the current left and right
            return max(left + 1, right + 1)

        recur(root)
        return max(res - 1, 0)
            
