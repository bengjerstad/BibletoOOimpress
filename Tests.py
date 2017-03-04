from fromdb import booklookup
import unittest

class TestStringMethods(unittest.TestCase):
	def test_booklookup_pass(self):
		self.assertEqual(booklookup('Genesis'),'Genesis')
	def test_booklookup_abr(self):
		self.assertEqual(booklookup('gen'),'Genesis')
	def test_booklookup_abr_cap(self):
		self.assertEqual(booklookup('Gen'),'Genesis')
	def test_booklookup_abr_cap_punc(self):
		self.assertEqual(booklookup('Gen.'),'Genesis')

		
if __name__ == '__main__':
	unittest.main()