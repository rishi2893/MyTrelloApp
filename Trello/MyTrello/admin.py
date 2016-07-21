# Register your models here.
from django.contrib import admin

from .models import Board, Card, List

admin.site.register(Board)
admin.site.register(Card)
admin.site.register(List)