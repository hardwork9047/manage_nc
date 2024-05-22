# models.py

from django.db import models

class Room(models.Model):
    room_no = models.IntegerField()

    def __str__(self):
        return str(self.room_no)
