import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

from forms import BookForm
from models import books

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BookForm()
    error = ""
    if request.method == 'POST':
        books.create(form.data)
        books.save_all()
        return redirect(url_for("books_list"))
    return render_template("books.html", form=form, books=books.all(), error=error)


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)
