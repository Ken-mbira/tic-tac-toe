# Write a tic tac toe game in python
import pyfiglet
import termcolor
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.layout import Layout

from player import Player

def run_intro():
    welcome_banner = pyfiglet.figlet_format("Welcome To TicTacToe",justify="center")
    print(termcolor.colored(welcome_banner,'red','on_grey'))

def main():
    while True:
        counter = 0
        winner = None

        board = [
            ["","",""],
            ["","",""],
            ["","",""]
        ]

        run_intro()


        player1 = Player(name=input("Player 1, enter your name : "),symbol=input("Player 1, enter your symbol : "))
        player2 = Player(name=input("Player 2, enter your name : "),symbol=input("Player 2, enter your symbol : "))

        if player1.symbol == player2.symbol:
            print("Please enter different names and symbols")
            break

        while counter <= 5:
            board = player1.make_move(board)
            if(player1.run_checks(board)):
                print(f"""{player1.name} is the winner""")
                break
            board = player2.make_move(board)
            if(player2.run_checks(board)):
                print(f"""{player2.name} is the winner""")
                break
            print(board)
            
            counter += 1

        print("end")
        break

if __name__ == "__main__":
    main()