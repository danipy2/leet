# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def reverse_inorder(node):
            nonlocal total
            if node:
                reverse_inorder(node.right)
                total += node.val
                node.val = total
                reverse_inorder(node.left)
        reverse_inorder(root)
        return root


        