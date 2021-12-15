#leetcode premium problem(489)
#logger rate limiter problem
#O(n)T |O(N)S

Class logger:
	def __init__(self):
		self.hashMap={}
	def shouldPrintMessage(self,message,timeStamp):
		if message not in self.hashMap:
			self.hashMap[message]=timeStamp
			return True
		elif timeStamp>=self.hashMap[message]+10:
			self.hashMap[message]=timeStamp
			return True
		else:
			return False
			

