def grid(var):
    print('-' * 9)
    for line in range(3):
        print(f'|', end=' ')
        start = line * 3
        for loop_var in var[start:start + 3]:
            print(loop_var, end=' ')
        print('|')
    print('-' * 9)


def line_check(var, m_list):
    num = 0
    while num < len(m_list):
        if m_list[num] == [var, var, var]:
            return True
        num += 1


def diagonal_check(var, m_list):
    num = 0
    res = set()
    while num < len(m_list):
        res.add(m_list[num][num])
        num += 1
    if res == {var}:
        return True


def global_checker():
    res = set()
    if line_check("X", matrix):
        res.add("X")
    if line_check("O", matrix):
        res.add("O")
    if line_check("X", transpose):
        res.add("X")
    if line_check("O", transpose):
        res.add("O")
    if diagonal_check("X", matrix):
        res.add("X")
    if diagonal_check("O", matrix):
        res.add("O")
    if diagonal_check("X", reverse):
        res.add("X")
    if diagonal_check("O", reverse):
        res.add("O")
    return res


data = "_________"
grid(data)
data_list = list(data)

matrix = []
while data_list:
    matrix.append(data_list[:3])
    data_list = data_list[3:]

data_list = list(data)
loop_var = 1

while True:

    try:
        row, column = input("Enter the coordinates: ").split(" ")
    except ValueError:
        print("You should enter numbers!")
        continue
    if int(row) > 3 or int(column) > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    row = int(row) - 1
    column = int(column) - 1

    if matrix[row][column] == "X" or matrix[row][column] == "O":
        print("This cell is occupied! Choose another one!")
        continue

    if loop_var % 2 != 0:
        matrix[row][column] = "X"
    else:
        matrix[row][column] = "O"

    loop_var += 1
    flat_list = [item for sublist in matrix for item in sublist]
    grid(flat_list)
    transpose = [list(x) for x in zip(*matrix)]
    reverse = [elem[::-1] for elem in matrix]

    if global_checker() == {"X"}:
        print("X wins")
        break
    elif global_checker() == {"O"}:
        print("O wins")
        break
    elif flat_list.count("X") + flat_list.count("O") == 9:
        print("Draw")
        break
