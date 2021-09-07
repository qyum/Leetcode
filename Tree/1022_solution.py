#recursive solution
#time complexity O(N) and space complexity O(1)
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def cal(node,temp):
            
            if node is None:
                return 0
            
            temp=temp*2+node.val
            
            if node.left is None and node.right is None:
                return temp

            return cal(node.left,temp) + cal(node.right,temp)
                
            
            
        return cal(root,0)
