name = input('What is the name of the robot?')
identifier = 2628

row_co = int(input('What is its current row coordinate?'))
col_co = int(input('What is its current column coordinate?'))
grid_size = 10

print(f'Hello. My name is {name}. My ID is {identifier}.')
if row_co < 0:
    row_co = 0
elif row_co > grid_size - 1:
    row_co = grid_size - 1
if col_co < 0:
    col_co = 0
elif col_co > grid_size - 1:
    col_co = grid_size - 1
if 0 <= row_co <= 4:
    if 0 <= col_co <= 4:
        print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
    elif 5 <= col_co <=9:
        print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
elif 5 <= row_co <= 9:
    if 0 <= col_co <= 4:
        print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
    elif 5 <= col_co <=9:
        print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')
