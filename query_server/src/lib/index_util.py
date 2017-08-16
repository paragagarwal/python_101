class PrefixIndex(object):
	def __init__(self):
		self.root=None
		self.initialize_root()

	def initialize_root(self):
		self.root=[{}, {}]

	def insert_data(self,  data, rank):
		search_str=self.search_extract(data)
		for str in search_str:
			self.insert(data, rank, str)

	def insert(self, data, rank, search_str):
		r=self.root
		for i in range(len(search_str)):
			if search_str[i] not in r[0]:
				r[0][search_str[i]]=[{}, {}]
				if  i+1 == len(search_str):
					r[0][search_str[i]][1][data]=rank
				r=r[0][search_str[i]]
			else:
				if i+1 == len(search_str):
					r[0][search_str[i]][1][data]=rank
				else:
					r=r[0][search_str[i]]

	def traverse_cal(self, root, sort_data):
		if root is None:
			return None
		if len(root[1]) > 0:
			for k, v in root[1].iteritems():
				sort_data.gen_result([k, v])
		for v in root[0].values():
			self.traverse_cal(v, sort_data)

	def find_match(self, root=None, prefix="", num=10):
		if root is None:
			root=self.root
		sort_data=MinData(num)
		target_root=None
		for i in range(len(prefix)):
			if prefix[i] in root[0]:
				if len(prefix)-1 == i:
					target_root=root[0][prefix[i]]
				else:
					root=root[0][prefix[i]]
			else:
				return sort_data.data
		self.traverse_cal(target_root, sort_data)
		return sort_data.data

	def search_extract(self, word):
		return [w for w in word.split("_")] 

class MinData(object):
	def __init__(self, num=10):
		self.data={}
		self.num=num

	def gen_result(self, result):
		if len(self.data) < self.num:
			self.data[result[0]]= result[1]
		else:
			min_d=self.find_min()
			if min_d[1] < result[1]:
				self.data.pop(min_d[0])
				self.data[result[0]]= result[1]

	def find_min(self):
		min_d=None
		for k, v in self.data.iteritems():
			if min_d is None:
				min_d=[k, v]
			else:
				if min_d[1] > v:
					min_d=[k, v]
		return min_d
