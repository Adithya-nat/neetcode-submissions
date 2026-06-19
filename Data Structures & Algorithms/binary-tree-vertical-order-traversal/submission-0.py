# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        max_col = 0
        min_col = 0

        queue = deque()
        queue.append((root, 0))
        res = []

        while queue:
            node, col = queue.popleft()

            cols[col].append(node.val)

            max_col = max(max_col, col)
            min_col = min(min_col, col)

            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col + 1))
        
        for i in range(min_col, max_col+1):
            res.append(cols[i])
        
        return res
            
        