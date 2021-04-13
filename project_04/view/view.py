#!/usr/bin/env python
# coding: utf-8

import inquirer


class View:

    def createplayer(self):
        last_name = str(input("Nom du joueur/joueuse : "))
        first_name = str(input("Prénom du joueur/joueuse : "))
        birth_date = str(input("La date de naissance du joueur/joueuse : "))
        gender_list = [
            inquirer.List("gender", message="sexe du joueur/joueuse", choices=["masculin", "féminin"], ),
        ]
        answers = inquirer.prompt(gender_list)
        gender = answers["gender"]
        ranking = int(input("Son classement : "))

        return last_name, first_name, birth_date, gender, ranking

    def createtournament(self):
        name = str(input("Nom du tournois : "))
        place = str(input("Lieu du tournois : "))
        date = str(input("La date du tournois : "))
        turn = 4
        control_list = [
            inquirer.List("control", message="contrôle du temps", choices=["bullet", "blitz", "coup rapide"],),
        ]
        answers = inquirer.prompt(control_list)
        time_check = answers["control"]
        description = str(input("Remarques générales : "))

        return name, place, date, turn, time_check, description
