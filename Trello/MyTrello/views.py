import datetime
from django.http.response import Http404

from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponse
from django.template import loader

from .models import Board, Card, BoardForm
import json
# Create your views here.

def index(request):
    latest_board_list = Board.objects.all()
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

def data(request):
    info = []
    if request.method == 'POST':
        newBoard = request.POST['board_name']
        newBoard1 = request.POST['id']
        print newBoard1
        board_data = Board(board_name=newBoard, create_date=datetime.now())
        board_data.save()


    all_boards = Board.objects.all()

    for some_board in all_boards:
        info.append({'id': some_board.id, 'board_name': some_board.board_name})

    return HttpResponse(json.dumps(info))

