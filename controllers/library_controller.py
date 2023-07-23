from flask import render_template, Blueprint, request, redirect
from models.book_list import books, Book

events_blueprint=Blueprint("books",__name__)

@events_blueprint.route('/')
def index():
    return render_template('index.jinja',books=books)

@events_blueprint.route('/books/<index>')
def call_book(index):
    return render_template('book.jinja',books=books,index=int(index))

@events_blueprint.route('/form')
def form(duplicate=False):
    return render_template('form.jinja',books=books,duplicate=duplicate)

@events_blueprint.route('/books/<index>',methods=["POST"])
def add_book(index):
    duplicate_index=[i for i in range(len(books)) if request.form["title"]==books[i].title and request.form["author"]==books[i].author]
    if len(duplicate_index)==0: # if the entry isn't already in the library
        books.append(Book(request.form["title"],request.form["author"],request.form["genre"],bool(request.form["checked"])))
        return render_template('book.jinja',books=books,index=int(index))
    elif int(index)==len(books): # this will happen if a new form is submitted with a duplicate book
        return form(True)
    else:
        return call_book(index) # this will happen if the book page is reloaded just after it's been added

@events_blueprint.route('/books/<index>/delete',methods=["POST"])
def remove_book(index):
    del books[int(index)]
    return redirect('/')

@events_blueprint.route('/books/<index>/check_out',methods=["POST"])
def check_out(index):
    books[int(index)].check_out(True)
    return redirect(f"/books/{index}")

@events_blueprint.route('/books/<index>/check_in',methods=["POST"])
def check_in(index):
    books[int(index)].check_out(False)
    return redirect(f"/books/{index}")