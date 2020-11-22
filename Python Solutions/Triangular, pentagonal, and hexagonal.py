# Triangular, pentagonal, and hexagonal
# Find the next triangle number that is also pentagonal and hexagonal.
# only took like half an hour to run LOL
def triNum(n):
    result = (-1 + (1 - 4 * (-2 * n)) ** 0.5) / 2
    if result == int(result):
        return True
    return False

def pentNum(n):
    result = (1 + (1 - 4 * 3 * (-2 * n)) ** 0.5) / 6
    if result == int(result):
        return True
    return False

def hexNum(n):
    result = (1 + (1 - 4 * 2 * (-1 * n)) ** 0.5) / 4
    if result == int(result):
        return True
    return False

def solution():
    count = 40756
    while True:
        if triNum(count) and pentNum(count) and hexNum(count):
            return count
        count += 1

print(solution())
