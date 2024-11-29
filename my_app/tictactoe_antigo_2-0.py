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
        a = True
        if (line, 0) not in cordinates: a = False
        if (line, 1) not in cordinates: a = False
        if (line, 2) not in cordinates: a = False
        
        if a: return True


def vertical(cordinates):
    for col in [0, 1, 2]:
        vertical_line = True
        if (0, col) not in cordinates: vertical_line = False
        if (1, col) not in cordinates: vertical_line =  False
        if (2, col) not in cordinates: vertical_line =  False

        if vertical_line: return True 


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








def maximizing(board, received_parent):
    values_list = []
    frontier = QueueFrontier()

    for action in actions(copy.deepcopy(board)):
        frontier.add(Node(action=action, parent=received_parent))
    
    for node in frontier.frontier:
        values_list.append([node, min_value(copy.deepcopy(board), node)])
    
    return values_list


def minimizing(board, received_parent):
    values_list = []
    frontier = QueueFrontier()

    for action in actions(copy.deepcopy(board)):
        frontier.add(Node(action=action, parent=received_parent))

    for node in frontier.frontier:
        values_list.append([node, max_value(copy.deepcopy(board), node)])

    return values_list


def max_value(received_board, received_node):
    v = -math.inf
    board = result(copy.deepcopy(received_board), received_node.action)[0]
    if terminal(copy.deepcopy(board)):
        return utility(board)

    for action in actions(copy.deepcopy(board)):
        new_board = result(copy.deepcopy(board), action)[0]
        if terminal(copy.deepcopy(new_board)):
            return utility(new_board)
        max = maximizing(new_board, received_node)
        for a in max:
            if a[1] > v: v = a[1]
    return v


def min_value(received_board, received_node):
    v = math.inf
    board = result(copy.deepcopy(received_board), received_node.action)[0]
    if terminal(copy.deepcopy(board)):
        return utility(board)

    for action in actions(copy.deepcopy(board)):
        new_board = result(copy.deepcopy(board), action)[0]
        if terminal(copy.deepcopy(new_board)): 
            return utility(new_board)
        min=minimizing(new_board, received_node)
        for a in min:
            if a[1] < v: v = a[1]
    return v
        
        
        
    # return v
    # if not terminal(board):
    #     action_value = 0
    #     for i in my_list:
    #         print(i)
    #         for a in i:
    #             print(a)
    #         print('\n')
    #         # action_value = action_value + i[1]
    #     return action_value


'''

[[[<util.Node object at 0x0000015DC9925850>, 1]], [[<util.Node object at 0x0000015DC9925AD0>, 0]]]
[['X', 'O', 'X'], ['X', 'X', 'O'], ['O', None, None]]

[[<util.Node object at 0x0000015DC9925850>, 1]]
[<util.Node object at 0x0000015DC9925850>, 1]

[[<util.Node object at 0x0000015DC9925AD0>, 0]]
[<util.Node object at 0x0000015DC9925AD0>, 0]


'''




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

    for action in possible_actions: initial_frontier.add(Node(action=action, parent=None))

    for node in initial_frontier.frontier:
        result_board = result(copy.deepcopy(first_board), node.action)[0]
        
        if terminal(result_board) and winner(result_board) ==  X: 
            move_value = node.action
            return move_value
    
    if player(first_board) == X:
        cost = -math.inf
        actions_cost = []

        for node in initial_frontier.frontier:
            max = maximizing(result(copy.deepcopy(first_board), node.action)[0], received_parent=node)
            action_value = 0
            action_node = 0
            for i in max:
                action_value = action_value + i[1]
                action_node = i[0]
                while not action_node.parent == None:
                    action_node = action_node.parent
            actions_cost.append([action_node.action, action_value])
        for possiblity in actions_cost:
            if cost < possiblity[1]: 
                cost = possiblity[1]
                move_value = possiblity[0]
            
    elif player(first_board) == O:
        cost = math.inf
        actions_cost = []

        for node in initial_frontier.frontier:
            min = minimizing(result(copy.deepcopy(first_board), node.action)[0], received_parent=node)
            action_value = 0
            action_node = 0
            for i in min:
                action_value = action_value + i[1]
                action_node = i[0]
                while not action_node.parent == None:
                    action_node = action_node.parent
            actions_cost.append([action_node.action, action_value])
        for possiblity in actions_cost:
            if cost > possiblity[1]: 
                cost = possiblity[1]
                move_value = possiblity[0]
    return move_value

