class Board:

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        print("Hello Welcome to TIC TAC TOE game \n")

    def show_cells(self):
        print("--------------------------------")
        print("%s|%s|%s" % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----")
        print("%s|%s|%s" % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----")
        print("%s|%s|%s" % (self.cells[7], self.cells[8], self.cells[9]))


# class Player(Board):
#
#     def __init__(self):
#         if self.cells[player] == 'X':
#             print("player ")
#         elif self.cells[player] == 'O':

    def update_cell_no(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
    #
    # def turn_player(self):
    #     if self.cells[cell_no] ==

    def win_game(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        else:
            return False


board = Board()

while True:

    board.show_cells()

    player = int(input("\n Select cells from 1-9 to input X or O "))
    board.update_cell_no(player, "X")
    # board.turn_player()
    board.show_cells()
    if board.win_game("X"):
        print("X wins ")

    player = int(input("\n Select cells from 1-9 to input X or O "))
    board.update_cell_no(player, "O")
    board.show_cells()
    if board.win_game("O"):
        print("O wins ")
