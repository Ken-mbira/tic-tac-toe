def check_win_col(board):
    for i in board:
        if( i[0] == i[1] == i[2] and i[0] != ""):
            return i[0]
        else:
            continue

    return False

def check_win_row(board):
    row_one = []
    row_two = []
    row_three = []

    for col in board:
        row_one.append(col[0])
        row_two.append(col[1])
        row_three.append(col[2])

    for i in [row_one,row_two,row_three]:
        if(i[0] == i[1] == i[2] and i[0] != ""):
            return i[0]

    return False

def check_win_diagonal(board):
    right_to_left = []
    left_to_right = []

    right_left_increment = 0
    left_right_increment = 2

    for col in board:
        right_to_left.append(col[right_left_increment])
        right_left_increment += 1

    for col in board:
        left_to_right.append(col[left_right_increment])
        left_right_increment -= 1

    for i in [right_to_left,left_to_right]:
        if(i[0] == i[1] == i[2] and i[0] != ""):
            return i[0]    

    return False


class Player:
    name = ""
    symbol = ""

    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self,board):
        move = input(f"""Player {self.name}, make your move : """)
        try:
            if(board[int(move[0])][int(move[1])] == ""):
                board[int(move[0])][int(move[1])] = self.symbol
                return board
            else:
                print("That move has already been made!")
                return self.make_move(board)
        except:
            print("That was not a valid move")
            return self.make_move(board)

    def run_checks(self,board):
        if(check_win_col(board)):
            return True

        if(check_win_row(board)):
            return True

        if(check_win_diagonal(board)):
            return True

        return False