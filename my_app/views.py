from django.shortcuts import render
from django.http import JsonResponse
import json
from . import tictactoe as ttt

# Create your views here.
def index(request):
    return render(request, "my_app/index.html")


def action_move(request):
    board = json.loads(request.body)['board']
    for row in board:
        for i in range(3):
            if row[i] == "EMPTY": row[i] = None

    move = str(ttt.minimax(board))
    print(move)
    if move in f"None {None}": return JsonResponse({'resultado': 'acabou'})

    row, col = move.replace('(', '').replace(')', '').split(', ')

    return JsonResponse({'row': row, 'col': col})