class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #return 
        #self.bfs(root)
        
        res=[]
        def bfs(root):
            if root:
                res.append(root.val)
                for child in root.children:
                    bfs(child)
        bfs(root)
        
        return res
