class Solution:
    def maxDepth(self, root: 'Node') -> int:
    
        
        if root is None:
            return 0
        else:
            max_dep=0
            for i in root.children:
                max_dep=max(max_dep,self.maxDepth(i))
            
            #print(max_dep)
            return max_dep+1
        
