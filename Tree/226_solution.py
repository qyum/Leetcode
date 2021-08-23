
#recursive,BFs solution
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #helper function
        def dfs(root):
		#check for null
            if root is None:
                return None
            
			#get the rest of the left & right side
            l = dfs(root.left)
            r = dfs(root.right)
            
			#swap the pointers  & return the roots
            root.left = r
            root.right = l
            return root

        return dfs(root)
