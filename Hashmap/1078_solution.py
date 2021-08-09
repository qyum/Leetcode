class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        text = text.split()
        res = []
        
        for i in range(0, len(text) - 2):
            
            if text[i] == first:    
                if text[i + 1] == second:
                    res.append(text[i + 2])    
                
        return res
