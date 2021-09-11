#recursive bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,s,ans):
        
        if node is None:
            return False
        if self.traversal(node.left,s,ans):
            node.left=None
        
        if self.traversal(node.right,s,ans):
            node.right=None
            
        if node.val in s:
            if node.left and node.left.val not in s:
                ans.append(node.left)
            if node.right and node.right.val not in s:
                ans.append(node.right)
        
            return True
        
     
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        s=set()
        for i in to_delete:
            s.add(i)
        
        ans=[]
        
        if not self.traversal(root,s,ans):
            ans.append(root)
        
        return ans
            
        
        
