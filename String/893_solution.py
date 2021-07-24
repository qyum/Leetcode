class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s=set()
        for st in words:
             
            #even index
            ev=st[1::2]
            #odd index
            od=st[::2]
            sort_ev_od="".join(sorted(ev)+sorted(od))
            print(sort_ev_od)
            s.add(sort_ev_od)
            
        return len(s)
