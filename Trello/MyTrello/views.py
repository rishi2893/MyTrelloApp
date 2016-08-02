import datetime
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

from datetime import datetime
from django.http import HttpResponse
from django.template import loader

from .models import Board, Card, List
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

def remove_board(request, board_id):
    board = Board.objects.get(pk=board_id)
    board.delete()
    return HttpResponse(json.dumps([]))

def remove_card(request, card_id):
    card = Card.objects.get(pk=card_id)
    card.delete()
    return HttpResponse([])

def remove_list(request, list_id):
    list = List.objects.get(pk=list_id)
    list.delete()
    return HttpResponse(json.dumps([]))

def edit_board(request, board_id):
    if request.method == 'POST':
        print "hi"
        new_board_name = request.POST['board_name']
        board = Board.objects.get(pk=board_id)
        board.board_name = new_board_name
        board.save()
    return HttpResponse(json.dumps([]))

def edit_card(request, card_id):
    if request.method == 'POST':
        print "hi"
        new_card_name = request.POST['card_name']
        card = Card.objects.get(pk=board_id)
        card.card_name = new_card_name
        card.save()
    return HttpResponse(json.dumps([]))


def edit_list(request, list_id):
    if request.method == 'POST':
        new_list_name = request.POST['list_name']
        new_list_description = request.POST['list_description']
        new_due_date = request.POST['due_date']
        new_created_by = request.POST['created_by']
        list = List.objects.get(pk=list_id)
        list.list_name = new_list_name
        list.list_description = new_list_description
        list.due_date = new_due_date
        list.created_by = new_created_by
        list.save()
        
    return HttpResponse(json.dumps(data))

def index_data(request):
    info = []
    if request.method == 'POST':
        newBoard = request.POST['board_name']
        newBoard1 = request.POST['id']
        data = Board(board_name=newBoard, create_date=datetime.now())
        print datetime.now()
        data.save()

    all_boards = Board.objects.all()

    for some_board in all_boards:
        info.append({'id': some_board.id, 'board_name': some_board.board_name})

    return HttpResponse(json.dumps(info))

def board_data(request, board_id):
    info = []

    if request.method == 'POST':
        newCard = request.POST['card_name']
        Boardnum = get_object_or_404(Board, pk=board_id)
        data = Card(board=Boardnum, card_name=newCard)
        data.save()

    boardobj = Board.objects.get(pk=board_id)
    all_cards = Card.objects.filter(board = boardobj)
    for some_card in all_cards:
        info.append({'id': some_card.id, 'card_name': some_card.card_name})

    return HttpResponse(json.dumps(info))

def card_data(request, card_id):
    info = []
    if request.method == 'POST':
        newListname = request.POST['list_name']
        newListdescription = request.POST['list_description']
        newCreatedate = request.POST['create_date']
        newDuedate = request.POST['due_date']
        newCreatedby = request.POST['created_by']
        Cardnum = get_object_or_404(Card, pk=card_id)
        data = List(card=Cardnum, list_name=newListname, list_description=newListdescription,
                    create_date=newCreatedate, due_date=newDuedate, created_by=newCreatedby)
        data.save()

    cardobj = Card.objects.get(pk=card_id)
    all_lists = List.objects.filter(card = cardobj)
    for some_list in all_lists:
        info.append({'id': some_list.id, 'list_name':some_list.list_name,
                     'list_description': some_list.list_description, 'create_date': some_list.create_date,
                     'due_date': some_list.due_date,'created_by': some_list.created_by})

    return HttpResponse(json.dumps(info))



