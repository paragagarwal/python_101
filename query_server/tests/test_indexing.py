import unittest
import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("tests", "src/lib"))
from index_util import PrefixIndex
 
class TestIndexing(unittest.TestCase):
 
	def gen_run(self, input, expected_result, query):
		index=PrefixIndex()
		for d in input:
			index.insert_data(d[0], d[1])
		result = index.find_match(index.root, query).keys()
		self.assertTrue(sorted(expected_result)==sorted(result))

	def test_no_result_1(self):
		expected_result=[]
		index=PrefixIndex()
		sample_data=[["a{0}".format(x), x] for x in range(100)]
		self.gen_run(sample_data, expected_result, "no_result")

	def test_no_result_2(self):
		expected_result=[]
		index=PrefixIndex()
		sample_data=[["a{0}".format(x), x] for x in range(100)]
		self.gen_run(sample_data, expected_result, "A")

	def test_case_sensitive(self):
		expected_result=['a99', 'a98', 'a95', 'a94', 'a97', 'a96', 'a91', 'a90', 'a93', 'a92']
		index=PrefixIndex()
		sample_data=[["a{0}".format(x), x] for x in range(100)]+[["A{0}".format(x), x] for x in range(100)]
		self.gen_run(sample_data, expected_result, "a")

	def test_order_result_1(self):
		expected_result=['a99', 'a98', 'a95', 'a94', 'a97', 'a96', 'a91', 'a90', 'a93', 'a92']
		index=PrefixIndex()
		sample_data=[["a{0}".format(x), x] for x in range(100)]
		self.gen_run(sample_data, expected_result, "a")

	def test_order_result_2(self):
		expected_result=['a128', 'a129', 'a120', 'a121', 'a122', 'a123', 'a124', 'a125', 'a126', 'a127']
		index=PrefixIndex()
		sample_data=[["a{0}".format(x), x] for x in range(1000)]
		self.gen_run(sample_data, expected_result, "a12")

	def test_duplicate(self):
		index=PrefixIndex()
		sample_data=[["is_it", x] for x in range(1000)]
		self.gen_run(sample_data, ['is_it'], "is")
		self.gen_run(sample_data, ['is_it'], "it")
		self.gen_run(sample_data, [], "is_it")

	def test_underscore(self):
		index=PrefixIndex()
		sample_data=[["is_it__me", 1], ["is_it", 1], ["is", 2],  ["it", 3],  ["me", 4]]
		self.gen_run(sample_data, ["is_it__me", "is", "is_it"], "is")
		self.gen_run(sample_data, ["is_it__me", "me"], "me")
		self.gen_run(sample_data, ["is_it__me", "it", "is_it"], "it")

	def test_long_match(self):
		expected_result=["{0}".format('a'*(x+1)) for x in range(90,100)]
		index=PrefixIndex()
		sample_data=[["{0}".format('a'*(x+1)), x+1] for x in range(100)]
		self.gen_run(sample_data, expected_result, "a")

if __name__ == '__main__':
    unittest.main()