#Inorder traversal and hash solution
#O(N)T|O(N)S

from collections import defaultdict,Counter

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
    
        def traverse(node,li):
          
            if node is None:
                return 
            traverse(node.left,li)
            li.append(node.val)   
            traverse(node.right,li)   
         
        convertToList_array=[]          
        traverse(root,convertToList_array)
       
        countMostFrequentElement=Counter(convertToList_array) 
        max_value=max(countMostFrequentElement.values())
        
        mostFrequentElement=[]
        for key,value in countMostFrequentElement.items():
            if max_value==value:
                mostFrequentElement.append(key)

        return  mostFrequentElement
         
