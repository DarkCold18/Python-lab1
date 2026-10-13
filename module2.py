def sum_multiples_of_5():
    total_sum = 0
    for i in range(500, 1001):
        if i % 5 == 0:
            total_sum += i
    return total_sum
