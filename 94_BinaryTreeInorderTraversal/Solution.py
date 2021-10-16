# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if root:
            stack = self.inorderTraversal(root.left) # recursive left
            stack.append(root.val) # append root
            stack += self.inorderTraversal(root.right) # recursive right
        return (stack)
        