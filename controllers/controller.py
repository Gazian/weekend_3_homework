# from flask import render_template
from app import app
from models.player import Player
from models.rps_game import determine_result

@app.route('/<choice_1>/<choice_2>')
def play_game(choice_1,choice_2):
    return determine_result(choice_1,choice_2)

