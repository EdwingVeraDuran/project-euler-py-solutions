import math
from functools import reduce


def mcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


smallest_number = reduce(mcm, range(1, 21))

print(f"Smallest evenly divisible number from 1 to 20: {smallest_number}")
