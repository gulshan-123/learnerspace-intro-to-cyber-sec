from pwn import *
import copy
from time import sleep
sudoku = [
    [-1, -1, 3, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [7, -1, -1, 1, -1, 3, -1, 5, -1],
    [-1, -1, -1, 3, -1, -1, 8, -1, 7],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [-1, -1, -1, -1, -1, -1, -1, 6, -1],
    [-1, -1, 1, -1, -1, -1, 9, 7, -1],
    [-1, -1, 2, -1, -1, 8, -1, -1, -1],
    [-1, -1, -1, 5, -1, -1, -1, -1, 2]
]

def print_sudoku(sudoku):
    for row in sudoku:
        print(row)

def is_valid(sudoku, row, col, num):
    # Check if the number is in the row
    if num in sudoku[row]:
        return False

    # Check if the number is in the column
    if num in [sudoku[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True

def solve_sudoku(sudoku_):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == -1:
                for num in range(1, 10):
                    if is_valid(sudoku, i, j, num):
                        sudoku[i][j] = num
                        if (solve_sudoku(sudoku)):
                            return True
                        sudoku[i][j] = -1
                return False
    return True

def compare_sudoku(sudoku, sudoku2):
    differences = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != sudoku2[i][j]:
                differences.append((i, j, sudoku2[i][j]))
    return differences

# print_sudoku(sudoku)
# print()
# solve_sudoku(sudoku)
# print()
# print_sudoku(sudoku)
y=[]



with process('./sudoku') as p:
    x=p.read().decode()
        # convert x to string
    x=x.split('\n')
    # print(x)
    for _ in range(len(x)):
        x[_]=x[_].strip()
        if x[_][0]==('|'):
            y.append(x[_])
    print('XXXXXXX')     
    print(x)
    print('YYYYY')
    print(y)
    print()
    assert len(y)==9
    for i in range(9):
        y[i]=y[i].split('|')[1:-1]
    # print(y)
    for i in range(len(y)):
        temp=''
        for j in range(len(y[i])):
            temp+=(y[i][j]).lstrip()
        y[i]=temp.rstrip()
    
    # concatenate all the strings by spaces
    temp=''
    for i in range(len(y)):
        temp+=y[i]+" "
    temp=temp
    # print ((temp))
    temp=temp.split(' ')[:81]
    rows=[temp[i:i+9] for i in range(0, len(temp), 9)]
    assert len(rows)==9
    sudoku= [[int(char) if char.isdigit() else -1 for char in row] for row in rows]

    soduku_ori=copy.deepcopy(sudoku)
    print_sudoku(sudoku)
    # print()
    solve_sudoku(sudoku)
    # print()
    # print_sudoku(sudoku)
    # print()
    differences=(compare_sudoku(soduku_ori,sudoku))
    print(differences)
    for stree2 in range(420):
        # p.recvuntil(b'i')
        print(stree2)
        sleep(0.06)
        # p.clean()
        for i in differences:
            # print(p.readline())
            if i==(differences[-1]):
                p.clean()
            p.sendline(bytes(f"{i[0]} {i[1]} {i[2]}\n",'ascii'))


# ----------------------------------------------------------------
# ----------------------------------------------------------------
    # for stree2 in range(420):
    #     print(stree2)
    #     y=[]
    #     x=p.read().decode()
    #     print(x)
    #     sentence_start = x.rfind("#")
    #     if sentence_start != -1:
    #         x = x[sentence_start:]
    #     else:
    #         x = ""  # or handle the case where "SENTENCE" is not found as needed
    #     x=x.split('\n')
    #     print(x)

    #     for munja in range(len(x)):
    #         x[munja]=x[munja].strip()
    #         if x[munja][0]==('|'):
    #             y.append(x[munja])
    #     print('XXXXXXX')     
    #     print(x)
    #     print('YYYYY')
    #     print(y)
    #     print()
    #     assert len(y)==9
    #     for i in range(9):
    #         y[i]=y[i].split('|')[1:-1]
    #     # print(y)
    #     for i in range(len(y)):
    #         temp=''
    #         for j in range(len(y[i])):
    #             temp+=(y[i][j]).lstrip()
    #         y[i]=temp.rstrip()
        
    #     # concatenate all the strings by spaces
    #     temp=''
    #     for i in range(len(y)):
    #         temp+=y[i]+" "
    #     temp=temp
    #     # print ((temp))
    #     temp=temp.split(' ')[:81]
    #     rows=[temp[i:i+9] for i in range(0, len(temp), 9)]
    #     assert len(rows)==9
    #     sudoku= [[int(char) if char.isdigit() else -1 for char in row] for row in rows]
    #     # print_sudoku(sudoku)
    #     soduku_ori=copy.deepcopy(sudoku)
    #     # print_sudoku(sudoku)
    #     # print()
    #     solve_sudoku(sudoku)
    #     # print()
    #     # print_sudoku(sudoku)
    #     # print()
    #     differences=(compare_sudoku(soduku_ori,sudoku))
    #     # print(differences)
    #     # p.clean()
    #     for i in range(len(differences)):
    #         # print(p.readline())
    #         if i%2==0 or i==len(differences)-1:
    #             p.clean()
    #         p.sendline(bytes(f"{differences[i][0]} {differences[i][1]} {differences[i][2]}\n",'ascii'))
    print(p.read().decode())



    
