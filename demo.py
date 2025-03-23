from booklover.booklover import BookLover

testreader=BookLover("Test Reader","johndoe@acme.com","SciFI")

print(testreader.book_list)

testreader.add_book("1984",5)
testreader.add_book("Ender's Game",2)
print(testreader.book_list)
print(testreader.fav_books())
print(testreader.num_books_read())

print(testreader.name)
print(testreader.email)
print(testreader.fav_genre)