# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append([root, 0])
        res = []
        level = 0
        current = []
        while queue:
            node, current_level = queue.popleft()
            if current_level > level:
                if len(current) > 0:
                    res.append(current[-1])
                current = []
                level = current_level
            if node is not None:
                current += [node.val]
            if node:
                queue.append([node.left, current_level + 1])
                queue.append([node.right, current_level + 1])
        if len(current) > 0:
            res.append(current[-1])

        return res
        