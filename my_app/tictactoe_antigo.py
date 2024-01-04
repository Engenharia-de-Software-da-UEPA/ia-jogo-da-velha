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

        def horizontal():
            for line in [0, 1, 2]:
                horizontal_line = True
                if (line, 0) not in cordinates: horizontal_line = False
                if (line, 1) not in cordinates: horizontal_line = False
                if (line, 2) not in cordinates: horizontal_line = False

                if horizontal_line: return True
            return False
        
        def vertical():
            for col in [0, 1, 2]:
                vertical_line = True
                if (0, col) not in cordinates: vertical_line = False
                if (1, col) not in cordinates: vertical_line =  False
                if (2, col) not in cordinates: vertical_line =  False

                if vertical_line: return True 
            return False

        def diagonal():
            if (0, 0) not in cordinates: return False
            if (1, 1) not in cordinates: return False
            if (2, 2) not in cordinates: return False

            return True
        
        if any([horizontal(), vertical(), diagonal()]):
            win = p
            return win

    return win


def terminal(board):
    over = False

    if actions(board) == []: over = True
    elif winner(board) != None: over = True

    # if over: utility(board)
    
    return over


def utility(board):
    value = 0
    if winner(board) == X: value = 1
    elif winner(board) == O: value = -1

    return value


def minimax(board):
    '''
    # print('-----\n----\n----\n\nacho q vou ter q fazer o minimax msm\n----\n----\n----\n')
    if terminal(board): return None
    # who_plays_now = player(board)
    # print(board)
    # print(who_plays_now)

    first_board = copy.deepcopy(board)
    move_value = 'definir move_value'
    possible_actions = actions(board)
    initial_frontier = QueueFrontier()
    first_move = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]

    # print(possible_actions)

    # as it's the first move i decided to play with some technique
    if len(possible_actions) == 9: 
        move_value = first_move[random.randint(0, 4)]
        return move_value

    for action in possible_actions: initial_frontier.add(Node(action=action, parent=None)) # this frontier won't change

    # verifica se vence com alguma jogada q tem no frontier
    for node in initial_frontier.frontier:
        result_board = result(copy.deepcopy(first_board), node.action)[0]
        
        # if terminal(result_board) and winner(result_board) ==  who_plays_now: 
        #     move_value = node.action
        #     return move_value
        
        if terminal(result_board): 
            move_value = node.action
            return move_value


    nodes_and_values = []
    

    def max_value(node, received_board, new_boards_list, count):
        if count >= 3: return False
        # print(f'{node}, {received_board}, {new_boards_list}')
        new_board = result(copy.deepcopy(received_board), node.action)

        if terminal(new_board[0]):
            nodes_and_values.append([node, utility(new_board[0])])
            return False
        
        for action in actions(copy.deepcopy(new_board[0])):
            new_boards_list.append([node, result(copy.deepcopy(new_board[0]), action)[0]])

        count += 1

        while not len(new_boards_list) == 0:
            new_b = new_boards_list[0]
            new_boards_list = new_boards_list[1:]

            new_possible_actions = actions(new_b[1])

            for new_possible_a in new_possible_actions:
                max_value(Node(action=new_possible_a, parent=node), copy.deepcopy(new_b[1]), copy.deepcopy(new_boards_list), count)


    for node in initial_frontier.frontier:
        new_boards_list = []
        max_value(node, board, new_boards_list, count=0)

        
    results = {}

    for i in nodes_and_values:
        node = i[0]
        while not node.parent == None:
            node = node.parent
        
        value = i[1]

        if f"{node.action}" in results:
            results[f"{node.action}"]["value"] = results[f"{node.action}"]["value"] + value
        else:
            results[f"{node.action}"] = {
                'value': value,
            }

    first_value_key = list(results.keys())[0]
    first_value = (first_value_key, {'value': results[f'{first_value_key}']['value']})

    for v in results.items():
        # if who_plays_now == X:
        # < int(first_value[1]['value']): first_value = v
        if int(v[1]['value']) > int(first_value[1]['value']): first_value = v
        

    move_value = first_value[0]
        
    return move_value
    '''
    if terminal(board): return None

    first_board = copy.deepcopy(board)
    move_value = 'definir move_value'
    possible_actions = actions(board)
    initial_frontier = QueueFrontier()
    first_move = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]

    # print(possible_actions)

    # as it's the first move i decided to play with some technique
    if len(possible_actions) == 9: 
        move_value = first_move[random.randint(0, 4)]
        return move_value

    for action in possible_actions: initial_frontier.add(Node(action=action, parent=None)) # this frontier won't change

    # verifica se vence com alguma jogada q tem no frontier
    for node in initial_frontier.frontier:
        result_board = result(copy.deepcopy(first_board), node.action)[0]
        
        if terminal(result_board) and winner(result_board) ==  X: 
            move_value = node.action
            return move_value


    nodes_and_values = []
    

    def max_value(node, received_board, new_boards_list, count):
        if count >= 3: return False
        # print(f'{node}, {received_board}, {new_boards_list}')
        new_board = result(copy.deepcopy(received_board), node.action)

        if terminal(new_board[0]):
            nodes_and_values.append([node, utility(new_board[0])])
            return False
        for action in actions(copy.deepcopy(new_board[0])):
            new_boards_list.append([node, result(copy.deepcopy(new_board[0]), action)[0]])

        count += 1

        while not len(new_boards_list) == 0:
            new_b = new_boards_list[0]
            new_boards_list = new_boards_list[1:]

            new_possible_actions = actions(new_b[1])

            for new_possible_a in new_possible_actions:
                max_value(Node(action=new_possible_a, parent=node), copy.deepcopy(new_b[1]), copy.deepcopy(new_boards_list), count)


    for node in initial_frontier.frontier:
        new_boards_list = []
        max_value(node, board, new_boards_list, count=0)

        
    results = {}

    for i in nodes_and_values:
        node = i[0]
        while not node.parent == None:
            node = node.parent
        
        value = i[1]

        if f"{node.action}" in results:
            results[f"{node.action}"]["value"] = results[f"{node.action}"]["value"] + value
        else:
            results[f"{node.action}"] = {
                'value': value,
            }

    first_value_key = list(results.keys())[0]
    first_value = (first_value_key, {'value': results[f'{first_value_key}']['value']})

    for v in results.items():
        if int(v[1]['value']) > int(first_value[1]['value']): first_value = v

    move_value = first_value[0]

    print(move_value)
        
    return move_value



# board = [[X, O, X], [EMPTY, O, X], [EMPTY, X, O]]