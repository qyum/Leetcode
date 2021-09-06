#recursive bfs

 
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        
        def dfs(node, parent, level):
            if not node :
                return None

            if node.val in [x, y]:
                
                if not self.found:
                    self.found = (parent, level)
                else:
                    self.result = (parent != self.found[0] and level == self.found[1])
                
            dfs(node.left, node.val, level + 1)                    
            dfs(node.right, node.val, level + 1)
            
        self.result = None
        self.found = None
        dfs(root, None, 0)
            
        return self.result
