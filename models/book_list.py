from models.book import Book

books=[Book(f"book {i}","same guy","nerd book",bool(i%2)) for i in range(10)]