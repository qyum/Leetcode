#dictionary solution
#Tim complexity o(n) and space complexity o(1)

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
        
  
        #for i in st1:
            #if i not in st2:
                #out.append(i)
        #for j in st2:
            #if j not in st1:
                #out.append(j)
        #print(out)
        #return out
        
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
