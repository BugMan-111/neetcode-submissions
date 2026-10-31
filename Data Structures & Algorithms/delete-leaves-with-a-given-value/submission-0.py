# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def check(r):
            if r is None:
                return None
            if r.left is None and r.right is None and r.val == target:
                return None
            r.left = check(r.left)
            r.right = check(r.right)

            # if r becomes a new leaf and have a target value
            if r.left is None and r.right is None and r.val == target:
                return None

            return r

        return check(root)
        