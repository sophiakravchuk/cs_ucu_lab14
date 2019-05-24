from board import Board


def start():
    print("Hello! Let's play a game!")
    print("Wait a moment, please, I am preparing to play with you :)")


def get_symb():
    print("What symbol do you want to play with?")
    print("Enter 1 if you want to play with 'X' and to make your steps first \n"
          "or enter 2 if you want to play with 'O' and to be second")
    symb = input()
    try:
        symb = int(symb)
        if symb == 1:
            return True
        elif symb == 2:
            return False
        else:
            raise Exception
    except:
        print("Your number was invalid!")
        return get_symb()


def get_coords():
    try:
        n = input("Enter coordinates wher do you want to go (ex. 0, 1) \n"
                  "the first number is a row the second is a column: ")
        row, col = n.split(", ")
        row = int(row)
        col = int(col)
        return row, col
    except:
        print("Your coords were invalid!")
        return get_coords()


if __name__ == "__main__":
    start()
    b = Board(3)
    player_is_x = get_symb()

    curr_player_is_human = player_is_x
    while True:
        if curr_player_is_human:
            row, col = get_coords()
            b.make_step(row, col)
        else:
            step = b.get_best_step()
            best_step = b.get_best_step()
            b.make_step(best_step[0], best_step[1])
        print(b)
        if b.current_step.field.is_win(player_is_x):
            print(b)
            print("Congratulations! You win!")
            break
        elif b.current_step.field.is_win(not player_is_x):
            print(b)
            print("I am sorry! You lose!")
            break
        elif len(b.current_step.children) == 0:
            print(b)
            print("It is a draw!")
            break
        curr_player_is_human = not curr_player_is_human
