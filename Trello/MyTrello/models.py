from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.forms import ModelForm


class Board(models.Model):
    board_name = models.CharField(max_length=150)
    create_date = models.DateTimeField('Date Published:')
    def __str__(self):
        return self.board_name

class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=150)
    def __str__(self):
        return self.card_name

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = '__all__'


class List(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=500)
    def __str__(self):
        return self.list_name



