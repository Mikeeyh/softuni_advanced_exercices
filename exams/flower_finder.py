from collections import deque

vowels = deque([x for x in input().split()])
consonants = input().split()

words = {"rose": "rose",
         "tulip": "tulip",
         "lotus": "lotus",
         "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words.keys():
        words[word] = words[word].replace(current_vowel, '')
        words[word] = words[word].replace(current_consonant, '')
        if words[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

# OR


def check_word(char, word):
    if char in word:
        word = word.replace(char, "")
    return word


flowers = ["rose", "tulip", "lotus", "daffodil"]
found_word = False

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for index in range(len(flowers)):
        flowers[index] = check_word(vowel, flowers[index])
        if flowers[index] == '':
            found_word = True
            break
        flowers[index] = check_word(consonant, flowers[index])
        if flowers[index] == '':
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
else:
    found_index = flowers.index("")
    if found_index == 0:
        print("Word found: rose")
    elif found_index == 1:
        print("Word found: tulip")
    elif found_index == 2:
        print("Word found: lotus")
    elif found_index == 3:
        print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
