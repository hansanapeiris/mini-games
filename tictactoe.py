"""
    Tic-tac-toe game

    Description: Made to practice git and to code properly

    Author: Hansana Peiris
    Created: 13 Dec 2023

    GitHub repository: https://github.com/hansanapeiris/mini-games
"""

class Player:

    def __init__(self, token:str) -> None:
        self.token = token
        
    def __str__(self) -> str:
        return self.token


class Console:
    @staticmethod
    def get_int_in_range(low:int = 0, high:int = float('inf'), prompt_for: str = "value") -> int:
        while True:
            try:
                value = int(input(f'{prompt_for}: '))
                if (value < low) or (value > high):
                    raise ValueError
                break
            except ValueError:
                print('invalid input format/range, try again!')
        return value


class Board:
    MIN_SIZE = 3
    MAX_SIZE = 9

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

    def __init__(self, size:int) -> None:
        self.slots = tuple(tuple(Board.Slot() for _ in range(size)) for _ in range(size))

        self.empty_slot_count = size ** 2

        right_diagonal = []
        for index in range(size):
            right_diagonal.append(self(index, index))
        self.right_diagonal = tuple(right_diagonal)

        left_diagonal = []
        for index in range(size):
            left_diagonal.append(self(index, (size-index - 1)))
        self.left_diagonal = tuple(left_diagonal)

    def __call__(self, row:int, col:int) -> Slot:
        return self.slots[row][col]
    
    def check_for_wins(self, row_no: int, col_no: int) -> bool:
        
        def has_same_tokens(slots: tuple[Board.Slot, ...]) -> bool:
            result = True
            for i in range(len(slots) - 1):
                result = result * (slots[i].token == slots[i+1].token)
            return bool(result)

        marked_row_index = row_no - 1
        marked_col_index = col_no - 1

        # to win, the token must have two pre/adjacent/post copies - Truple

        # error handles
        # - IndexErrors (out of range)
        # - list wrap around (negative indices)

        # check row
        marked_row = self.slots[marked_row_index]
        if has_same_tokens(marked_row):
            print('ROW WIN')
            return True

        # check column
        marked_col = []
        for row in self.slots:
            marked_col.append(row[marked_col_index])
        if has_same_tokens(marked_col):
            print('COLUMN WIN')
            return True

        # check right-diagonal
        if marked_row_index == marked_col_index:
            if has_same_tokens(self.right_diagonal):
                print('R-DIAGONAL WIN')
                return True

        # check left-diagonal
        if marked_row_index + marked_col_index == len(self.slots):
            if has_same_tokens(self.left_diagonal):
                print('R-DIAGONAL WIN')
                return True

        return False

    def mark_slot(self, row_no: int, col_no: int, token: str) -> bool:
        slot: Board.Slot = self.slots[row_no - 1][col_no - 1]
        success = slot.change_token(token)

        if success:
            self.empty_slot_count -= 1

        return success

    def display(self) -> None:
        print()
        print('\t⌜', end='')
        for i in range(len(self.slots)):
            print(f" {i + 1}", end='')
        print(' ⌝')

        for i, row in enumerate(self.slots):
            print(f'\t{i + 1}|', end='')
            for slot in row:
                print(f'{slot}|', end='')
            print(f'{i + 1}')
        
        print('\t⌞', end='')
        for i in range(len(self.slots)):
            print(f" {i + 1}", end='')
        print(' ⌟')
        print()


class TicTacToeGame:

    def __init__(self) -> None:
        board_size = Console.get_int_in_range(Board.MIN_SIZE, Board.MAX_SIZE, f"Board Size ({Board.MIN_SIZE} - {Board.MAX_SIZE})")

        # initialise players
        self.players = (Player('X'), Player('O'))

        # initilise board
        self.board = Board(board_size)

    def play(self) -> None:
        print("--GAME STARTED--")
        print('Player X goes first!')

        board_size = len(self.board.slots)

        current_player_index = 0

        while self.board.empty_slot_count > 0:
            self.board.display()
            current_player = self.players[current_player_index]

            print(f"Player {current_player}'s turn")

            row_no = Console.get_int_in_range(1, board_size, "row")
            col_no = Console.get_int_in_range(1, board_size, "col")
            
            result = self.board.mark_slot(row_no, col_no, current_player.token)

            if result:
                print(f"Player {current_player} marked ({row_no}, {col_no})")
                # go to next player
                current_player_index = not current_player_index

                if self.board.check_for_wins(row_no, col_no):
                    self.board.display()
                    print(f"Player {current_player} WINS!")
                    break
            else:
                # marking failed
                print(f'({row_no}, {col_no}) already marked!!')
                print(f"Player {current_player} try again!")

        else:
            print("\n--NO WINNERS--")

        print("--GAME OVER--")


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
