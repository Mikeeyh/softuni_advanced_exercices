test_dict = {'a': 1, 'b': 2, 'c': 3}
test_list = ('a', 'b', 'c')
letter = input()

try:
    print(test_list[8])
    print(test_dict[letter])  # if we type letter that is not in the dict it will return KeyError
except KeyError:
    print('Key Error')
except IndexError:
    print('Index Error')
else:
    print('No errors found')  # if we do not enter except we execute the code in else
finally:
    print('Program finished')  # finally will always print


try:
    print(test_list[8])
    print(test_dict[letter])
except (KeyError, IndexError):  # we can add more errors checks in except, we can also use more except functions
    print('Key or Index Error')
else:
    print('No errors found')
finally:
    print('Program finished')

# Error TYPE and Error Message
try:
    print(test_list[8])
    print(test_dict[letter])
except Exception as e:
    print(f'We have this error: {e}')  # it prints the error message
    print(f'Error type: {type(e)}')  # it prints the error type
    print('Key Error')
else:
    print('No errors found')
finally:
    print('Program finished')

