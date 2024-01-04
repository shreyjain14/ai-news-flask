from . import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.String(32), unique=True)
    title = db.Column(db.String(2000))
    og_content = db.Column(db.String(50000))
    ai_content = db.Column(db.String(50000))
    description = db.Column(db.String(5000))

