#hash solution

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cp=collections.defaultdict(int)
        
        for cpd in cpdomains:
            current=cpd.split(" ")
            #print(current)
            count=int(current[0])
            domain=current[1]
            print(domain)
            
            cdm=""
            print(domain.split(".")[::-1])
            for sub in domain.split(".")[::-1]:
                if cdm=="":
                    cdm=sub
                else:
                    #print(sub)
                    cdm=sub+"."+cdm
                cp[cdm]+=count
                
        #print(cp)
        #print(cdm)
        res=[]
        for key in cp.keys():
            res.append(str(cp[key])+" "+key)
        return res
