from flask import render_template
from app import app
from models.player import Player
from models.rps_game import player_1,player_2, determine_result



@app.route('/rps_game')
def determine_result(player_1,player_2):
    return result