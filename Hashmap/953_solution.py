class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        l1 = {c:i for i,c in enumerate(order)}
        #print(l1)
        
        l2 = [[l1[i] for i in word] for word in words]
        #print(l2)
        #print(sorted(l2))
        
        if l2==sorted(l2):
            return True
        else:
            return False
