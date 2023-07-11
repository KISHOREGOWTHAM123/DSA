"""
    Prime Number (the number which can be divided by 1 and itself only)

    example
    2 -> smallest prime number
"""

def is_prime(num: int) -> bool:

    def factors(num: int) -> list[int]:
        return [i for i in range(1, num + 1) if num % i == 0]

    return factors(num) == [1, num]

def is_prime_method_2(num: int) -> bool:
    result: bool = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result 

# added optimization for iteration
# for prime numbers its enough to check only the n/2 elements
def is_prime_method_3(num: int) -> bool:
    import math
    result, count = True, 2
    while result and (count < math.sqrt(num)):
        if num % count == 0:
            result = False
        count += 1
    return result 


def prime_upto(num: int) -> list[int]:
    return [i for i in range(1, num + 1) if is_prime_method_3(i)]

print(prime_upto(10)) # [2, 3, 5, 7]


def first_n_primes(num: int) -> list[int]:
    count, primes, index = 0, [], 0
    while count < num:
        if is_prime(index):
            count, primes = count + 1, primes + [index]
        index += 1
    return primes

print(first_n_primes(10)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]