#inorder traversal

class Solution:
    
    def __init__(self):
        self.res=0
        
    def traversal(self,node,min_,max_):
        if node is None:
            return None
        else:
            minV=min(min_,node.val)
            maxV=max(max_,node.val)
            self.res=max(self.res,abs(node.val-minV),abs(node.val-maxV))
            
            self.traversal(node.left,minV,maxV)
            self.traversal(node.right,minV,maxV)
            
            
            
            
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #print(root.val)
        self.traversal(root,root.val,root.val)
        
        return self.res
