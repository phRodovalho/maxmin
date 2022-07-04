import random


def do_move(board, move, player):
    board.board[move] = player
    board.count_full = board.count_full + 1


def undo_move(board, move):
    board.board[move] = ' '
    board.count_full = board.count_full - 1
    board.is_winner = False
    board.player_won = ' '


def best_move(board):

    # computer is first, corner is best.
    if board.count_full == 0:
        return random.choice([1, 3, 7, 9])

    # fill last cell.
    if board.count_full == 8:
        for i in range(1, 10):
            if board.board[i] == ' ':
                return i

    # computer is second, player 'X' in a corner, so 'O' in the middle.
    if board.count_full == 1:
        for i in [1, 3, 7, 9]:
            if board.board[i] != ' ':
                return 5

    # maxmin method
    avaliables = board.avaliable_cells()

    best = -1000
    best_turn = 0

    for move in avaliables:
        do_move(board, move, 'O')

        # value move
        check = maxmin(board, 0, False)
        if check > best:
            best = check
            best_turn = move

        undo_move(board, move)

    return best_turn


def evaluate(board):
    board.check_win()
    if board.is_winner:
        return 10 if board.player_won == 'O' else -10
    if board.count_full == 9:  # and no winner, tie
        return 0
    return ' '


def maxmin(board, depth, isMax):

    score = evaluate(board)
    if score != ' ':
        return score

    avaliables = board.avaliable_cells()

    # If this maximizer's move
    if isMax:
        best = -1000
        for move in avaliables:
            do_move(board, move, 'O')
            check = maxmin(board, depth+1, not isMax)
            best = check if check > best else best
            undo_move(board, move)
        return best-depth

    # If this minimizer's move
    else:
        best = 1000
        for move in avaliables:
            do_move(board, move, 'X')
            check = maxmin(board, depth+1, not isMax)
            best = check if check < best else best
            undo_move(board, move)
        return best+depth
