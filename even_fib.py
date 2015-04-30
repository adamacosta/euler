ans = 0
fib = 0
max = 4000000

f1 = 1
f2 = 1

while (fib < max):
    fib = f1 + f2
    ans += fib if fib % 2 == 0 else 0
    f1 = f2
    f2 = fib

print(ans)
