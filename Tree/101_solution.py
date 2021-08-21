#BFS solution

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is not None:
            return self.util(root.left, root.right)
        
    
    def util(self, left, right):
        if left is not None and right is not None:
            if left.val == right.val:
                return self.util(left.right, right.left) and self.util(left.left, right.right)
            
            else:
                return False
        
        if left is None and right is None:
            return True
        
        return False
