# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val == key:
            if root.left and root.right:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
            elif root.left:
                return root.left
            else:
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root

