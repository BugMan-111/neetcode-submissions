# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.l = []
        self.inorder_traversal(root)
        # check if the l is sorted
        for i in range(0, len(self.l) - 1):
            if self.l[i] >= self.l[i + 1]:
                return False
        return True

    def inorder_traversal(self, root):
        if root is None:
            return 
        self.inorder_traversal(root.left)
        self.l.append(root.val)
        self.inorder_traversal(root.right)
        