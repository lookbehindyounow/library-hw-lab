from models.book import Book, titles_blurbs

books=[Book(f"book {i+1}","same guy","nerd book") for i in range(10)]

secret_books_list=[Book(book[0],book[1],"there's no such thing",book[2]) for book in titles_blurbs]
# ^^ too many books - homepage tries to load all of them in html, never happens