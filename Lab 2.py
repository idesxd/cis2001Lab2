N = 8  # Board size is 8x8

MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid(x, y, board):
    """Check if (x, y) is inside the board and unvisited."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def count_onward_moves(x, y, board):
    """Count unvisited squares reachable from (x, y)."""
    count = 0
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            count += 1
    return count

def get_sorted_moves(x, y, board):
    """
    Generate next moves sorted by Warnsdorff’s rule:
    fewest onward moves first.
    """
    candidates = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            degree = count_onward_moves(nx, ny, board)
            candidates.append((degree, nx, ny))

    candidates.sort(key=lambda t: t[0])
    return [(nx, ny) for _, nx, ny in candidates]

def knight_tour(x, y, move_i, board):
    """Recursive backtracking solver."""
    if move_i == N * N:
        return True

    for nx, ny in get_sorted_moves(x, y, board):
        board[nx][ny] = move_i
        if knight_tour(nx, ny, move_i + 1, board):
            return True
        board[nx][ny] = -1  # backtrack

    return False

def solve_knights_tour(start_x=0, start_y=0):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = 0

    if knight_tour(start_x, start_y, 1, board):
        return board
    else:
        return None

def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))


solution = solve_knights_tour(0, 0)

if solution:
    print("Knight's Tour found:\n")
    print_board(solution)
else:
    print("No tour exists.")
#Extra
#CITATION, UMGPT PROMPT: How do i check if the tour is closed, what can i add after the completion?
def is_closed_tour(board, start_x, start_y):
    for i in range(N):
        for j in range(N):
            if board[i][j] == N * N - 1:
                end_x, end_y = i, j

    for dx, dy in MOVES:
        if end_x + dx == start_x and end_y + dy == start_y:
            return True
    return False
