from flask import Blueprint, render_template, request, redirect
from models.book_list import books, Book

events_blueprint=Blueprint("books",__name__)

@events_blueprint.route('/') # homepage with book list
def index():
    return render_template('index.jinja',books=books)

@events_blueprint.route('/books/<int:index>') # book page with details & check in/out buttons for individual copies
def call_book(index):
    return render_template('book.jinja',book=books[index],index=index)

@events_blueprint.route('/form') # form for adding a new book
def form(duplicate=False): # duplicate is a boolean that controls a message that comes up when you try to log a book already in the system
    return render_template('form.jinja',books=books,duplicate=duplicate)

@events_blueprint.route('/books/<int:index>',methods=["POST"]) # function for adding new book that also takes you to that book's page
def add_book(index):
    duplicate_index=[True for book in books if request.form["title"]==book.title and request.form["author"]==book.author]
    if len(duplicate_index)==0: # if the entry isn't already in the library
        books.append(Book(request.form["title"],request.form["author"],request.form["genre"]))
        return render_template('book.jinja',book=books[index],index=index)
    elif index==len(books): # this will happen if a new form is submitted with a book already in the system
        return form(True)
    else: # this will happen if the book page is reloaded just after the book has been added
        return call_book(index)

@events_blueprint.route('/books/<int:index>/delete',methods=["POST"]) # function for deleting books from the system
def delete_book(index):
    del books[index]
    return redirect('/')

@events_blueprint.route('/books/<int:index>/<copy>',methods=["POST"]) # function for adding copies of a book or checking them in/out
def book_actions(index,copy):
    if copy=="add":
        books[index].add_copy()
    else:
        books[index].check_in_or_out(int(copy))
    return redirect(f"/books/{index}")

@events_blueprint.route('/books/<int:index>/<int:copy>/delete',methods=["POST"]) # function for adding copies of a book or checking them in/out
def delete_copy(index,copy):
    if len(books[index].checked_out)==1:
        return delete_book(index) # if only 1 copy left, delete book
    books[index].delete_copy(copy) # otherwise just delete copy
    return redirect(f"/books/{index}")