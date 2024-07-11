from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null = True)
    message = models.TextField()
    