def numbers(*args):
    sum_positive = 0
    sum_negative = 0

    for num in args:
        num = int(num)
        if num < 0:
            sum_negative += num
        else:
            sum_positive += num

    print(sum_negative)
    print(sum_positive)

    if abs(sum_negative) > sum_positive:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


string = input().split()
print(numbers(*string))
