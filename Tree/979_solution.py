#dfs+recurisve solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def calculateBalance(node):
            nonlocal moves
            
            if not node:
                return 0
            
            leftBalance = calculateBalance(node.left)
            nodeBalance = node.val - 1
            rightBalance = calculateBalance(node.right)
            moves += abs(leftBalance) +abs(rightBalance)
            
            #return moves
            return leftBalance + nodeBalance + rightBalance
        moves = 0
        calculateBalance(root)
        
        print(moves)
        return moves
