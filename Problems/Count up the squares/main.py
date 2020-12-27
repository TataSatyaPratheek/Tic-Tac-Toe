a = int(input())
sq = a**2
if a == 0:
    print(0)
else:
    while a != 0:
        b = int(input())
        a += b
        sq += b**2
    print(sq)