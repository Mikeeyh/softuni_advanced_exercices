from collections import deque

sequence_of_parentheses = deque(input())
opening_parentheses = '([{'
closing_parentheses = ')]}'
counter = 0

while sequence_of_parentheses and counter < len(sequence_of_parentheses) / 2: # checks if balanced are until the middle

    if sequence_of_parentheses[0] not in opening_parentheses: # checks if the sequence starts with opening parentheses
        break

    index = opening_parentheses.index(sequence_of_parentheses[0]) # checks the index of the first opening parentheses
    if sequence_of_parentheses[1] == closing_parentheses[index]: # checks if the sequence ends with the same type par.
        sequence_of_parentheses.popleft()
        sequence_of_parentheses.popleft()
        sequence_of_parentheses.rotate(counter) # rotates 'counter' times to revert the initial sequence
        counter = 0
    else:
        sequence_of_parentheses.rotate(-1) # rotates to move the current element to last position
        counter += 1

if sequence_of_parentheses: # if the is something left in the sequence_of_parentheses it means that it is not balanced
    print('NO')
else:
    print('YES')
