size = int(input())

if size <1:
    print("no army")
elif (size <=9):
    print('few')
elif size <=49:
    print('pack')
elif size <=499:
    print('horde')
elif size<=999:
    print('swarm')
elif size>=1000:
    print('legion')