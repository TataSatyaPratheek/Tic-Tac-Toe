# write your code here
a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(f"""
---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} | 
| {a[6]} {a[7]} {a[8]} | 
---------""")
num_turns = 0
result = False
pos = ["11", '12', '13', '21', '22', '23', '31', '32', '33']
vic_pos = [[a[0], a[1], a[2]],
               [a[3], a[4], a[5]],
               [a[6], a[7], a[8]],
               [a[0], a[3], a[6]],
               [a[1], a[4], a[7]],
               [a[2], a[5], a[8]],
               [a[0], a[4], a[8]],
               [a[2], a[4], a[6]]
               ]
while result is False:
    num_x = a.count("X")
    num_o = a.count("O")
    if abs(num_o-num_x) > 1:
        print("Impossible")
        result = True
    elif (['X', 'X', 'X'] in vic_pos) and (['O', 'O', 'O'] in vic_pos):
        print("Impossible")
        result = True
    elif num_o + num_x < 9:
        b = input().replace(" ", '')
        if num_turns % 2 == 0:
            while b not in pos:
                if not b.isnumeric():
                    print("You should enter numbers!")
                elif b not in pos:
                    print("Coordinates should be from 1 to 3!")
                b = input().replace(" ", '')
            while a[3 * (int(b[0]) - 1) + int(b[1]) - 1] != ' ':
                print("This cell is occupied! Choose another one!")
                b = input().replace(" ", '')
                while b not in pos:
                    if not b.isnumeric():
                        print("You should enter numbers!")
                    elif b not in pos:
                        print("Coordinates should be from 1 to 3!")
                    b = input().replace(" ", '')
            a[3 * (int(b[0]) - 1) + int(b[1]) - 1] = "X"
            print(f"""
            ---------
            | {a[0]} {a[1]} {a[2]} |
            | {a[3]} {a[4]} {a[5]} | 
            | {a[6]} {a[7]} {a[8]} | 
            ---------""")
            vic_pos = [[a[0], a[1], a[2]],
                       [a[3], a[4], a[5]],
                       [a[6], a[7], a[8]],
                       [a[0], a[3], a[6]],
                       [a[1], a[4], a[7]],
                       [a[2], a[5], a[8]],
                       [a[0], a[4], a[8]],
                       [a[2], a[4], a[6]]
                       ]
            num_turns += 1
            if ['X', 'X', 'X'] in vic_pos:
                print("X wins")
                result = True
        else:
            while b not in pos:
                if not b.isnumeric():
                    print("You should enter numbers!")
                elif b not in pos:
                    print("Coordinates should be from 1 to 3!")
                b = input().replace(" ", '')
            while a[3 * (int(b[0]) - 1) + int(b[1]) - 1] != " ":
                print("This cell is occupied! Choose another one!")
                b = input().replace(" ", '')
                while b not in pos:
                    if not b.isnumeric():
                        print("You should enter numbers!")
                    elif b not in pos:
                        print("Coordinates should be from 1 to 3!")
                    b = input().replace(" ", '')
            a[3 * (int(b[0]) - 1) + int(b[1]) - 1] = "O"
            print(f"""
            ---------
            | {a[0]} {a[1]} {a[2]} |
            | {a[3]} {a[4]} {a[5]} | 
            | {a[6]} {a[7]} {a[8]} | 
            ---------""")
            vic_pos = [[a[0], a[1], a[2]],
                       [a[3], a[4], a[5]],
                       [a[6], a[7], a[8]],
                       [a[0], a[3], a[6]],
                       [a[1], a[4], a[7]],
                       [a[2], a[5], a[8]],
                       [a[0], a[4], a[8]],
                       [a[2], a[4], a[6]]
                       ]
            num_turns += 1
            if ['O', 'O', 'O'] in vic_pos:
                print("O wins")
                result = True
    elif not ((['X', 'X', 'X'] in vic_pos) and (['O', 'O', 'O'] in vic_pos)):
        print("Draw")
        result = True



"""
check if the current game is legal
    count the number of x and o
    check if the difference between num x and num o is 0 or 1 
    check if both x and o dont oc 

check if the game is complete 
"""