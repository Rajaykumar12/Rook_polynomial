from itertools import combinations

def rook_polynomial(board):
    m, n = len(board), len(board[0])  
    max_rooks = min(m, n)
    coefficients = []

    def is_valid_placement(placement):
        rows = set()
        cols = set()
        for r, c in placement:
            if r in rows or c in cols:
                return False
            rows.add(r)
            cols.add(c)
        return True

    
    for k in range(max_rooks + 1):
        valid_placements = 0
       
        cells = [(r, c) for r in range(m) for c in range(n) if board[r][c] == 1]
        for placement in combinations(cells, k):
            if is_valid_placement(placement):
                valid_placements += 1
        coefficients.append(valid_placements)

    
    polynomial = " + ".join(f"{coef}x^{i}" if i > 0 else str(coef) for i, coef in enumerate(coefficients))
    return polynomial


def get_board_from_user():
   
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("\nEnter the board row by row (1 for valid cell, 0 for invalid cell):")
    board = []
    for r in range(rows):
        while True:
            row = input(f"Row {r + 1}: ").strip().split()
            if len(row) == cols and all(cell in {'0', '1'} for cell in row):
                board.append(list(map(int, row)))
                break
            else:
                print(f"Invalid input. Enter exactly {cols} values (0 or 1).")

    return board


if __name__ == "__main__":
    print("Rook Polynomial Calculator")
    board = get_board_from_user()
    print("\nYour board:")
    for row in board:
        print(" ".join(map(str, row)))

    polynomial = rook_polynomial(board)
    print("\nRook Polynomial:", polynomial)
