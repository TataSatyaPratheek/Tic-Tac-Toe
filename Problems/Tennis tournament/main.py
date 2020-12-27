num = int(input())

list_ = []
for i in range(num):
    list_.append(list(input().split()))
a = [x[0] for x in list_ if x[1] == 'win']
print(a)
print(len(a))