import unittest
import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("tests", "src/lib"))
import reader
import json

class TestLuhn10(unittest.TestCase):

	def test_valid_luhn10_0(self):
		self.check_valid('00000000000')

	def test_valid_luhn10_1(self):
		self.check_valid('4111111111111111')

	def test_valid_luhn10_2(self):
		self.check_valid('5454545454545454')

	def test_valid_luhn10_3(self):
		self.check_valid('4171512051500147')

	def test_valid_luhn10_4(self):
		self.check_valid('4280769499845116')

	def test_valid_american_express(self):
		for card in self.get_card_numbers_from_file('tests/credit_cards/american_express.json'):
			self.check_valid(card)

	def test_valid_visa(self):
		for card in self.get_card_numbers_from_file('tests/credit_cards/visa.json'):
			self.check_valid(card)

	def test_valid_master_card(self):
		for card in self.get_card_numbers_from_file('tests/credit_cards/master_card.json'):
			self.check_valid(card)

	def test_in_valid_luhn10_1(self):
		self.check_invalid('474439393')

	def test_in_valid_luhn10_2(self):
		self.check_invalid('10200')

	def test_in_valid_luhn10_3(self):
		self.check_invalid('1234567890123456')

	def test_in_valid_luhn10_4(self):
		self.check_invalid('4040920220')

	def check_valid(self, num):
		c, v = reader.is_luhn10(num)
		self.assertTrue(c, "{0} should be valid luhn".format(v))

	def check_invalid(self, num):
		c, v = reader.is_luhn10(num)
		self.assertFalse(c, "{0} should be in valid luhn".format(num))

	def get_card_numbers_from_file(self, path):
		json_data=open(path).read()
		data = json.loads(json_data)
		return [ str(v['CreditCard']['CardNumber']) for v in data]

if __name__ == '__main__':
    unittest.main()