# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def pst(t):
            if t:
                pst(t.left)
                pst(t.right)
                arr.append(t.val)
        pst(root)
        return arr