Approach:
1)Initially enqueue the root node in the list,then start swapping the child node level by level through the loop.
      Swapping Step And Traversing:
                i)Pop out the parent node from queue(FIFO),then swap the two child nodes of parent Node           
                ii)After swapping two nodes,then add current nodes(swap nodes) to the queue.
                iii)And start traversing to go next level of tree(depth of tree)
2)Now continuously hit step 1 until the queue is not getting empty.
                         

#......................................code solution..........................
@Queue Solution with Time Complexity O(N) and Space Complexity O(N)

  class Solution:  
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue=[root]
        while len(queue)>0:
            currentNode=queue.pop(0)
            
            if currentNode is None:
                continue
            self.swapLeftRight(currentNode)
            queue.append(currentNode.left)
            queue.append(currentNode.right)
        return root
    
    def swapLeftRight(self,currentNode):
        currentNode.left,currentNode.right=currentNode.right,\
                                            currentNode.left
