#! /usr/bin/env python3
# coding: utf-8

import inquirer
from model.tournament import *
from model.player import PlayerModel


def create():
	name = input("Entrez le nom du tournois : ")
	place = input("Entrez le lieu où se déroule le tournois : ")
	date = input("Entrez la date : ")
	TURNS = 4
	tours = "#"
	players = PlayerModel
	timeControl = [
		inquirer.List("timeControl", message="contrôle du temps", choices=["bullet", "blitz", "coup rapide"],),
		]
	answers = inquirer.prompt(timeControl)
	timeControl = answers["timeControl"]
	description = input("Les remarques du directeur : ")

	tournament = TournamentModel(name=name, place=place, date=date, turns=TURNS, tours=tours, players=players, timeControl=timeControl, description=description,)
	return tournament


class TournamentController:

	def __init__(self):
		self.model = TournamentModel()
		self.playerModel = PlayerModel()

	create()
