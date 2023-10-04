import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", "r") as file:
    text = file.read().lower()

words = {}

for searched_word in searched_words:
    regex = re.compile(f"\b{searched_word}\b")
    result = re.findall(regex, text)
    words[searched_word] = len(result)

print(words)
