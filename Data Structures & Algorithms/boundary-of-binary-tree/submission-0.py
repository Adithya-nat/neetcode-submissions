# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]
        
        curr = root.left

        def isLeaf(root):
            if not root.right and not root.left:
                return True
            return False

        while curr:
            if not isLeaf(curr):
                res.append(curr.val)
            
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
        def addLeaves(root):
            if not root:
                return
            if isLeaf(root):
                res.append(root.val)
                return
            
            addLeaves(root.left)
            addLeaves(root.right)
        
        addLeaves(root.left)
        addLeaves(root.right)

        curr = root.right
        rb = []

        while curr:
            if not isLeaf(curr):
                rb.append(curr.val)
            
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        res.extend(reversed(rb))

        return res





        