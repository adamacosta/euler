def square_of_sums(n):
    return int((n * (n + 1) / 2) ** 2)

def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)

def sum_square_diff(n):
    return square_of_sums(n) - sum_of_squares(n)

num = 100

print(sum_square_diff(num))
