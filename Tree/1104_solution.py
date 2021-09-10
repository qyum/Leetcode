class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        level = int(log2(label))
        #print(level)
        compl = 3*2**level - 1 - label # complement 
        #print(compl)
        
        ans = []
        while label: 
            ans.append(label)
            label //= 2
            compl //= 2
            print(label,compl)
            label, compl = compl, label
            
    
        return ans[::-1]
