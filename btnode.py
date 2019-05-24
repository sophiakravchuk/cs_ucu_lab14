import copy


class Field:
    def __init__(self, n):
        self.width = n
        self.board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(None)
            self.board.append(row)
        self.last_comb = ()

    def is_win(self, el):
        for row_ind in range(self.width):
            am_hor = 0
            am_vert = 0
            for col_ind in range(self.width):
                if self.board[row_ind][col_ind] == el:
                    am_hor += 1
                if self.board[col_ind][row_ind] == el:
                    am_vert += 1
            if am_vert == self.width or am_hor == self.width:
                return True

        am_diag1 = 0
        am_diag2 = 0
        for i in range(self.width):
            if self.board[i][i] == el:
                am_diag1 += 1
            if self.board[i][self.width - 1 - i] == el:
                am_diag2 += 1

        return am_diag1 == self.width or am_diag2 == self.width


class BTNode(object):
    """Represents a node for a linked binary tree."""

    def __init__(self, field, step_row = None, step_col = None):
        self.field = field
        self.children = []
        self.first_player = None
        self.rating = 0
        self.step_row = step_row
        self.step_col = step_col

    def build_children(self, first_player):
        self.children = []
        self.first_player = first_player
        if self.field.is_win(first_player):
            return
        for row_ind in range(self.field.width):
            for col_ind in range(self.field.width):
                if self.field.board[row_ind][col_ind] is None:
                    new_field = Field(self.field.width)
                    # new_field.board = copy.deepcopy(self.field.board)
                    new_field.board = []
                    for row in self.field.board:
                        new_field.board.append(row.copy())
                    new_field.board[row_ind][col_ind] = first_player

                    new_btnode = BTNode(new_field, row_ind, col_ind)
                    self.children.append(new_btnode)
                    new_btnode.build_children(not first_player)

    def calc_rating(self, cur_player):
        self.rating = 0
        if self.field.is_win(not cur_player):
            self.rating = 1
            return self.rating
        if len(self.children) == 0:
            return 0
        all_rating = 0
        for child in self.children:
            all_rating += -child.calc_rating(not cur_player)
        self.rating = all_rating / len(self.children)
        return self.rating










