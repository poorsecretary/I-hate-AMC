import math
count = 0
count_list = []
for x in range(1, 51):
    numerator = math.factorial((pow(x, 2) - 1))
    denominator = pow(math.factorial(x), x)
    if numerator % denominator == 0:
        print('When x is {}, the expression result is an intenger.'.format(x))
        count += 1
        count_list.append(x)
print(count, '\n', count_list)
