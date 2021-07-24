class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        #pat=sources
        #out=""
        #for pat,target,indice in zip(sources, targets,indices):
            #print(pat)
            #st=
            #KMPSearch(pat, s,target,indice)
            #print(st)
            #out+=st
        #return out
        
        ans = s
        sums = 0
        for idx, source, target in sorted(zip( indices, sources, targets)):
            #print(s[idx:idx + len(source)])
             
            if source != s[idx:idx + len(source)]:
                continue
            print(ans[0:idx+sums] + ans[idx+sums:].replace(source, target, 1))
            ans = ans[0:idx+sums] + ans[idx+sums:].replace(source, target, 1)
            sums += len(target) - len(source)
            print(sum)
        return ans
