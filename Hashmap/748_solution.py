class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        res={}
        lp=licensePlate.lower()
        d={}
        for i in lp:
            if i.isalpha():
                d[i]=lp.count(i)
                
        
        print(d)
        for i in words:
            j=i.lower()
            #print(j)
            c=0
            for k in d.keys():
                #print(j.count(k),d[k])
                if j.count(k)<d[k]:
                    c=1
                    break
            if c==0:
                m=res.get(len(j),[])
                print(m,j)
                res[len(j)]=m+[j]
        
        print(res,list(res.keys()))
        #print(min(list(res.keys())))
        #print(res[(min(list(res.keys())))])
        
        return res[(min(list(res.keys())))][0]
                
