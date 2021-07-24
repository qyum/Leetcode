#from ipaddress import ip_address, IPv6Address         

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        def checkv4(s):
            try:
                return str(int(s))==s and 0<=int(s)<=255
            except:
                return False
        
        
        def checkv6(s):
            if len(s)>4:
                return False
            try:
                int(s,16)
                return True
            except:
                return False
              
        
        ip4=IP.split(".")
        ip6=IP.split(":") 
        if len(ip4)==4 and all(checkv4(i) for i in ip4):
            return "IPv4"
        if len(ip6)==8 and all(checkv6(i) for i in ip6):
            return "IPv6"
        
        return "Neither" 
