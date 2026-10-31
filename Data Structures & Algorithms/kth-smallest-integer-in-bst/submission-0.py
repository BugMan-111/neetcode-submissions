# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def recur(root, result):
            if root is None:
                return
            recur(root.left, result)
            result.append(root.val)
            recur(root.right, result)

        recur(root, result)
        return result[k - 1]
        