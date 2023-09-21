from random import *

my_password = input("\nEnter your password:")

password_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '^', '*']

password_found = ""

while password_found != my_password:
    guessPass = ""
    for letter in range(len(my_password)):
        guessLetter = password_chars[randint(0, 42)]
        password_found = str(guessLetter) + str(password_found)
    print(password_found)

print("Result marched password is: ", password_found)
