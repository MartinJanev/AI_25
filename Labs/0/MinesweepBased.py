import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


def game(grid):
    N = len(grid)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def count_mines(x, y):
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == "#":
                count += 1
        return count

    return [
        [str(count_mines(i, j)) if grid[i][j] == '-' else '#' for j in range(N)]
        for i in range(N)
    ]


def main():
    N = int(input())
    grid = []

    for _ in range(N):
        row = input().split()
        grid.append(row)
    res = game(grid)

    for row in res:
        print("\t".join(row))


if __name__ == "__main__":
    main()
