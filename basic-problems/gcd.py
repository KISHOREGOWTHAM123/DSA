"""
    GCD(greatest common divisor)

    example:
    gcd(6, 12) = 6 

"""


def gcd_method_1(num1: int, num2: int) -> int:
    cf: list = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            cf.append(i)
    return cf[-1]

print(gcd_method_1(6, 12)) # 6


# using list comprehension
def gcd_method_2(num1: int, num2: int) -> int:
    return [i for i in range(1, min(num1, num2) + 1) if num1 % i == 0 and num2 % i == 0][-1]

print(gcd_method_2(3, 6)) # 3

# reducing the space complexity
def gcd_method_3(num1: int, num2: int) -> int:
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            cf = i
    return cf

print(gcd_method_3(24, 50)) # 2

# recursive method to solve gcd
def gcd_method_4(num1: int, num2: int) -> int:
    a, b = max(num1, num2), min(num1, num2)
    if a % b == 0:
        return b
    else:
        return gcd_method_4(b, a - b)

print(gcd_method_4(5, 100)) # 5

# Euclid's Method (most optimized way)
def gcd_method_5(num1: int, num2: int) -> int:
    a, b = max(num1, num2), min(num1, num2)
    if a % b == 0:
        return b
    else:
        return gcd_method_4(b, a % b)

print(gcd_method_4(1234, 4321)) # 1