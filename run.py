# Write a tic tac toe game in python
from itertools import combinations
from time import sleep
import statistics

winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6,],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

class Player:
    name = ""
    symbol = ""
    moves = []

    def __init__(self,name,symbol,moves):
        self.name = name
        self.symbol = symbol
        self.moves = moves

    def make_move(self,possibles):
        move = input(f"""Player {self.name}, make your move : """)
        if(move.isnumeric() and int(move) in possibles):
            self.moves.append(int(move))
            return int(move)
        else:
            print("That was not a valid move")
            return self.make_move(possibles)

    def check_winner(self):
        self.moves.sort()
        if(len(self.moves) >= 3):
            isWinner = False
            for i in range(0,len(self.moves)):
                difference = self.moves[i+1] - self.moves[i]
                try:
                    if((self.moves[i+2] - self.moves[i+1]) == difference):
                        isWinner = True
                        break
                    else:
                        continue
                except:
                    break
            return isWinner

        else:
            return False
            
            





def main():
    while True:
        counter = 0
        moves = []
        winner = None

        board = [
            "","","",
            "","","",
            "","",""
        ]

        print("Welcome To Tic Tac Toe")

        player1 = Player(name=input("Player 1, enter your name : "),symbol=input("Player 1, enter your symbol : "),moves=[])
        player2 = Player(name=input("Player 2, enter your name : "),symbol=input("Player 2, enter your symbol : "),moves=[])

        if player1.symbol == player2.symbol:
            print("Please enter different names and symbols")
            break

        while counter < 5:
            #Find possible values in the array
            possibles = []
            for value in range(0,len(board)):
                if board[value] == "":
                    possibles.append(value)

            player_one_move = player1.make_move(possibles)
            possibles.remove(player_one_move)
            board[player_one_move] = player1.symbol

            if(player1.check_winner()):
                print("Player 1 is the winner")
                break

            player_two_move = player2.make_move(possibles)
            board[player_two_move] = player2.symbol

            if(player2.check_winner()):
                print("Player 2 is the winner")
                break


            print(board)
            counter += 1

if __name__ == "__main__":
    main()