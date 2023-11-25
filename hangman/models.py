# hangman/models.py

from . import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    guessed_letters = db.Column(db.String(26), default="")
    attempts = db.Column(db.Integer, default=0)

class HangmanWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
