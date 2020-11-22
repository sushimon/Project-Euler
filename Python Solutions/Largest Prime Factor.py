# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
targ = 600851475143

def largestPrimeFact(targ):
    fact = 2
    while fact ** 2 <= targ:
        if targ % fact == 0:
            targ //= fact
        else:
            fact += 1
    if targ > fact:
        return targ
    return fact

print(largestPrimeFact(targ))