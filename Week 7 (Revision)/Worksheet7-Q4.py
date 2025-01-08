def check_move(position):
    if (len(position) != 2):
        return f"The position is not valid."

    # checking if position has right amount of characters
    else:
        column = position[0].upper()
        row = int(position[1])
        if ('A' <= column <= 'H'):
            if (1 <= row <= 8):
                return f"The piece is moved to {column}{row}."
            else:
                return f"The row value is not in the range 1 to 8!"
        else:
            return f"The column value is not in the range a-h or A-H!"

