import time

from btree import BTree


class Board:
    def __init__(self, n):
        self.width = n
        self.tree = BTree(n)
        self.tree.build()
        self.current_step = self.tree._root
        self.first_is_x = True

    def make_step(self, row, col):
        if self.current_step.field.board[row][col] is not None:
            raise Exception("Wrong move")
        for step in self.current_step.children:
            if step.step_row == row and step.step_col == col:
                self.current_step = step
                break

    def get_best_step(self):
        best_step = None
        for step in self.current_step.children:
            if best_step is None or best_step.rating < step.rating:
                best_step = step
        return best_step.step_row, best_step.step_col

    def __str__(self):
        s = ""
        for row in range(self.width):
            for col in range(self.width):
                is_first = self.current_step.field.board[row][col]
                if is_first is None:
                    s += "  | "
                elif self.first_is_x == is_first:
                    s += "X | "
                else:
                    s += "O | "
            s = s[:-3] + "\n"
            s += ("-" * self.width * 3) + "\n"
        return s[:-((self.width * 3)+1)]


if __name__ == "__main__":
    start = time.time()
    b = Board(3)
    print(time.time() - start)
    for i in range(9):
        step = b.get_best_step()
        best_step = b.get_best_step()
        b.make_step(best_step[0], best_step[1])
        print(best_step)
        print(b)
        if b.current_step.field.is_win(True) or b.current_step.field.is_win(False):
            break
