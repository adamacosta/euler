three_range = int((999 - 999 % 3) / 3)
five_range = int((999 - 999 % 5) / 5) 
fifteen_range = int((999 - 999 % 15) / 15)

ans = 0
ans += (three_range * (3 + 3 * three_range)) / 2
ans += (five_range * (5 + 5 * five_range)) / 2
ans -= (fifteen_range * (15 + 15 * fifteen_range)) / 2

print(ans)
