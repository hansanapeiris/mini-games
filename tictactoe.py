"""
    Tic-tac-toe game

    Description: Made to practice using git and code

    Author: Hansana Peiris
    Created: 13 Dec 2023

    GitHub repository: https://github.com/hansanapeiris/mini-games
"""

from random import choice


class Player:
    def __init__(self, token:str) -> None:
        self.token = token
        
    def __str__(self) -> str:
        return self.token

class Slot:
    def __init__(self) -> None:
        self.state = None

    def __str__(self) -> str:
        if self.state is None:
            return '_'
        return self.state
    
    def change_state(self, token:str) -> bool:
        if self.state is None:
            self.state = token
            return True
        return False

class Board:
    SIZE = 3

    def __init__(self) -> None:
        self.slots = []
        for i in range(Board.SIZE):
            row = [Slot() for _ in range(Board.SIZE)]
            self.slots.append(row)

    def display(self) -> None:
        for row in self.slots:
            print('|', end='')
            for slot in row:
                print(f'{slot}|', end='')
            print()

class Game:

    def __init__(self) -> None:

        # initialise players
        self.players = (Player('X'), Player('O'))

        # initilise board
        self.board = Board()

    def play(self) -> None:
        print('X goes first!')

        current_player_index = 0

        while True:
            self.board.display()

            current_player = self.players[current_player_index]

            print(f"Player {current_player}'s turn")
            row = int(input('row: ')) - 1
            col = int(input('col: ')) - 1
            slot: Slot = self.board.slots[row][col]

            slot.change_state(current_player.token)

            current_player_index = not current_player_index

if __name__ == "__main__":
    game = Game()
    game.play()