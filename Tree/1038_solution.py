class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root,0)
        return root
    
    def helper(self,root,val):
        if root is None:
            return val
        else:
            outvalue=self.helper(root.right,val)
            root.val +=outvalue
            
            return self.helper(root.left,root.val)
