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
    
    def test_delete_copy(self):
        self.book.add_copy()
        self.book.checked_out[1]=True # set 2nd copy to checked out
        self.book.delete_copy(1) # delete 2nd copy
        self.assertEqual(len(self.book.checked_out),1) # check deleted
        self.assertFalse(self.book.checked_out[0]) # check remaining copy is checked in
        self.book.add_copy()
        self.book.checked_out[0]=True # set original copy to checked out
        self.book.delete_copy(0) # delete original copy
        self.assertFalse(self.book.checked_out[0]) # check remaining copy is checked in
        # The purpose of the second half of this test is to ensure delete_copy removes the specified copy & not just any copy
    
    def test_check_in_or_out(self):
        self.assertFalse(self.book.checked_out[0])
        self.book.check_in_or_out(0)
        self.assertTrue(self.book.checked_out[0])