import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book=Book("1984","Jorjor Well","Year",False)
    
    def test_has_attributes(self):
        self.assertEqual(self.book.title,"1984")
        self.assertEqual(self.book.author,"Jorjor Well")
        self.assertEqual(self.book.genre,"Year")
        self.assertEqual(self.book.checked_out,False)
    
    def test_check_out(self):
        self.book.check_out(True)
        self.assertTrue(self.book.checked_out)
        self.book.check_out(False)
        self.assertFalse(self.book.checked_out)