# Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sumSquares(upper):
    sum1 = 0
    for i in range(1, upper + 1):
        sum1 += i ** 2
    return sum1

def squareSum(upper):
    sum1 = (upper * (2 + (upper - 1))) // 2
    return sum1 ** 2

def diffSums(targ):
    print(squareSum(targ) - sumSquares(targ))

diffSums(100)