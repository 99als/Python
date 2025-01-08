def check_move(column, row):
    column = column.upper()
    if ('A' <= column <= 'H'):
        if (1 <= row <= 8):
            return f"The piece is moved to {column}{row}."
        else:
            return f"The position is not valid."
    else:
        return f"The position is not valid."