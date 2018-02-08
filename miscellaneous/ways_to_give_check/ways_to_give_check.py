#!/bin/python

import sys

def waysToGiveACheck(board):
    # Complete this function
    # print(board)
    success = 0
    # Find all possible pawn promotion tiles
    promo_list = [i for i, x in enumerate(list(board[1][0])) if x == "P"]
    bk_i, bk_j = find_b_king(board)
    # Check each position
    for p in promo_list:
        if board[0][0][p] != '#':
            print('skipped', p)
            continue # skip if pawn can't move to position on line 8
        # Check knight possibilities
        success += knight_check(p, bk_i, bk_j, board)
        success += rook_check(p, bk_i, bk_j, board)
        success += bishop_check(p, bk_i, bk_j, board)
        success += queen_check(p, bk_i, bk_j, board)
    return success

def find_b_king(board):
    for i, s in enumerate(board):
        for j, y in enumerate(s[0]):
            # print(y)
            if 'k' == y:
                return i, j# 2*(i+1)+(j+1)

def knight_check(p, k_i, k_j, board):
    count = 0
    # Check for valid move, king there
    if 
    return count

def rook_check(p, k_i, k_j, board):
    count = 0
    return count

def bishop_check(p, k_i, k_j, board):
    count = 0
    return count

def queen_check(p, k_i, k_j, board):
    count = 0
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

