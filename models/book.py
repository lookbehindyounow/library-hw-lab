class Book():

    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
        self.checked_out=[False]
    
    def add_copy(self):
        self.checked_out.append(False)
    
    def delete_copy(self,copy):
        del self.checked_out[copy]
    
    def check_in_or_out(self,copy):
        self.checked_out[copy]=not self.checked_out[copy]