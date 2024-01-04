from . import db
from .models import Article
from .newsApi import get_india_news
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv('.env')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def contextAI(content, a_id, app):
    try:
        try:
            aiContent = chat.send_message(
                f'Rewrite the following article in under 50000 characters and just the article '
                f'and nothing else no bolds as well. \n\n {content}').text
            aiDescription = chat.send_message(
                f'Give a description for the following article in under 750 characters and just '
                f'the description and nothing else no bolds as well. \n\n {content}').text
            aiTitle = chat.send_message(
                f'Give a Title for the following article in under 500 characters and just the title '
                f'and nothing else no bolds as well. \n\n {content}').text

            new_article = Article(a_id=a_id, title=aiTitle, og_content=aiContent, ai_content=aiContent,
                                  description=aiDescription)

            with app.app_context():
                db.session.add(new_article)
                db.session.commit()

        except google.generativeai.types.generation_types.BlockedPromptException:
            pass
    except NameError:
        pass


def get_news(app):
    counter = 1
    for j in range(30):
        news = get_india_news()

        for i in news:
            contextAI(i[0], i[1], app)
            print(f'saved in db: {counter}')
            counter += 1


def main_get_news(n, app):
    i = 0
    while i < n:
        i += 1
        get_news(app)
        time.sleep(900)


def load_news(count):
    art_list = []

    # with app.app_context():
    articles = Article.query.all()

    for article in articles:
        art_list.append([article.a_id, article.title[2:-2], article.description])

    len_l = len(art_list) - count

    if len_l - 10 < 0:
        art_lnew = art_list[0:len_l]
    else:
        art_lnew = art_list[len_l - 10:len_l]

    return art_lnew


def load_article(a_id):
    article = Article.query.filter_by(a_id=a_id).first()
    return [article.title[2:-2], article.ai_content]
