from django.db import models

# Create your models here.

class Places(models.Model):
    name: models.CharField(max_length=255, unique=True)
    picture: models.CharField()


class Food(models.Model):
    name: models.CharField(max_length=255, unique=True)
    picture: models.CharField()