from flask import render_template, request, redirect, url_for
from sqlalchemy import func
from .models import db, Game, HangmanWord

def get_random_word():
    word_record = HangmanWord.query.order_by(func.random()).first()
    return word_record.word if word_record else None

def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/new_game')
    def new_game():
        word = get_random_word()
        game = Game(word=word)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('play_game', game_id=game.id))

    @app.route('/play_game/<int:game_id>', methods=['GET', 'POST'])
    def play_game(game_id):
        game = Game.query.get_or_404(game_id)

        if request.method == 'POST':
            letter = request.form['letter']
            game.guessed_letters += letter
            if letter not in game.word:
                game.attempts += 1
            db.session.commit()

        min_attempts = min(game.attempts, 6)  # Adjust the maximum number of attempts as needed
        return render_template('play.html', game=game, min_attempts=min_attempts)
