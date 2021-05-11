from levelupapi.models.game import Game
from django.db import models



class Event(models.Model):  

    game = models.ForeignKey("Game" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="attending")
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    time = models.TimeField()
    description = models.CharField(max_length=50)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
