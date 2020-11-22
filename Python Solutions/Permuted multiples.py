# Permuted multiples
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
def solution():
    ans = 0
    count = 10
    
    while count < 10 ** 6:
        sols = [True]
        ans = count
        for i in range(2, 7):
            original = [x for x in str(count)]
            curr = [x for x in str(count * i)]
            for i in curr:
                if i in original:
                    original.remove(i)
            if len(original) == 0:
                sols.append(True)
            else:
                sols.append(False)
                break
        if not (False in sols):
            return ans
        count += 1

print(solution())