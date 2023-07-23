import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book=Book("1984","Jorjor Well","Year")
    
    def test_has_attributes(self):
        self.assertEqual(self.book.title,"1984")
        self.assertEqual(self.book.author,"Jorjor Well")
        self.assertEqual(self.book.genre,"Year")
        self.assertFalse(self.book.checked_out[0])
    
    def test_add_copy(self):
        self.book.add_copy()
        self.assertEqual(len(self.book.checked_out),2)
    
    def test_check_in_or_out(self):
        self.assertFalse(self.book.checked_out[0])
        self.book.check_in_or_out(0)
        self.assertTrue(self.book.checked_out[0])