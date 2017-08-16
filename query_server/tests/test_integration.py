import unittest
import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("tests", "src/lib"))
from client import Client
PORT=8080
class TestIndexing(unittest.TestCase):
 
	def test_smoke(self):
		self.insert_data()
		expected_data=['a1', 'a0', 'a2']
		data= self.query_and_verify()
		print data
		self.assertTrue(sorted(data)==sorted(expected_data))

	def insert_data(self):
		data=[{"name":"a0", "rank":1}, {"name":"a1", "rank":1}, {"name":"a2", "rank":2}]
		d_client=Client(PORT)
		d_client.send_data(data)
		
	def query_and_verify(self):
		d_client=Client(PORT)
		return d_client.query("a")

if __name__ == '__main__':
    unittest.main()