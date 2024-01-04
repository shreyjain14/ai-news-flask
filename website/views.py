from flask import Blueprint, render_template, request, flash, jsonify
from .models import Article
from . import db
import json
from .getAI import load_article

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/article/<a_id>')
def article(a_id):
    n_article = load_article(a_id)
    return render_template("article.html", article=n_article)
