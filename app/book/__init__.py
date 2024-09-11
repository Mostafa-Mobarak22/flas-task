from flask import Blueprint

book_blueprint = Blueprint('book',__name__,url_prefix='/book')

from app.book import views