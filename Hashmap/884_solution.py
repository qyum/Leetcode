#dictionary solution
#Time complexity o(n) and space complexity o(n)

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
        st1=s1.split(" ")
        #print(st1)
        st2=s2.split(" ")
      
        d={}
        for i in st1:
            d[i]=d.get(i,0)+1
        for j in st2:
            d[j]=d.get(j,0)+1
            
        #print(d) 
        #print(d) 
        out=[]
        for key,value in d.items():
            if value==1:
                out.append(key)
        return out          
