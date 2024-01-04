from flask import Blueprint, render_template, request, flash, jsonify, make_response
from .newsApi import get_india_news
from .models import Article
from . import db
import json
from .getAI import load_news

getArticles = Blueprint('getArticles', __name__)


@getArticles.route('/load')
def load():
    if request.args:

        counter = int(request.args.get('c'))

        if counter == 100:
            return make_response(jsonify({}), 200)

        else:
            news = load_news(counter)
            if news:
                return make_response(jsonify(news), 200)
            else:
                return make_response(jsonify({}), 200)
