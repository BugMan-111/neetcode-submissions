# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # perform bfs algo
        queue = [(root, 1)]
        result = []
        while len(queue) > 0:
            # queue FIFO
            current_root, current_level = queue.pop(0)  
            if current_root is None:
                continue
            if len(result) < current_level:
                result.append([])
            queue.append((current_root.left, current_level + 1))
            queue.append((current_root.right, current_level + 1))
            result[current_level - 1].append(current_root.val)

        return result



        