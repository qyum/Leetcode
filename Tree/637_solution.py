class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        avg, nodes = [], [root]
        #print(nodes)
        while nodes:
            #print(nodes)
            avg.append(sum(node.val for node in nodes)/len(nodes))
            print(avg)
            
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                if node.left:
                    #print(node.left)
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return  avg
