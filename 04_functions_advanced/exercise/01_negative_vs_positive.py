# def num_sums(*args):
#     n_sum = sum(num for num in args if num < 0)
#     p_sum = sum(num for num in args if num > 0)
#
#     return n_sum, p_sum
#
#
# nums = map(int, input().split())
# neg_sum, pos_sum = num_sums(*nums)
#
# print(neg_sum)
# print(pos_sum)
# if abs(neg_sum) > pos_sum:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")

def is_num_positive(*args):
    result_p = 0
    result_n = 0
    for num in args:
        if num > 0:
            result_p += num
        elif num < 0:
            result_n += num
        else:
            pass
    return result_p, result_n


numbs = map(int, input().split())

positives, negatives = is_num_positive(*numbs)

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")

else:
    print("The positives are stronger than the negatives")