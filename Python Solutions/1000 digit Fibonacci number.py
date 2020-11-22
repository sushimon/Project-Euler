# 1000-digit Fibonacci number
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
def solution(digits):
    first = 1
    second = 1
    count = 1
    while True:
        count += 1
        if len(str(second)) == digits:
            return count
        else:
            second = first + second
            first = second - first

print(solution(1000))