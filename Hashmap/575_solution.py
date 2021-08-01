class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        #if all(i==candyType[0] for i in candyType):
            #return 1
        #else:
            #return len(candyType)/2
        df=len(list(set(candyType)))
        print(df)
        x=len(candyType)/2
        print(x)
        
        if x>df:
            return df
        else:
            return x
