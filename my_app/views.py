from django.shortcuts import render
from django.http import JsonResponse, Http404
import json
from . import tictactoe as ttt

# Create your views here.
def index(request):
    return render(request, "my_app/index.html")


def action_move(request):
    if request.method != "POST": raise Http404
    board = json.loads(request.body)['board']
    for row in board:
        for i in range(3):
            if row[i] == "EMPTY": row[i] = None

    move = str(ttt.minimax(board))
    
    if move in f"None {None}": return JsonResponse({'resultado': 'acabou'})

    row, col = move.replace('(', '').replace(')', '').split(', ')

    return JsonResponse({'row': row, 'col': col})


def terminal_view(request):
    if request.method != "POST": raise Http404
    board = json.loads(request.body)['board']
    for row in board:
        for i in range(3):
            if row[i] == "EMPTY": row[i] = None

    return JsonResponse({"terminal": ttt.terminal(board)})