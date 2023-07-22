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

@events_blueprint.route('/',methods=["POST"]) # change route to book page
def add_book():
    book=Book(request.form["title"],request.form["author"],request.form["genre"],request.form["checked"])
    if request.form["title"] not in [book.title for book in books] and request.form["author"] not in [book.author for book in books]:
        books.append(book)
    return render_template('index.jinja',title="Library",books=books) # change route

@events_blueprint.route('/books/<index>/delete',methods=["POST"])
def remove_event(index):
    print(index,len(books),[book.title for book in books])
    del books[int(index)]
    return redirect('/')