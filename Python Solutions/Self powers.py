# Self powers
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
def solution(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** i
    return str(result)[-10:]

print(solution(1000))