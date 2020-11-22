# Large sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
file = open("large sum.txt", 'r')
sum1 = 0

for line in file:
    sum1 += int(line)

print(str(sum1)[:10])