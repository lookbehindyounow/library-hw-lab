import csv

# Below is a database with the blurbs for about 58,000 books,
# someone scraped it together & posted it on a website called kaggle.
blurbs=csv.reader(open("models/books_with_blurbs.csv","r"))
titles_blurbs=[[row[1],row[2],row[5]] for row in blurbs]

class Book():
    def __init__(self,title,author,genre,blurb=None):
        self.title=title
        self.author=author
        self.genre=genre
        self.checked_out=[False]
        # this condition is to save this loop running 58k * 58k times if you're using the experimental (non-working) book list
        if blurb is None:
            self.blurb=[book[2] for book in titles_blurbs if title.lower()==book[0].lower() and author.lower()==book[1].lower()]
            # if the book added is in the blurbs database, add the blurb to the book
    
    def add_copy(self):
        self.checked_out.append(False)
    
    def delete_copy(self,copy):
        del self.checked_out[copy]
    
    def check_in_or_out(self,copy):
        self.checked_out[copy]=not self.checked_out[copy]