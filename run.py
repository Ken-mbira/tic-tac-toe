# Write a tic tac toe game in python
from time import sleep
from tokenize import Number

class Player:
    name = ""
    symbol = ""
    move = 0

    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        move = input(f"""Player {self.name}, make your move : """)
        if(isinstance(int(move),int) and 0 <=  int(move) < 9):
            return move
        else:
            print("That was not a valid move")
            self.make_move()
                


def main():
    while True:
        counter = 0
        moves = []
        winner = None

        board = [
            ["","",""],
            ["","",""],
            ["","",""]
        ]

        print("Welcome To Tic Tac Toe")

        player1 = Player(name="",symbol="")
        player2 = Player(name="",symbol="")

        player1.name = input("Player 1, please enter your name : ")
        player1.symbol = input("Player 1, please enter your symbol : ")
        player2.name = input("Player 2, please enter your name : ")
        player2.symbol = input("Player 2, please enter your symbol : ")

        if player1.name == player2.name or player1.symbol == player2.symbol:
            print("Please enter different names and symbols")
            break

        while counter < 9:
            player_one_move = player1.make_move()
            player_two_move = player2.make_move()

            break

if __name__ == "__main__":
    main()