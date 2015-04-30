import time

ones = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
         "seventeen","eighteen","nineteen"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = "hundred"
thousand = "onethousand"

def letter_count():
    """Input: None.
    Output: The letter count of English word representations of
    all numbers from 1 to 1000."""
    result = 0
    ones_sum = sum(len(num) for num in ones)
    teens_sum = sum(len(num) for num in teens)
    tens_sum = sum(len(num) for num in tens)
    under_hundred = teens_sum + 10 * tens_sum + 9 * ones_sum
    # Count one thousand
    result += len(thousand)
    # Count all values less than 100
    result += under_hundred
    # Count all values between 100 and 999
    result += 100 * ones_sum
    result += 9 * under_hundred
    result += 9 * len(hundred)
    result += 9 * 99 * (len(hundred) + len("and"))
    return result

t0 = time.time()
ans = letter_count()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
