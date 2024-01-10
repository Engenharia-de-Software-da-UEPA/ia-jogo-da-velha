"""
Tic Tac Toe Player
"""

import math
import copy
import random
from .util import Node, QueueFrontier

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = 0
    count_o = 0
    for i in board:
        count_x = count_x + i.count(X)
        count_o = count_o + i.count(O)
    
    return X if count_x <= count_o else O


def actions(board):
    possible_actions = []

    count_i, count_j = -1, -1

    for i in board:
        count_i, count_j = count_i + 1, -1
        for j in i:
            count_j += 1
            if j == EMPTY: possible_actions.append((count_i, count_j))

    return possible_actions


def result(board, action):
    if action[0] > 2 or action[1] > 2: raise Exception("invalid action")

    board_unmodified, new_board, actual_player = copy.deepcopy(board), board, player(board)
    
    new_board[action[0]][action[1]] = actual_player

    return new_board, board_unmodified


def horizontal(cordinates):
    for line in [0, 1, 2]:
        if (line, 0) in cordinates and (line, 1) in cordinates and (line, 2) in cordinates:
            return True
    return False

def vertical(cordinates):
    for col in [0, 1, 2]:
        vertical_line = True
        if (0, col) not in cordinates: vertical_line = False
        if (1, col) not in cordinates: vertical_line =  False
        if (2, col) not in cordinates: vertical_line =  False

        if vertical_line: return True 
    return False

def diagonal(cordinates):
    diagonal_line = False
    if (0, 0) in cordinates and (1, 1) in cordinates and (2, 2) in cordinates: diagonal_line = True
    elif (0, 2) in cordinates and (1, 1) in cordinates and (2, 0) in cordinates: diagonal_line = True

    return diagonal_line

def winner(board):
    possible_winners = [X, O]

    win = None

    for p in possible_winners:
        cordinates = []
        count_i, count_j = -1, -1

        for i in board:
            count_i, count_j = count_i + 1, -1
            for j in i:
                count_j += 1
                if p == j: cordinates.append((count_i, count_j))
        
        if any([horizontal(cordinates), vertical(cordinates), diagonal(cordinates)]):
            win = p
            return win

    return win


def terminal(board):
    over = False

    if actions(board) == []: over = True
    elif winner(board) != None: over = True
    
    return over


def utility(board):
    value = 0
    if winner(board) == X: value = 1
    elif winner(board) == O: value = -1

    return value












def maximizing(board, received_parent=None):
    return_v = -math.inf
    possible_actions = actions(board)
    frontier = QueueFrontier()
    actions_values = []
    move_value = "definir"

    for action in possible_actions:
        frontier.add(Node(action=action, parent=received_parent))

    for node in frontier.frontier:
        # print('eu sou o "', player(board), '" e vou jogar no', node.action)
        result_board = result(copy.deepcopy(board), node.action)[0]
        v = min_value(result_board, node)
        # print('resultado:', v)
        # print('\n')
        actions_values.append((node.action, v))

    # print('jogadas possiveis no maximizing', actions_values)
    for value in actions_values:
        # print('value[1] > return_v', value[1] > return_v, value[1], return_v)
        if value[1] > return_v: 
            return_v = value[1]
            move_value = value[0]

    if received_parent == None: return move_value
    
    return return_v


def minimizing(board, received_parent=None):
    return_v = math.inf
    possible_actions = actions(board)
    frontier = QueueFrontier()
    actions_values = []
    move_value = "definir"

    for action in possible_actions:
        frontier.add(Node(action=action, parent=received_parent))

    for node in frontier.frontier:
        # print('eu sou o "', player(board), '" e vou jogar no', node.action)
        result_board = result(copy.deepcopy(board), node.action)[0]
        v = max_value(result_board, node)
        # print('resultado:', v)
        # print('\n')
        actions_values.append((node.action, v))

    # print('jogdas possiveis no minimizing', actions_values)
    for value in actions_values:
        # print(return_v, value[1], value[0], value[1] < return_v, move_value)
        if value[1] < return_v:
            return_v = value[1]
            move_value = value[0]

    # print('melhor jogada do O', move_value)
    if received_parent == None: 
        return move_value
    
    return return_v




def max_value(board, received_parent):
    # print('recebi ->', board)
    if terminal(board):
        return utility(board)

    # print('ainda nao acabou e é a vez do', player(board), 'entao vou chamr o maximizing')
    board_copy = copy.deepcopy(board)
    v = maximizing(board_copy, received_parent=received_parent)
    
    return v

    



def min_value(board, received_parent):
    # print('recebi ->', board)
    if terminal(board):
        return utility(board)

    # print('ainda nao acabou e é a vez do', player(board), 'entao vou chamar o minimizing')

    board_copy = copy.deepcopy(board)
    v = minimizing(board_copy, received_parent=received_parent)

    return v

    

















def minimax(board):
    if terminal(board): return None

    first_board = copy.deepcopy(board)
    move_value = 'definir move_value'
    possible_actions = actions(board)

    if len(possible_actions) == 1: 
        move_value = possible_actions[0]
        return move_value
    
    initial_frontier = QueueFrontier()

    if len(possible_actions) == 9: 
        first_move = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
        move_value = first_move[random.randint(0, 4)]
        return move_value

    if len(possible_actions) == 8:
        if first_board == [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY,EMPTY]]: return (1, 1)
        elif first_board == [[EMPTY, EMPTY, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY,EMPTY]]: return (1, 1)
        elif first_board == [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [X, EMPTY,EMPTY]]: return (1, 1)
        elif first_board == [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY,X]]: return (1, 1)

    for action in possible_actions: initial_frontier.add(Node(action=action, parent=None))

    for node in initial_frontier.frontier:
        result_board = result(copy.deepcopy(first_board), node.action)[0]
        
        if terminal(result_board) and winner(result_board) ==  X: 
            move_value = node.action
            return move_value
    




    if player(first_board) == X:
        # cost = -math.inf
        # actions_cost = []

        max = maximizing(copy.deepcopy(first_board))
        # print('final => ', max)
        move_value = max

        # for node in initial_frontier.frontier:
        #     result_board = result(copy.deepcopy(first_board), node.action)[0]
        #     print('action:', node.action, ', board:', result_board)
        #     max = maximizing(result_board)
        #     print("\n\n=-=-=-=-=-=-=-\nValor final:", max, "\n=-=-=-=-=-=-=-\n\n")

        #     actions_cost.append([node.action, max])
        
        # for action_cost in actions_cost:
        #     if action_cost[1] > cost:
        #         cost = action_cost[1]
        #         move_value = action_cost[0]
        
    elif player(first_board) == O:
        # cost = math.inf
        # actions_cost = []

        min = minimizing(copy.deepcopy(board))
        # print('final => ', min)
        move_value = min

        # for node in initial_frontier.frontier:
        #     result_board = result(copy.deepcopy(first_board), node.action)[0]
        #     print('action:', node.action, ', board:', result_board)
        #     min = minimizing(copy.deepcopy(first_board))
        #     print("\n\n=-=-=-=-=-=-=-\nValor final:", min, "\n=-=-=-=-=-=-=-\n\n")

        #     actions_cost.append([node.action, min])
        
        # for action_cost in actions_cost:
        #     if action_cost[1] < cost: 
        #         cost = action_cost[1]
        #         move_value = action_cost[0]
        

    
    return move_value

