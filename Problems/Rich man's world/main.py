amount = int(input())
i = 0
while amount < 700000:
    amount += amount*0.071
    i += 1
print(i)
