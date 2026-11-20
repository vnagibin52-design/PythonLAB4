words = ["кот", "собака", "кот", "мышь", "собака"]

words_dict = {}
for word in words:
    words_dict[word] = len(word)

words_dict2 = {word: len(word) for word in words}

print(words_dict)
print(words_dict2)