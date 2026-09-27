# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        def rec_sol(root):
            if not root:
                return
            
            rec_sol(root.left)
            print(root)
            
            rec_sol(root.right)
            res.append(root.val)
        rec_sol(root)
        return res