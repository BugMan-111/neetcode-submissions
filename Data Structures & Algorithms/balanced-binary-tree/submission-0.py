# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def recur(root):
            if root is None:
                return 0

            global result
            left = recur(root.left) + 1
            right = recur(root.right) + 1

            if abs(left - right) > 1:
                self.result = False

            return max(left, right)

        recur(root)
        return self.result 
                    