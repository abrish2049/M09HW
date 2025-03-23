import pandas as pd

class BookLover:
    '''
    A class used to represent a BookLover.

    The BookLover class is used to store and return favorite books of users
    along with their own names, email, and ratings for those books.

    Attributes:
    -----------
    name : str
        The name of the BookLover.
    email : str
        The email address of the BookLover.
    fav_genre : str
        The favorite genre of the BookLover.
    num_books : int, optional
        The number of books the BookLover has added to their book list. Defaults to 0.
    book_list : pd.DataFrame
        A DataFrame storing the list of books with their ratings.
    '''
    
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name: str = name
        self.email: str = email
        self.fav_genre: str = fav_genre
        self.num_books: int = num_books
        self.book_list: pd.DataFrame = book_list
    
    def add_book(self, book_name: str, rating: int):
        '''
        Adds a book to the BookLover's book list with the specified rating.
        Returns a string message if the book is already in the list or the rating is invalid.
        '''
        if not (0 <= rating <= 5):
            return "Error: Rating must be an integer between 0 and 5."
        
        if book_name in self.book_list['book_name'].tolist():
            return f"{book_name} is already in the book list."
                   
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1
    
    def has_read(self, book_name: str):
        '''
        Checks if the BookLover has read a particular book by checking the book name in their list.
        Returns True if the book is in the list, otherwise False.
        '''
        if book_name in self.book_list['book_name'].tolist():
            return True
        return False
    
    def num_books_read(self):
        '''
         Returns the number of books the BookLover has read (added to their list).
        '''
        if self.num_books:
            return self.num_books
        return 0
    
    def fav_books(self):
        '''
        Returns a DataFrame of the BookLover's favorite books (those with a rating greater than 3).
        '''
        fav_books_list = self.book_list[self.book_list['book_rating'] > 3]
        if not fav_books_list.empty:
            return fav_books_list
        return pd.DataFrame({'book_name': [], 'book_rating': []})

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Dune", 5)
    print(test_object.book_list)
