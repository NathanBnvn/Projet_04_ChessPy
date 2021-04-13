#! /usr/bin/env python3
# coding: utf-8

from tinydb import TinyDB, Query

class TournamentModel():

	def __init__(self, name, place, date, turns, tours, players, timeControl, description):
		self.name = name
		self.place = place
		self.date = date
		self.turns = turns
		self.tours = tours
		self.players = players
		self.timeControl = timeControl
		self.description = description

# ts

serialized_tournament = {
	'name': 
	'place':
	'date':
	'turns':
	'tours':
	'players':
	'timeControl':
	'description':

}

db = TinyDB("tournamentdb.json")
db.insert({'name': ,'place': , 'date': , 'turns': , 'tours': , 'players': , 'timeControl': , 'description': })