class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        self.ptr=0
        
        
        def helper(root):

            if root is None:
                return 0
            l=helper(root.left)
            r=helper(root.right)

            if l+r>self.ptr:
                self.ptr=l+r
            
            #print(1+max(l,r))
            return 1+max(l,r)
        
        helper(root)
        #print(self.ptr)
        return self.ptr
