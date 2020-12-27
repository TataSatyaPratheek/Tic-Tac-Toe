a = input()
max_num = 0
place = ''
if a == "MEOW":
    print(0)
else:
    max_num = int(a.split()[1])
    place = a.split()[0]
    b = input().split()
    while b[0] != "MEOW":
        if int(b[1]) > max_num:
            max_num = int(b[1])
            place = b[0]
        b = input().split()
    print(place)