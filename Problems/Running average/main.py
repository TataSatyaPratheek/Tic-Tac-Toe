seq = input()
a = [(int(seq[i]) + int(seq[i+1]))/2.0 for i in range(len(seq)-1)]
print(a)