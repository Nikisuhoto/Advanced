def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


a = {"a": {1: [{'f': 1}]}, "b": [1, 2, 3], "c": {0: {1: {2: {"c": [{"k": 3}]}}}}}

print(recursive_power(2, 10))
