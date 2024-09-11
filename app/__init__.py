from flask_wtf import FlaskForm, CSRFProtect
from app.config import config_option,config
from flask import Flask
from app.models import db
from flask_migrate import Migrate
from app.book import book_blueprint
from flask_bootstrap import Bootstrap5
def create_app(config_name='prod'):
    app = Flask(__name__)
    current_config = config_option[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"] = current_config.SQLALCHEMY_DATABASE_URI
    bootstrap = Bootstrap5(app)
    app.secret_key = config.secret_key
    db.init_app(app)
    migrate = Migrate(app,db)
    app.register_blueprint(book_blueprint)
    return app