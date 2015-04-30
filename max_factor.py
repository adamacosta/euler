def max_factor(n):
    lpf = 3
    while n > 1:
        f = lpf
        if n % f == 0:
            n //= f
        else:
            lpf += 2
    return lpf

test_num = 600851475143

print(max_factor(test_num))
