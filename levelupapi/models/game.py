from levelupapi.models.gametype import GameType
from levelupapi.models.gamer import Gamer
from django.db import models

class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)