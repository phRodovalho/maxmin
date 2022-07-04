from computerLogicCode import best_move


class Board:

    # create board

    def __init__(self):

        self.board = {1: ' ', 2: ' ', 3: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}
        self.is_winner = False
        self.count_full = 0
        self.player_won = ' '
        self.player_starts = ' '

    # win checks

    def win_row(self):
        row_start_point = [1, 4, 7]
        for start in row_start_point:
            if self.board[start] != ' ' and self.board[start] == self.board[start+1] == self.board[start+2]:
                self.is_winner = True
                self.player_won = self.board[start]
                break

    def win_column(self):
        row_start_point = [1, 2, 3]
        for start in row_start_point:
            if self.board[start] != ' ' and self.board[start] == self.board[start+3] == self.board[start+6]:
                self.is_winner = True
                self.player_won = self.board[start]
                break

    def win_diagonal(self):
        if self.board[5] != ' ' and (self.board[1] == self.board[5] == self.board[9] or self.board[3] == self.board[5] == self.board[7]):
            self.is_winner = True
            self.player_won = self.board[5]

    def check_win(self):
        self.win_row()
        if self.is_winner == False:
            self.win_column()
            if self.is_winner == False:
                self.win_diagonal()

    # prints & instructions

    def print_board(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])

    def print_instructions(self):
        print("HELLO! welcome to TIC-TAC-TOE")
        print("This is our board cells number markings:")
        print()
        print('1|2|3')
        print('-+-+-')
        print('4|5|6')
        print('-+-+-')
        print('7|8|9')
        print()
        print("When asked please play your turn and enter avaliable cell number for X.")

    def who_starts(self):
        while self.player_starts != 'X' and self.player_starts != 'O':
            print("You're X I'm O. Who goes first ? please enter X or O.")
            self.player_starts = input().upper()

    def message_end(self):
        print("GAME OVER!")
        if self.is_winner:
            print(self.player_won, "WON!")
        else:
            print("TIE!")

    def avaliable_cells(self):
        avaliables = []
        for i in range(1, 10):
            if self.board[i] == ' ':
                avaliables.append(i)
        return avaliables

    # player_turn

    def player_turn(self):
        turn = 0
        avaliables = self.avaliable_cells()
        while turn not in avaliables:
            print("Your turn! Please enter avaliable cell number for X.")
            turn = input()
            turn = ord(turn) - 48
        self.board[turn] = 'X'

    def total_player_turn(self):
        self.player_turn()
        self.count_full = self.count_full + 1
        self.print_board()
        self.check_win()

     # computer_turn

    def computer_turn(self):
        turn = best_move(self)
        self.board[turn] = 'O'
        # print ("computer still learning :(")

    def total_computer_turn(self):
        self.computer_turn()
        self.count_full = self.count_full + 1
        print("Computer turn :)")
        self.print_board()
        self.check_win()
