# Factorial digit sum
# Find the sum of the digits in the number 100!
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result

print(solution(fact(100)))