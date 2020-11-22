# Digit factorials
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
fact = [1]
for i in range(1, 10):
    fact.append(fact[i-1] * i)

def digitFact(n):
    result = 0
    while n > 0:
        result += fact[int(n % 10)]
        n //= 10
    return result

def solution():
    result = 0
    for i in range(10, 7 * fact[9] + 1):
        if i == digitFact(i):
            result += i
    return result

print(solution())