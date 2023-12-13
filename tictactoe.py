"""
    Tic-tac-toe game

    Description: Made to practice git and to code properly

    Author: Hansana Peiris
    Created: 13 Dec 2023

    GitHub repository: https://github.com/hansanapeiris/mini-games
"""

from time import sleep


class Player:

    def __init__(self, token:str) -> None:
        self.token = token
        
    def __str__(self) -> str:
        return self.token
    
    def get_tuple(self) -> tuple:
        row:str = input('row: ')
        while not row.isdigit():
            print('invalid input format, try again!')
            row:str = input('row: ')
        row = int(row)

        col:str = input('col: ')
        while not col.isdigit():
            print('invalid input format, try again!')
            col:str = input('col: ')
        col = int(col)

        return (row, col)

class Board:
    SIZE = 3

    class Slot:
        def __init__(self) -> None:
            self.token = None

        def change_token(self, token:str) -> bool:
            if self.token is not None:
                return False
            self.token = token
            return True
        
        def __str__(self) -> str:
            if self.token is None:
                return '_'
            return self.token

    def __init__(self) -> None:
        self.slots = []
        for i in range(Board.SIZE):
            row = [Board.Slot() for _ in range(Board.SIZE)]
            self.slots.append(row)

        self.empty_slot_count = Board.SIZE ** 2

    def check_for_wins(self) -> bool:
        # check all rows
        for row in self.slots:
            count_x = 0
            count_o = 0

            for slot in row:
                slot = str(slot)
                if slot == 'X':
                    count_x += 1
                elif slot == 'O':
                    count_o += 1
            
            if count_x == Board.SIZE:
                print('X wins')
                return True
            elif count_o == Board.SIZE:
                print('O wins')
                return True

        # check all columns
        for index in range(Board.SIZE):
            count_x = 0
            count_o = 0

            for row in self.slots:
                slot = row[index]
                slot = str(slot)
                if slot == 'X':
                    count_x += 1
                elif slot == 'O':
                    count_o += 1
            
            if count_x == Board.SIZE:
                print('X wins')
                return True
            elif count_o == Board.SIZE:
                print('O wins')
                return True

        # check diagonals
        count_x = 0
        count_o = 0
        for i in range(Board.SIZE):
            slot = self.slots[i][i]
            slot = str(slot)
            if slot == 'X':
                count_x += 1
            elif slot == 'O':
                count_o += 1
        if count_x == Board.SIZE:
            print('X wins')
            return True
        elif count_o == Board.SIZE:
            print('O wins')
            return True
        
        count_x = 0
        count_o = 0
        for i in range(Board.SIZE):
            slot = self.slots[i][i]
            slot = str(slot)
            if slot == 'X':
                count_x += 1
            elif slot == 'O':
                count_o += 1
        if count_x == Board.SIZE:
            print('X wins')
            return True
        elif count_o == Board.SIZE:
            print('O wins')
            return True

        count_x = 0
        count_o = 0
        for x, y in [(0,2), (1,1), (2,0)]:
            slot = self.slots[x][y]
            slot = str(slot)
            if slot == 'X':
                count_x += 1
            elif slot == 'O':
                count_o += 1
        if count_x == Board.SIZE:
            print('X wins')
            return True
        elif count_o == Board.SIZE:
            print('O wins')
            return True

        return False

    def mark_slot(self, row_no: int, col_no: int, token: str) -> bool:
        slot: Board.Slot = self.slots[row_no - 1][col_no - 1]
        success = slot.change_token(token)

        if success:
            self.empty_slot_count -= 1

        return success

    def display(self) -> None:
        print(' ', end='')
        for i in range(Board.SIZE):
            print(f" {i + 1}", end='')
        print()

        for i, row in enumerate(self.slots):
            print(f'{i + 1}|', end='')
            for slot in row:
                print(f'{slot}|', end='')
            print(f'{i + 1}')
        
        print(' ', end='')
        for i in range(Board.SIZE):
            print(f" {i + 1}", end='')
        print()

class Game:

    def __init__(self) -> None:

        # initialise players
        self.players = (Player('X'), Player('O'))

        # initilise board
        self.board = Board()

    def play(self) -> None:
        print("--GAME STARTED--")

        print('Player X goes first!')
        self.board.display()

        current_player_index = 0

        while self.board.empty_slot_count > 0:
            current_player = self.players[current_player_index]

            print(f"Player {current_player}'s turn")
            row, col = current_player.get_tuple()
            while not ((1 <= row <= Board.SIZE) and (1 <= col <= Board.SIZE)):
                print('out of range, try again!')
                row, col = current_player.get_tuple()
            
            result = self.board.mark_slot(row, col, current_player.token)

            if result:
                # go to next player
                current_player_index = not current_player_index
            else:
                # marking failed
                print('slot already taken!!')
                print(f"Player {current_player} try again!")
                sleep(1.5)

            self.board.display()

            if self.board.check_for_wins():
                break

        print("--GAME OVER--")
            

if __name__ == "__main__":
    game = Game()
    game.play()