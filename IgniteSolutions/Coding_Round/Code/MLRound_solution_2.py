class A_and_B_Test():
	def __init__(self ,filepath):
		self.file_path = filepath

		self.user_interactions = []

		self.b_design_users = []

		self.a_design_users = []

		self.parse_json()

	def parse_json(self):

		"""
	    	searches.json file is a newline delimited json file. 
			Parse line by line and convert each  line into dict in python.
			users have is_instructor flag set to False
		"""

		import json
		try:
			nd_json_file=open(self.file_path,"r")

			self.user_interactions = [json.loads(content) for content in nd_json_file]

			self.b_design_users = [user for user in self.user_interactions if user['uid']%2!=0 and user['is_instructor']==False]  # B test users 

			self.a_design_users = [user_0 for user_0 in self.user_interactions if user_0['uid']%2==0 and user_0['is_instructor']==False] # A test users
		except FileNotFoundError:
			print("provide proper filepath for seraches.json at command line or change value for dataset_filepath in solution_2.py ")
			import sys
			sys.exit()

		"""
		Q1.	Did more users use search feature in b design 
		"""
	def q1_answer(self):
		
		"""
			Returns 'B design' if users are more for b design 
			Assumption: Consider a user is valid if search_count is atleast one.
		"""
		
		verify_validity =  lambda  dict1 :  True if dict1['search_count']>=1 else False

		users_b = [verify_validity(each_user) for each_user in self.b_design_users]

		users_a = [verify_validity(each_user)  for each_user in self.a_design_users]

		"""
		Count number of users for each design
		"""
		c1 = sum(users_b)
		c2 = sum(users_a)

		return "Yes" if c1>c2 else "No"

		"""
		Q2 . Did users search more often in B design
		"""
	def q2_answer(self):
		
		"""
		if sum of logins are more in b design then b design has more frequent 
		"""

		count1 = [user_0['login_count'] for user_0 in self.b_design_users]
		count2 = [user_1['login_count'] for user_1 in self.a_design_users]

		return "Yes" if count1>count2 else "No"

if __name__ == '__main__':

	from sys import argv
	dataset_filepath = None
	try:
		dataset_filepath = argv[1]
	except IndexError:
		print("Assumming searches.json is in same folder as solution_2.py\n")
		dataset_filepath = "./searches.json"
		
	ans=A_and_B_Test(dataset_filepath)
	print("--"*12,"Answers","--"*12)
	print("Did more users use search feature in B design : %s\n"%ans.q1_answer())
	print("Did users search more often in B design : %s"%ans.q2_answer())
