def palindrome(word, index=0):
    new_word = ""
    for char in range(len(word) - 1, -1, -1):
        new_word += word[char]

    if word == new_word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
