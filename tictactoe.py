
class Player:
    # class variable
    player_count = 0

    def __init__(self, name:str = None) -> None:
        if not name:
            name = f'Player {Player.player_count + 1}'
        self.name = name
        Player.player_count += 1

    def get_name(self) -> str:
        return self.name

class Slot:
    def __init__(self) -> None:
        self.state = None

    def __str__(self) -> str:
        return '_'

class Board:
    def __init__(self, size:int = 3) -> None:
        self.size = size

        self.slots = []
        for i in range(size):
            row = [Slot()] * size
            self.slots.append(row)

    def display(self) -> None:
        for row in self.slots:
            print('|', end='')
            for slot in row:
                print(f'{slot}|', end='')
            print()

class Game:
    MAX_PLAYER_COUNT = 2

    def __init__(self) -> None:
        self.players = []
        for _ in range(Game.MAX_PLAYER_COUNT):
            self.players.append(Player(input('name: ')))
        
        for player in self.players:
            print(player.get_name())

        self.board = Board()

game = Game()
print(Player.player_count)

print(game.board.display())