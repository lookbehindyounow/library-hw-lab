from models.book import Book, titles_blurbs

books=[Book(f"book {i+1}","same guy","nerd book") for i in range(10)]
# books=[Book(book[0],book[1],"there's no such thing",book[2]) for book in titles_blurbs] # too many books homepage takes forever to load