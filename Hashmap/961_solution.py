class Solution(object):
	def repeatedNTimes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#dictionary solution

		d={}
		for i in nums:
			d[i]=d.get(i,0)+1

		for key,value in d.items():
			if value>=2:
				return key
		return False
