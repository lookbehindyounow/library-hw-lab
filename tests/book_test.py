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