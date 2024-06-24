name = input('What is the name of the robot?')
identifier = 2628

row_co = int(input('What is its current row coordinate?'))
col_co = int(input('What is its current column coordinate?'))
grid_size = 10
max_row = grid_size - 1
max_col = grid_size - 1

init_dir = input('What is its initial direction [n|s|e|w]?')

print(f'Hello. My name is {name}. My ID is {identifier}.')

if row_co < 0:
    row_co = 0
elif row_co > max_row:
    row_co = max_row
if col_co < 0:
    col_co = 0
elif col_co > max_col:
    col_co = max_col
if 0 <= row_co <= max_row // 2:
    if 0 <= col_co <= max_col // 2:
        print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
    elif 5 <= col_co <= max_col:
        print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
elif 5 <= row_co <= max_row:
    if 0 <= col_co <= max_col // 2:
        print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
    elif 5 <= col_co <= max_col:
        print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')

if init_dir == 'n':
    print('I am facing North.')
    print('Moving one step forward.')
    row_co -= 1
    if row_co > max_row:
        row_co = max_row
    if 0 <= row_co <= max_row // 2:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
    elif 5 <= row_co <= max_row:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')


if init_dir == 's':
    print('I am facing South.')
    print('Moving one step forward.')
    row_co += 1
    if row_co > max_row:
        row_co = max_row
    if 0 <= row_co <= max_row // 2:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
    elif 5 <= row_co <= max_row:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')

if init_dir == 'e':
    print('I am facing East.')
    print('Moving one step forward.')
    col_co += 1
    if col_co > max_col:
        col_co = max_col
    if 0 <= row_co <= max_row // 2:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
    elif 5 <= row_co <= max_row:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')

if init_dir == 'w':
    print('I am facing West.')
    print('Moving one step forward.')
    col_co -= 1
    if col_co > max_col:
        col_co = max_col
    if 0 <= row_co <= max_row // 2:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the top left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the top right quadrant.')
    elif 5 <= row_co <= max_row:
        if 0 <= col_co <= max_col // 2:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom left quadrant.')
        elif 5 <= col_co <= max_col:
            print(f'My curren location is ({row_co},{col_co}). I am in the bottom right quadrant.')
