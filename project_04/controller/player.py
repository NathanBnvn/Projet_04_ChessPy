from model.player import PlayerModel
from view.view import View


class PlayerController:

    def __int__(self, view, model):
        self.view = View()
        self.model = PlayerModel

    def create(self):
        add = self.view.createtournament()
        player = PlayerModel(last_name=add.last_name, first_name=add.first_name, birth_date=add.birth_date,
                             gender=add.gender, ranking=add.ranking,)
        return player


controller = PlayerController()
controller.create()
