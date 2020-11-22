# How many reversible numbers are there below one-billion?
def reverse(n):
    result = str(n)[::-1]
    return int(result)

def isOdd(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n //= 10
    return True

def solution():
    count = 0
    for i in range(1, 10 ** 9):
        if isOdd(i + reverse(i)) and i % 10 != 0:
            count += 1
    return count
    
print(solution())