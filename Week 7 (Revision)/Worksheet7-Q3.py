def check_move(column, row):
    column = column.upper()
    if ('A' <= column <= 'H'):
        if (1<= row <= 8):
            return f"The piece is moved to {column}{row}."
        else:
            return f"The row value is not in the range 1 to 8!"
    else:
        return f"The column value is not in the range a-h or A-H!"