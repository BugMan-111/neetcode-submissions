# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_max = 0
        def recur(root):
            if root is None:
                return
            nonlocal current_max
            recur(root.left)
            recur(root.right)
            current = self.height(root.left) + self.height(root.right)
            current_max = max(current_max, current)

        recur(root)
        return current_max
    
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
        