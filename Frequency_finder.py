file= open("words.txt", "r", encoding="UTF-8")
reader = file.read()
words = reader.split()
repeat = {}
for word in words:
    if word in repeat:
        repeat[word] = repeat[word] + 1
    else:
        repeat[word] = 1
print(repeat)
for key, value in repeat.items():
    print(key, "=", value)