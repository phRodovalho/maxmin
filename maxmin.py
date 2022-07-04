from board import Board


def new_game():
    board = Board()
    board.print_instructions()
    board.who_starts()

    print('Lets start!')
    board.print_board()

    if board.player_starts == 'X':
        while board.is_winner == False and board.count_full < 9:
            board.total_player_turn()
            if board.is_winner or board.count_full == 9:
                break
            board.total_computer_turn()

    elif board.player_starts == 'O':
        while board.is_winner == False and board.count_full < 9:
            board.total_computer_turn()
            if board.is_winner or board.count_full == 9:
                break
            board.total_player_turn()

    board.message_end()


new_game()
