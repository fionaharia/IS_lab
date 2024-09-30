from typing import List, Tuple

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_moves(board: List[List[int]]) -> List[List[List[int]]]:
    moves = []
    n = 3  
    empty_pos = find_empty_position(board)
    x, y = empty_pos
    
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        
        if is_valid_move(new_x, new_y, n):
            new_board = copy_board(board)
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            moves.append(new_board)
    
    return moves

def is_valid_move(x: int, y: int, n: int) -> bool:
    return 0 <= x < n and 0 <= y < n

def find_empty_position(board: List[List[int]]) -> Tuple[int, int]:
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    raise ValueError("No empty tile found in the board")

def copy_board(board: List[List[int]]) -> List[List[int]]:
    return [row.copy() for row in board]

def print_board(board: List[List[int]]) -> None:
    for row in board:
        print(' '.join(map(str, row)))
    print()

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    print("Initial Board:")
    print_board(initial_board)

    possible_moves = generate_moves(initial_board)

    print("Possible Moves:")
    for move in possible_moves:
        print_board(move)
