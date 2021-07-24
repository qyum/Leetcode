class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        #...............hashmap solution.......................
        #str1=str
        #x=sorted(order)
        #print(x)
        
        
        counter = collections.Counter(str)
        #print(counter)
        out=""
        
        for i in range(len(order)):
            if order[i] in counter:
                #print(order[i],counter[order[i]])
                out+=(order[i]*counter[order[i]])
                del counter[order[i]]
        
        print(out)
        print(counter)
        if len(counter):
            for key, val in counter.items():
                print(key,val)
                out += (key*val)
        
        
        #print(out)
        return out
        
        
        
