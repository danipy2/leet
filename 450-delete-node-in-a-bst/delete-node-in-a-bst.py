# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findsiccessor(r):
            cur = r
            while cur.left:
                cur = cur.left
            return cur.val
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val <key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            root.val = findsiccessor(root.right)
            root.right = self.deleteNode(root.right,root.val)
          
        return root

        
    
        