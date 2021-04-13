#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB
#from controller.player import PlayerController


class PlayerModel:

    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking


serialized_players = {
    #'last_name':
    #'first_name': player.first_name,
    #'birth_date': player.birth_date,
    #'gender': player.gender,
    #'ranking': player.ranking
}

db = TinyDB('player.json')
