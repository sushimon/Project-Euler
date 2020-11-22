# Power digit sum
# What is the sum of the digits of the number 2^1000?
def powerDigitSum(base, exp):
    sumDigits = 0
    power = base ** exp
    for i in str(power):
        sumDigits += int(i)
    return sumDigits

print(powerDigitSum(2, 1000))