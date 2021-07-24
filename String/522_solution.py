class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        #s=(len(strs))
        #print(s)
        
        def fn(p, s): 
            """Return True if p is a subsequence of s."""
            ss = iter(s)
            print(ss)
            #print(all(c in ss for c in p))
            return all(c in ss for c in p)
        
        st=strs.sort(key=len, reverse=True)
        print(st)
        for i in range(len(strs)): 
            if not any(fn(strs[i], strs[ii]) for ii in range(len(strs)) if i != ii): 
                return len(strs[i])
        
        
        return -1
