#booklover_test.py

import unittest
from booklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        self.assertTrue("The Great Gatsby" in book_lover.book_list["book_name"].tolist())

    def test_2_add_book(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        book_lover.add_book("The Great Gatsby", 5)
        self.assertEqual(book_lover.book_list["book_name"].tolist().count("The Great Gatsby"), 1)
                
    def test_3_has_read(self): 
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("1984", 4)
        self.assertTrue(book_lover.has_read("1984"))
        
    def test_4_has_read(self): 
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        self.assertFalse(book_lover.has_read("Brave New World"))
        
    def test_5_num_books_read(self): 
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("Moby Dick", 3)
        book_lover.add_book("Pride and Prejudice", 4)
        book_lover.add_book("To Kill a Mockingbird", 5)
        self.assertEqual(book_lover.num_books_read(), 3)

    def test_6_fav_books(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("Moby Dick", 3)
        book_lover.add_book("Pride and Prejudice", 4)
        book_lover.add_book("To Kill a Mockingbird", 5)
        fav_books = book_lover.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books["book_rating"].tolist()))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
