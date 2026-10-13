import math

def calculate_expression(a, b, x, y):
    numerator = abs(a - b) + math.cos(x)
    denominator = 1 + math.sqrt(y)
    return numerator / denominator
