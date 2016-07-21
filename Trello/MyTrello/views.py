from django.http.response import Http404

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Board, Card


# Create your views here.

def index(request):
    latest_board_list = Board.objects.order_by('-create_date')[:5]
    template = loader.get_template('MyTrello/index.html')
    context = {
        'latest_board_list': latest_board_list,
    }
    return HttpResponse(template.render(context, request))

def board_detail(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        raise Http404("Board does not exist")
    return render(request, 'MyTrello/board_detail.html', {'board': board})

def card_detail(request, board_id, card_id):
    try:
        card = Card.objects.get(pk=card_id)
        board = card.board.id
        if board != int(board_id):
            raise Http404("Illegal access")
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    return render(request, 'MyTrello/card_detail.html', {'card': card})
