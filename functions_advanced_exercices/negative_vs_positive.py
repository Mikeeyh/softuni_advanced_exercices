def num_sums(*args):
    neg_sum = sum([x for x in args if x < 0])
    pos_sum = sum([x for x in args if x > 0])

    return neg_sum, pos_sum


nums = [int(x) for x in input().split()]
print(num_sums(*nums)[0])  # *nums -> unpacking of our list, [0] position in index 0 because = neg_sum
print(num_sums(*nums)[1])  # if we give nums instead of *nums we will have ([1, 2, 3]) and not (1, 2, 3)

if abs(num_sums(*nums)[0]) > num_sums(*nums)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

# OR ---------------------------------------------------------------------------------


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
