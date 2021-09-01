class Solution(object):
    
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        
        return self.traversal(root,low,high)
    
    def traversal(self,root,low,high):
        if root is None:
            return None
        
        if root.val<low:
            return self.traversal(root.right,low,high)
        elif root.val>high:
            return self.traversal(root.left,low,high)

        root.left=self.traversal(root.left,low,high)
        root.right=self.traversal(root.right,low,high)
        
        return root
