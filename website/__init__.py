from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv
from dotenv import load_dotenv

load_dotenv('/.env')

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .getArticles import getArticles

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(getArticles, url_prefix='/')

    from .models import Article
    
    with app.app_context():
        db.create_all()

    from .getAI import get_news, load_news

    # get_news(100, app)

    # load_news(app, 0)

    return app
