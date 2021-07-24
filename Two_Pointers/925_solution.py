class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif i == 0 or name[i - 1] != typed[j]:
                print(name[i-1],typed[j])
                return False
        
        return i == len(name)
