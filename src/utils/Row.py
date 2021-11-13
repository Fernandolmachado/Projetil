from src.objects.Player import Player


class Row(object):
    def __init__(self):
        self.row = list()

    def get_player(self) -> Player:
        for i in range(len(self.row)):
            player = self.row[0]
            self.row.remove(player)
            if not player.is_dead():
                break
        return player

    def get_players(self) -> list:
        return self.row

    def set_player(self, player: Player):
        self.row.append(player)

    def length(self):
        return len(self.row)

    def clean(self):
        for i in range(len(self.row)):
            player = self.row[i]
            if player.is_dead():
                self.row.remove(player)
                break
