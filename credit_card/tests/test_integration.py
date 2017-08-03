import unittest
import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("tests", "src/lib"))
import reader
 
class TestIntegration(unittest.TestCase):
 
   	def gen_duplicate_input(self):
		lines=[]
		lines.append('Add duplicate 4111111111111111 $1000')
		lines.append('Charge duplicate $200')
		lines.append('Add duplicate 4111111111111111 $0')
		lines.append('Charge duplicate $100')
		return lines

   	def gen_case_sensitive_input(self):
		lines=[]
		lines.append('Add CASE 4111111111111111 $1000')
		lines.append('Add case 5454545454545454 $1000')
		lines.append('Charge CASE $100')
		lines.append('charge case $100')
		return lines

  	def gen_test_alpha_input(self):
		lines=[]
		lines.append('Add aaa 4111111111111111 $1000')
		lines.append('Add aa 5454545454545454 $3000')
		lines.append('Add a 4280769499845116 $2000')
		lines.append('Charge aaa $100')
		lines.append('Charge aa $100')
		lines.append('Charge aa $100')
		lines.append('Credit aaa $100')
		lines.append('Credit aa $100')
		lines.append('Credit aa $100')
		return lines

 	def gen_test_input(self):
		lines=[]
		lines.append('Add Tom 4111111111111111 $1000')
		lines.append('Add Lisa 5454545454545454 $3000')
		lines.append('Add Quincy 1234567890123456 $2000')
		lines.append('Charge Tom $500')
		lines.append('Charge Tom $800')
		lines.append('Charge Lisa $7')
		lines.append('Credit Lisa $100')
		lines.append('Credit Quincy $200')
		return lines

	def test_error(self):
		lines=[]
		lines.append('Add test_error 1010101 $2000')
		lines.append('Credit test_error $200')
		expected=['test_error: error']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_border(self):
		lines=[]
		lines.append('Add test_border 5454545454545454 $200')
		lines.append('Charge test_border $200')
		expected=['test_border: $200']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_decline(self):
		lines=[]
		lines.append('Add test_decline 5454545454545454 $0')
		lines.append('Charge test_decline $200')
		expected=['test_decline: $0']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_credit(self):
		lines=[]
		lines.append('Add test_credit 5454545454545454 $2000')
		lines.append('Charge test_credit $100')
		expected=['test_credit: $100']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_full_name_charge(self):
		lines=[]
		lines.append('Add John Aflex Wordworth 5454545454545454 $2000')
		lines.append('Charge John Aflex Wordworth $100')
		expected=['John Aflex Wordworth: $100']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_full_name_decline(self):
		lines=[]
		lines.append('Add John Aflex Wordworth 5454545454545454 $0')
		lines.append('Charge John Aflex Wordworth $100')
		expected=['John Aflex Wordworth: $0']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_full_name_credit(self):
		lines=[]
		lines.append('Add John Aflex Wordworth 5454545454545454 $10000')
		lines.append('Credit John Aflex Wordworth $100')
		expected=['John Aflex Wordworth: $-100']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_charge(self):
		lines=[]
		lines.append('Add test_charge 5454545454545454 $2000')
		lines.append('Credit test_charge $100')
		expected=['test_charge: $-100']
		actual=reader.consume_lines_and_display_result(lines)
		self.assertEqual(actual, expected)

	def test_case_sensitive_input(self):
		actual=reader.consume_lines_and_display_result(self.gen_case_sensitive_input())
		expected=['CASE: $100', 'case: $100']
		self.assertEqual(actual, expected)

	def test_duplicate_input(self):
		actual=reader.consume_lines_and_display_result(self.gen_duplicate_input())
		expected=['duplicate: $0']
		self.assertEqual(actual, expected)

	def test_sort_input(self):
		actual=reader.consume_lines_and_display_result(self.gen_test_alpha_input())
		expected=['a: $0', 'aa: $0', 'aaa: $0']
		self.assertEqual(actual, expected)

	def test_line_input(self):
		actual=reader.consume_lines_and_display_result(self.gen_test_input())
		expected=['Lisa: $-93', 'Quincy: error', 'Tom: $500']
		self.assertEqual(actual, expected)

 	def test_empty_file_input(self):
 		try:
	 		lines = self.gen_test_input()
	 		os.system("mkdir test_1")
	 		f = open('test_1/empty_file.txt', 'w')
			f.close()
			actual=reader.consume_file_and_display_result('test_1/empty_file.txt')
			expected=[]
			self.assertEqual(actual, expected)
		finally:
			os.system("rm -rf test_1")

 	def test_file_input(self):
 		try:
	 		lines = self.gen_test_input()
	 		os.system("mkdir test_1")
	 		f = open('test_1/test_file.txt', 'w')
	 		for line in lines:
				f.write(line+"\n")
			f.close()
			actual=reader.consume_file_and_display_result('test_1/test_file.txt')
			expected=['Lisa: $-93', 'Quincy: error', 'Tom: $500']
			self.assertEqual(actual, expected)
		finally:
			os.system("rm -rf test_1")

if __name__ == '__main__':
    unittest.main()