word = input()

caps ='QWERTYUIOPASDFGHJKLZXCVBNM'

empty = []

for letter in word[1:]:
    if letter in caps:
        letter = "_" + letter.lower()
        empty.append(letter)
    else:
        empty.append(letter)

print(word[0].lower() + "".join(empty))