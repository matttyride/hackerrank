#!/bin/python

import sys

def waysToGiveACheck(board):
    # Complete this function
    # print(board)
    success = 0
    # Find all possible pawn promotion tiles
    promo_list = [i for i, x in enumerate(list(board[1][0])) if x == "P"]
    # print('promotions', promo_list)
    bk_i, bk_j = find_b_king(board)
    # print('bk', bk_i, bk_j)
    # Check each position
    for p in promo_list:
        if board[0][0][p] != '#':
            # print('skipped', p)
            continue # skip if pawn can't move to position on line 8
        # Check knight possibilities
        success += knight_check(0, p, bk_i, bk_j, board)
        success += rook_check(0, p, bk_i, bk_j, board)
        success += bishop_check(0, p, bk_i, bk_j, board)
        success += queen_check(0, p, bk_i, bk_j, board)
        # Search for discovered checks
        for i in range(len(boards)): # rows
            for j in range(len(boards[0])): # cols
                if boards[i][0][j] == 'n':
                    success += knight_check(j, i, bk_i, bk_j, board)
    return success

def find_b_king(board):
    for i, s in enumerate(board):
        for j, y in enumerate(s[0]):
            if 'k' == y:
                return i, j

def knight_check(p_i, p_j, k_i, k_j, board):
    count = 0
    # TODO: change to search for all discovered checks
    # Check for valid move, king there
    if p_j >= 2 and p_i and board[p_i+1][0][p_j-2] == 'k': # 2 left, 1 down
        count += 1
    elif p_j >= 1 and board[2][0][p_j-1] == 'k': # 1 left, 2 down
        count += 1
    elif p_j <= 5 and board[1][0][p_j+2] == 'k': # 2 right, 1 down
        count += 1
    elif p_j <= 6 and board[2][0][p_j+1] == 'k': # 1 right, 2 down
        count += 1
    return count

def rook_check(p, k_i, k_j, board):
    count = 0
    if k_i == 0:
        if p - k_i == 1 or p - k_i == -1: # no space between king and pawn
            count += 1
        else:
            min_ = min([p, k_i])
            max_ = max([p, k_i])
            if board[0][0][min_:max_] == "#"*(max_-min_):
                count += 1
    elif k_j == p:
        if k_i - 0 == 1: # no space between king and pawn
            count += 1
        else:
            blocked = False
            for i in range(2, k_i): # check all spaces between
                if board[i][0][p] != '#':
                    blocked = True
                    break
            if not blocked:
                count += 1
    return count

def bishop_check(p, k_i, k_j, board):
    count = 0
    #print('a', k_i-0)
    #print('b', abs(k_j-p))
    if k_i == 0:
        return count
    elif k_i - 0 == abs(k_j - p): # is diagonal
        if k_j - p > 0: # going right
            blocked = False
            for i in range(1, k_j-p):
                if board[i][0][i] != '#':
                    blocked = True
                    break
            if not blocked:
                count += 1
        elif k_j - p < 0:
            blocked = False
            for i in range(1, abs(k_j-p)):
                if board[i][0][0-i] != '#':
                    blocked = True
                    break
            if not blocked:
                count += 1
    return count

def queen_check(p, k_i, k_j, board):
    count = 0
    count += rook_check(p, k_i, k_j, board)
    count += bishop_check(p, k_i, k_j, board)
    return count

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        board = []
        for board_i in xrange(8):
            board_temp = map(str,raw_input().strip().split(' '))
            board.append(board_temp)
        result = waysToGiveACheck(board)
        print result

