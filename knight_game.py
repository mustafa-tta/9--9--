def knight_moves(position):
    row, col = position
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    valid_moves = []
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            valid_moves.append((new_row, new_col))
    return valid_moves

def print_board(knight_pos):
    valid_moves = knight_moves(knight_pos)
    for r in range(8):
        row_str = ""
        for c in range(8):
            if (r, c) == knight_pos:
                row_str += " K "   # Knight position
            elif (r, c) in valid_moves:
                row_str += " * "   # Possible moves
            else:
                row_str += " . "   # Empty square
        print(row_str)
    print()

def main():
    knight_pos = (0, 1)  # start at row 0, column 1
    while True:
        print_board(knight_pos)
        print("Knight is at:", knight_pos)
        print("Valid moves:", knight_moves(knight_pos))
        
        move = input("Enter new position as 'row col' (or 'q' to quit): ")
        if move.lower() == 'q':
            break
        
        try:
            r, c = map(int, move.split())
            if (r, c) in knight_moves(knight_pos):
                knight_pos = (r, c)
            else:
                print("Invalid move! Try again.")
        except:
            print("Invalid input format. Use: row col")

if __name__ == "__main__":
    main()