from flask_sqlalchemy import SQLAlchemy
from flask import url_for
db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    image = db.Column(db.String(250))
    number = db.Column(db.Integer)

    @property
    def img_url(self):
        return url_for('static',filename=f'book/images/{self.image}')

    @property
    def show_url(self):
        return url_for('book.show',id=self.id)

    @property
    def delete_url(self):
        return url_for('book.delete',id=self.id)

    @property
    def update_url(self):
        return url_for('book.update',id=self.id)

    def __str__(self):
        return f"{self.name}"
