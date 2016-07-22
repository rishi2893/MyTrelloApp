# Register your models here.
from django.contrib import admin

from .models import Board, Card, List

class ListInline(admin.StackedInline):
    model = List
    extra = 2

class CardInline(admin.StackedInline):
    model = Card
    extra = 2

class CardAdmin(admin.ModelAdmin):
    inlines = [ListInline]

class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['board_name']}),
        ('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
    ]
    inlines = [CardInline]

admin.site.register(Board, BoardAdmin)
admin.site.register(Card, CardAdmin)