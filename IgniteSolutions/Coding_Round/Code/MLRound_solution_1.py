class Solution():
	"""
		Generally we could use standard algorithms  like quicksort,insertion sort etc..

	 	But here  all numbers are in range from 1 to 100.

	 	So create buckets from range 1 to 100 and store counts of every number 

	 	algorithm is o(n) complexity with o(n) extra space

	"""

	def  __init__(self):
		
		self.list = self.populate_list()

		self.bucket = [0 for num in range(0,101)]

		self.sorted_list = []

		self.sort()

		self.bucket_to_list()

	def populate_list(self):

		from random import randint

		len_ = round(1e7)

		return [randint(1,100) for i in range(len_)]

	def sort(self):

		for number in self.list:
			self.bucket[number]+=1

	def bucket_to_list(self)->None:

		from functools import reduce

		"""
			concat lists that are made from bucket frequencies 
		"""
		length = len(self.bucket)

		self.sorted_list =  reduce(lambda x,y : x+y ,[[number]*self.bucket[number] for number in range(1,length)])

	

	def is_sorted(self):
		"""
		verify if list is sorted 
		"""

		l = round(1e7)

		assert len(self.list)==len(self.sorted_list)

		for index in range(l-1):
			if self.sorted_list[index+1]<self.sorted_list[index]:
				return False
		return True


ans=Solution()

assert ans.is_sorted()==True
