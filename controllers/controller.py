from flask import render_template
from app import app
from models.player import Player
from models.rps_game import determine_result, player_1,player_2, determine_2player_game_result

# @app.route('/<choice_1>/<choice_2>')
# def play_game(choice_1,choice_2):
#     return determine_result(choice_1,choice_2)

@app.route('/rps_game')
def index():
    return render_template('index.html', title='Home', player_1=player_1, player_2=player_2, result = determine_2player_game_result(player_1,player_2))



