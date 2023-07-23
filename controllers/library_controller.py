from flask import render_template, Blueprint, request, redirect
from models.book_list import books, Book

events_blueprint=Blueprint("books",__name__)

@events_blueprint.route('/')
def index():
    return render_template('index.jinja',title='Library',books=books)

@events_blueprint.route('/books/<index>')
def call_book(index):
    return render_template('book.jinja',title=books[int(index)].title,book=books[int(index)])

@events_blueprint.route('/form')
def form():
    return render_template('form.jinja',title='Add Book',books=books)

@events_blueprint.route('/books/<index>',methods=["POST"]) # change route to book page
def add_book(index):
    book=Book(request.form["title"],request.form["author"],request.form["genre"],bool(request.form["checked"]))
    if request.form["title"] not in [book.title for book in books] or request.form["author"] not in [book.author for book in books]:
        books.append(book)
    print([books[i].checked_out for i in range(len(books)) if i==len(books)-1])
    return render_template('book.jinja',title=books[int(index)].title,book=books[int(index)])

@events_blueprint.route('/books/<index>/delete',methods=["POST"])
def remove_book(index):
    print(index,len(books),[book.title for book in books])
    del books[int(index)]
    return redirect('/')