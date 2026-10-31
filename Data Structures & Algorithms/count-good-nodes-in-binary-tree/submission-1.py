# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        return self.helper(root, root.val)

    def helper(self, root, prev_max):
        if root is None:
            return 0
        print(prev_max)
        if root.val >= prev_max:
           return self.helper(root.left, root.val) + self.helper(root.right, root.val) + 1
        return self.helper(root.left, prev_max) + self.helper(root.right, prev_max)
        