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
        self.slots = []
        for _ in range(size):
            row = [Board.Slot() for _ in range(size)]
            self.slots.append(row)

        self.empty_slot_count = size ** 2

    # def __call__(self, row:int, col:int) -> Slot:
    #     return self.slots[row][col]

    def are_slots_available(self) -> bool:
        return self.empty_slot_count > 0
    
    def check_for_wins(self, row_no: int, col_no: int) -> bool:
        
        def has_same_tokens(three_slots: tuple[Board.Slot, Board.Slot, Board.Slot]) -> bool:
            return three_slots[0].token == three_slots[1].token == three_slots[2].token

        marked_row_index = row_no - 1
        marked_col_index = col_no - 1

        # to win, the token must have two pre/adjacent/post copies - Truple

        # error handles
        # - IndexErrors (out of range)
        # - list wrap around (negative indices)

        # check row
        starting_col_indices_for_truples = (marked_col_index-2, marked_col_index-1, marked_col_index)
        for col in starting_col_indices_for_truples:
            try:
                if col < 0:
                    continue

                slot_truple = (self.slots[marked_row_index][col], self.slots[marked_row_index][col+1], self.slots[marked_row_index][col+2])
                if has_same_tokens(slot_truple):
                    print("ROW WIN")
                    return True
            except IndexError:
                continue

        # check column
        starting_row_indices_for_truples = (marked_row_index-2, marked_row_index-1, marked_row_index)
        for row in starting_row_indices_for_truples:
            try:
                if row < 0:
                    continue
                
                slot_truple = (self.slots[row][marked_col_index], self.slots[row+1][marked_col_index], self.slots[row+2][marked_col_index])
                if has_same_tokens(slot_truple):
                    print("COLUMN WIN")
                    return True
            except IndexError:
                continue

        # check right-diagonal
        starting_slot_location_for_truples = ( (marked_row_index-2, marked_col_index-2),
                                   (marked_row_index-1, marked_col_index-1),
                                   (marked_row_index, marked_col_index) )
        
        for row, col in starting_slot_location_for_truples:
            try:
                if row < 0 or col < 0:
                    continue
                
                slot_truple = (self.slots[row][col], self.slots[row+1][col+1], self.slots[row+2][col+2])
                if has_same_tokens(slot_truple):
                    print("RIGHT-DIAGONAL WIN")
                    return True
            except IndexError:
                continue

        # check left-diagonal
        starting_slot_location_for_truples = ( (marked_row_index+2, marked_col_index-2),
                                   (marked_row_index+1, marked_col_index-1),
                                   (marked_row_index, marked_col_index) )
        
        for row, col in starting_slot_location_for_truples:
            try:
                if row < 0 or col < 0:
                    continue
                
                slot_truple = (self.slots[row][col], self.slots[row-1][col+1], self.slots[row-2][col+2])
                if has_same_tokens(slot_truple):
                    print("LEFT-DIAGONAL WIN")
                    return True
            except IndexError:
                continue

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

        current_player_index = 0

        while self.board.are_slots_available():
            self.board.display()
            current_player = self.players[current_player_index]

            print(f"Player {current_player}'s turn")

            row_no = Console.get_int_in_range(1, len(self.board.slots), "row")
            col_no = Console.get_int_in_range(1, len(self.board.slots), "col")
            
            result = self.board.mark_slot(row_no, col_no, current_player.token)

            if result:
                print(f"Player {current_player} marked ({row_no}, {col_no})")
                # go to next player
                current_player_index = not current_player_index

                if self.board.check_for_wins(row_no, col_no):
                    print(f"Player {current_player} WINS!")
                    break
            else:
                # marking failed
                print(f'({row_no}, {col_no}) already marked!!')
                print(f"Player {current_player} try again!")

        else:
            print("\n--NO WINNERS--")

        self.board.display()
        print("--GAME OVER--")


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
