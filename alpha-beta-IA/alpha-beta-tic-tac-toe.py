import time
fat_dna_pos = 1000
fat_dna_neg = -1000
typegame = ""


class Player:
    players = []

    def __init__(self, name='', letter=''):
        self.name = name
        self.letter = letter
        Player.players.append(self)


def create_board():  # Dict of board
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    return board


def print_board(board):
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3] + ' ')
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6] + ' ')
    print('───┼───┼───')
    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9] + ' ')
    print('')


def space_is_empty(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def find_computer_obj():
    for player in Player.players:
        if player.name == 'computer':
            return player


def find_computer2_obj():
    for player in Player.players:
        if player.name == 'computer2':
            return player


def find_human_obj():
    for player in Player.players:
        if player.name == 'human':
            return player


def delay():
    time.sleep(0.5)


def insert_letter(board, letter, position):
    delay()
    if space_is_empty(board, position):
        board[position] = letter
        print('')
        print_board(board)

        if check_tie(board):
            print('Empate!')
            exit()
        elif victory(board):  # add computer2
            if letter == find_computer_obj().letter:
                print('O computador ganhou!')
            elif letter == find_human_obj().letter and typegame == "player":
                print('Você ganhou!')
            elif letter == find_computer2_obj().letter and typegame == "computer2":
                print('O computador2 ganhou!')
        return

    else:
        print('A posição escolhida está ocupada!')
        delay()
        position = int(input('Escolha uma nova posição: '))
        insert_letter(board, letter, position)
        return


def check_rows_win(board, letter=None):
    if letter is None:
        if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
            return True
        else:
            return False


def check_columns_win(board, letter=None):
    if letter is None:
        if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[4] and board[1] == board[7] and board[1] == letter:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
            return True
        else:
            return False


def check_diagonal_win(board, letter=None):
    if letter is None:
        if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[5] and board[1] == board[9] and board[1] == letter:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == letter:
            return True
        else:
            return False


def victory(board):
    if check_rows_win(board):
        return True
    elif check_columns_win(board):
        return True
    elif check_diagonal_win(board):
        return True
    else:
        return False


def player_won(board, player):
    if check_rows_win(board, player):
        return True
    elif check_columns_win(board, player):
        return True
    elif check_diagonal_win(board, player):
        return True
    else:
        return False


def check_tie(board):  # check empate
    for key in board.keys():
        if board[key] == ' ':
            return False

    if victory(board):
        return False
    else:
        return True


def human_movement(board, human):
    position = int(
        input('Digite a posição para sua jogada "' + human.letter + '": '))
    insert_letter(board, human.letter, position)
    return

# add computer2_movement


def computer2_movement(board, computer):
    best_score = fat_dna_pos  # computer2 is max 800
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer.letter
            score = minimax(board, 3, True)  # alter to true
            board[key] = ' '
            if score < best_score:
                best_score = score
                best_move = key
    print('Jogada do computador2:', best_move)
    insert_letter(board, computer.letter, best_move)
    return


def computer_movement(board, computer):
    best_score = fat_dna_neg
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer.letter
            score = minimax(board, 3, False)  # alter to true
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    print('Jogada do computador:', best_move)
    insert_letter(board, computer.letter, best_move)
    return

# is_maximizing true

# alter to suported diferents ways to game: pc vs pc2; pc vs human


def minimax(board, depth, is_maximizing):
    computer = find_computer_obj()
    human = find_human_obj()
    computer2 = find_computer2_obj()
    if player_won(board, computer.letter):
        return 1
    elif check_tie(board):
        return 0

    # verifica se human ou computer2 ta jogando
    if human != None:
        if player_won(board, human.letter):
            return -1
    elif player_won(board, computer2.letter):
        return -1

    if is_maximizing:
        best_score = fat_dna_neg
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer.letter
                # Next move should minimize
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = fat_dna_pos
        for key in board.keys():
            if board[key] == ' ':
                if human != None:
                    board[key] = human.letter
                else:
                    board[key] = computer2.letter
                # Next move should maximize
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def define_first_player():
    """
    if human goes first -> return True
    if computer goes first -> return False
    """
    delay()
    option = int(
        input('1 - Player joga primeiro;\n2 - Computador joga primeiro;\n Digite uma opção: '))
    if option == 1:
        print('Você é o primeiro a jogar! Boa Sorte!')
        return True
    elif option == 2:
        print('O Computador joga primeiro! Boa Sorte!')
        return False
    else:
        print('Digite uma opção válida!')
        define_first_player()


def define_type_of_game():
    """
    if human vs computer -> return True
    if computer vs computer2 -> return False
    """
    delay()
    option = int(
        input(' 1 - Player vs Computer;\n 2 - Computer vs Computer2;\nDigite uma opção para começar: '))
    if option == 1:
        print('\nPlayer VS Computer\n')
        return True
    elif option == 2:
        print('\nComputer VS Computer2\n')
        return False
    else:
        print('Digite uma opção válida!')
        define_type_of_game()


def create_players(config):
    """
    if config = 1 -> human goes first X
    if config = 0 -> computer goes first X
    if config = -1 -> computer = X VS computer2 = 0
    """
    if config == 1:
        human = Player('human', 'X')
        computer = Player('computer', '0')
        return human, computer
    elif config == 0:
        human = Player('human', '0')
        computer = Player('computer', 'X')
        return human, computer
    elif config == -1:
        computer = Player('computer', 'X')
        computer2 = Player('computer2', '0')
        return computer, computer2


def human_vs_computer(board):
    human_goes_first = define_first_player()
    print('')

    if human_goes_first:
        human, computer = create_players(1)
        print_board(board)
        while not victory(board):
            delay()
            human_movement(board, human)
            delay()
            computer_movement(board, computer)

    else:
        human, computer = create_players(0)
        while not victory(board):
            delay()
            computer_movement(board, computer)
            delay()
            human_movement(board, human)


def computer_vs_computer(board):
    computer, computer2 = create_players(-1)
    print_board(board)
    while not victory(board):
        delay()
        computer_movement(board, computer)
        delay()
        computer2_movement(board, computer2)


def main():
    print('_________________________________________________')
    print('|                 Jogo da Velha                  |')
    print('|________________________________________________|')
    print('Para jogar digite o número referente a posição')
    print('que você deseja jogar, seguindo o mapa abaixo:')
    print('')
    delay()
    print(' 1 │ 2 │ 3 ')
    print('───┼───┼───')
    print(' 4 │ 5 │ 6 ')
    print('───┼───┼───')
    print(' 7 │ 8 │ 9 ')
    print('')

    board = create_board()
    type_game = define_type_of_game()

    if type_game:
        human_vs_computer(board)
        typegame = "player"
    else:
        print("Computer = X VS Computer2 = 0\n")
        computer_vs_computer(board)
        typegame = "computer2"


if __name__ == '__main__':
    main()
