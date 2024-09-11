import os
from crypt import methods
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for
from app.book import book_blueprint
from app.models import db ,Book
from app.book.forms import BoookForm
@book_blueprint.route('create',endpoint='create',methods=['GET','POST'])
def create_form():
    form = BoookForm()
    if request.method=='POST':
        if form.validate_on_submit():
            image_name = None
            if request.files.get('image'):
                image = form.image.data
                image_name = secure_filename(image.filename)
                image.save(os.path.join('static/book/images/', image_name))
            newbook = Book(name=request.form["name"], description=request.form["description"], image=image_name
                           , number=request.form['number'])
            db.session.add(newbook)
            db.session.commit()
            return redirect(newbook.show_url)
    return render_template('book/createbook.html',form=form)

@book_blueprint.route('',endpoint='list')
def list():
    books = Book.query.all()
    return render_template('book/listbook.html',books=books)

@book_blueprint.route('<int:id>',endpoint='show')
def show(id):
    books = db.get_or_404(Book,id)
    return render_template('book/showbook.html',books=books)

@book_blueprint.route('<int:id>/delete',endpoint='delete')
def delete(id):
    oldbook = db.get_or_404(Book,id)
    db.session.delete(oldbook)
    db.session.commit()
    return redirect(url_for("book.list"))

@book_blueprint.route('<int:id>/update',endpoint='update',methods=['GET','POST'])
def update_form(id):
    form = BoookForm()
    oldbook = db.get_or_404(Book,id)
    form.name.data = oldbook.name
    form.number.data = oldbook.number
    form.description.data = oldbook.description
    if request.method=='POST':
        if form.validate_on_submit():
            image_name = None
            if request.files.get('image'):
                image = form.image.data
                image_name = secure_filename(image.filename)
                image.save(os.path.join('static/book/images/', image_name))
            oldbook.name = request.form["name"]
            oldbook.image = image_name
            oldbook.number = request.form['number']
            oldbook.description = request.form["description"]
            db.session.add(oldbook)
            db.session.commit()
            return redirect(oldbook.show_url)
    return render_template('book/updatebook.html',form=form)