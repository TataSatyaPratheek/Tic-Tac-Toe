text = input()
words = text.split()
for word in words:
    # finish the code here
    if word[:4] == "WWW." or word[:4] == "www.":
        print(word)
    elif word[:8] == "https://":
        print(word)
    elif word[:7] == "http://":
        print(word)