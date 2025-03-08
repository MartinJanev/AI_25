import random, os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, position):
        self.x, self.y = position


class Game:
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid

    def valid_moves(self, positions):
        moves = []
        x, y = positions
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        for dx, dy in directions:
            ny, nx = y + dy, x + dx
            if 0 <= nx < self.height and 0 <= ny < self.width:
                moves.append((nx, ny))
        return moves

    def is_point(self, x, y):
        return self.grid[x][y] == "."

    def rm_point(self, player):
        if self.is_point(player.x, player.y):
            self.grid[player.x][player.y] = "#"

    def has_points(self):
        for row in self.grid:
            if "." in row:
                return True
        return False


class Pacman:
    def __init__(self, width, height, grid):
        self.player = Player()
        self.game = Game(width, height, grid)

    def play(self):
        if not self.game.has_points():
            print("No more points")
            return

        steps = 0
        while self.game.has_points():
            x, y = self.player.x, self.player.y
            valid_moves = self.game.valid_moves((x, y))

            point_moves = [
                move for move in valid_moves if self.game.is_point(move[0], move[1])
            ]
            if point_moves:
                move = random.choice(point_moves)
            else:
                move = random.choice(valid_moves)

            self.player.move(move)
            self.game.rm_point(self.player)
            steps += 1
            print(f"[{self.player.x}, {self.player.y}]")

        print(f"Game Over in {steps} steps")


if __name__ == "__main__":
    width = int(input())
    height = int(input())
    grid = [list(input()) for _ in range(height)]

    pacman = Pacman(width, height, grid)
    pacman.play()
